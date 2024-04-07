import pandas as pd
import re
import sys
import argparse
from solver import extract_equation



def find_symbolic_form(response):
    symbolic_form_match = re.search(r'\[\[(.*?)\]\]', response)
    if symbolic_form_match:
        return symbolic_form_match.group(0)
    return "Failed"

def Result_From_Symbolic_Form(symbolic_Form):
    if symbolic_Form == "Failed":
        return "Failed to find symbolic form"
    try:
        result = extract_equation(symbolic_Form)
        result_type = type(result)
        if not result:
            return "No solution exists"
        elif (result_type == list):
            if len(result) == 1:
                return result[0]
        else:
            return result
    except Exception as e:
        return "Error: " + str(e)

def main(Predict_path, Test_path):
    print("Predict_path: ", Predict_path)
    print("Test_path: ", Test_path)

    df = pd.read_json(Predict_path, lines=True)

    df['predict'] = df['predict'].apply(lambda x: re.sub(r'.*Problem:\s*', '', x))
    df['predict'] = df['predict'].apply(lambda x: x.split(']]')[0] + ']]')
    df['SymbolicForm'] = df['predict'].apply(find_symbolic_form)
    df['SymbolicAnswer'] = df['SymbolicForm'].apply(Result_From_Symbolic_Form)

    question = pd.read_json(Test_path, lines=True)

    question['SymbolicAnswer'] = question['Symbolic Form'].apply(Result_From_Symbolic_Form)
    question.head()

    df.drop(columns=['label'], inplace=True)
    question.drop(columns=['Answer',"Source",], inplace=True)
    question.rename(columns={'SymbolicAnswer': 'Answer'}, inplace=True)
    result = pd.merge(df, question, left_index=True, right_index=True)
    result['Math'] = result['SymbolicAnswer'] == result['Answer']
    result['Math'].value_counts()
    accuracy = result['Math'].value_counts()[0] / len(result)
    print(f"Accuracy: {accuracy}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Evaluate prediction accuracy.')
    parser.add_argument('Predict_path', type=str, help='Path to the prediction file')
    parser.add_argument('Test_path', type=str, help='Path to the test file')
    args = parser.parse_args()
    main(args.Predict_path, args.Test_path)
