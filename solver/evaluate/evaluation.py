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
    # Print input paths
    print(f"\nEvaluating predictions from: {Predict_path}")
    print(f"Against test data from: {Test_path}\n")

    # Load and process prediction data
    predictions_df = pd.read_json(Predict_path, lines=True)
    predictions_df['SymbolicForm'] = predictions_df['predict'].apply(find_symbolic_form)
    predictions_df['PredictSymbolicAnswer'] = predictions_df['SymbolicForm'].apply(Result_From_Symbolic_Form)

    # Load and process test data
    test_df = pd.read_json(Test_path, lines=True)
    test_df['SymbolicAnswer'] = test_df['Symbolic Form'].apply(Result_From_Symbolic_Form)

    # Merge and compare results
    result = pd.merge(predictions_df, test_df, left_index=True, right_index=True)
    result['Match'] = result.apply(lambda x: compareResult(x['PredictSymbolicAnswer'], x['SymbolicAnswer']), axis=1)

    # Calculate and display metrics
    total_questions = len(result)
    correct_answers = result['Match'].sum()
    accuracy = correct_answers / total_questions
    fixed_score = result[result['Match'] == True]['Fixed'].sum()

    print("Results:")
    print("-" * 50)
    print(f"Total Questions: {total_questions}")
    print(f"Correct Answers: {correct_answers}")
    print(f"Accuracy: {accuracy:.2%}")
    print(f"Score: {fixed_score}")
    print("-" * 50)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Evaluate prediction accuracy.')
    parser.add_argument('Predict_path', type=str, help='Path to the prediction file')
    parser.add_argument('Test_path', type=str, help='Path to the test file')
    args = parser.parse_args()
    main(args.Predict_path, args.Test_path)
