import sympy
from sympy import symbols, cos, simplify, trigsimp, factor, solveset, S, Eq, solve, solve_univariate_inequality
import re
from .solve_function import Solve, Relation
from .utils import Operation, my_igcd, my_ilcm
import time, threading
import stopit
Relation = Relation
Action = ['solve', 'igcd', 'ilcm', 'divisible', 'simplify','lcm']

def isOperator(x):
    return x in ['+', '-', '*', '/']

def isAction(x):
    return x in Action

def doAction(Equation_to_Solve, action):
    if action == 'solve':
        return Solve(Equation_to_Solve)
    elif action == 'igcd':
        return my_igcd(Equation_to_Solve)
    elif action == 'ilcm':
        return my_ilcm(Equation_to_Solve)
    
def parse_combination_and_permutation(equation):
    # find all permutation whose format is num1Anum2
    permutation = re.findall(r'\d+P\d+', equation)
    for item in permutation:
        num1, num2 = item.split('P')
        equation = equation.replace(item, str(sympy.factorial(int(num1))//sympy.factorial(int(num1)-int(num2))))
    
    # find all combination whose format is num1Cnum2
    combination = re.findall(r'\d+C\d+', equation)
    for item in combination:
        num1, num2 = item.split('C')
        equation = equation.replace(item, str(sympy.binomial(int(num1), int(num2))))
    
    return equation

def parse_percentage(equation):
    percentage = re.findall(r'\d+%', equation)
    for item in percentage:
        num = item.replace('%', '')
        equation = equation.replace(item, str(int(num)/100))
    return equation
def replace_p_string(match):
    return 'P' + match.group(1).replace(' ', '')
def replace_n_string(match):
    return 'n' + match.group(1).replace(' ', '')
def replace_or_sign(equation):
    for i in range(97, 123):
        if chr(i) not in equation:
            equation = equation.replace('|', chr(i))
            break
    return equation

def remove_commas_in_numbers(input_string):
    # Define a regex pattern to find numbers with commas. ex : 1,000,000
    pattern = r'\b\d{1,3}(?:,\d{3})+\b'

    def replace_commas(match):
        return match.group().replace(',', '')
    
    result = re.sub(pattern, replace_commas, input_string)
    return result

def parse_and_simplify_equation(equation):
    parse_equation = equation
    parse_equation = re.findall(r'\[\[(.*?)\]\]', parse_equation)[0].split(',')
    parse_equation = [parse_percentage(item.strip()) for item in parse_equation]
    parse_equation = [simplify(item.strip()) if item.strip() not in Action and item.strip() not in Relation else item.strip() for item in parse_equation]
    return parse_equation

@stopit.threading_timeoutable(default="Time limit exceeded")
def extract_equation(parse_equation):
    parse_equation = parse_and_simplify_equation(parse_equation)
    Equation_to_Solve = []
    if not any([isAction(x) for x in parse_equation]):
        return "No Action Found"
    for i in range(len(parse_equation)):
        if isOperator(parse_equation[i]):
            number = Operation(Equation_to_Solve, parse_equation[i])
            Equation_to_Solve.append(number)
        elif isAction(parse_equation[i]):
            result = doAction(Equation_to_Solve, parse_equation[i])
            return result
        else:
            Equation_to_Solve.append(parse_equation[i])
            
    return Equation_to_Solve