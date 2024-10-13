import pandas as pd
import re
import sys
import argparse
from ..solve_main import extract_equation
import sympy


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
def preprocess_result_TypeAnd(result):
    variables = re.findall(r'\b[a-zA-Z]+\b', result)
    
    mapping = {}
    replacements = ['x', 'y', 'z']
    
    for variable in variables:
        if variable not in mapping:
            if len(mapping) < len(replacements):
                mapping[variable] = replacements[len(mapping)]
            else:
                mapping[variable] = replacements[-1]

    if not mapping:
        return result
    preprocessed_result = re.sub(r'\b(' + '|'.join(mapping.keys()) + r')\b', lambda m: mapping[m.group()], result)
    
    return preprocessed_result
def compare_result_TypeAnd(result1, result2):
    return preprocess_result_TypeAnd(result1) == preprocess_result_TypeAnd(result2)
def compare_values_dict(dict1, dict2):
    array_dict1 = list(dict1.values())
    array_dict2 = list(dict2.values())

    array_dict1.sort()
    array_dict2.sort()
    return array_dict1 == array_dict2
def compareResult(result1, result2):
    if type(result1) == dict and type(result2) == dict:
        return compare_values_dict(result1, result2)
    elif type(result1) == sympy.logic.boolalg.And and type(result2) == sympy.logic.boolalg.And:
        return compare_result_TypeAnd(str(result1), str(result2))
    else:
        return result1 == result2

def main(Predict_path, Test_path):
    print("Predict_path: ", Predict_path)
    print("Test_path: ", Test_path)

    df = pd.read_json(Predict_path, lines=True)
    df['SymbolicForm'] = df['predict'].apply(find_symbolic_form)
    df['PredictSymbolicAnswer'] = df['SymbolicForm'].apply(Result_From_Symbolic_Form)

    question = pd.read_json(Test_path, lines=True)
    question['SymbolicAnswer'] = question['Symbolic Form'].apply(Result_From_Symbolic_Form)
    result = pd.merge(df, question, left_index=True, right_index=True)

    result['Match'] = result.apply(lambda x: compareResult(x['PredictSymbolicAnswer'], x['SymbolicAnswer']), axis=1)

    print(result['Match'].value_counts())
    accuracy = result['Match'].value_counts()[0] / len(result)
    print(f"Accuracy: {accuracy}")
    print(result[result['Match'] == True]['Fixed'].sum())
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Evaluate prediction accuracy.')
    parser.add_argument('Predict_path', type=str, help='Path to the prediction file')
    parser.add_argument('Test_path', type=str, help='Path to the test file')
    args = parser.parse_args()
    main(args.Predict_path, args.Test_path)
