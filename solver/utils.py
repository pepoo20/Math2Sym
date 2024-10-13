import sympy

def Operation(Equation_to_Solve, operator):
    x = Equation_to_Solve.pop()
    y = Equation_to_Solve.pop()
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    elif operator == '/':
        return x / y
    
def my_igcd(Equation_to_Solve):
    print("Equation to Solve: ", Equation_to_Solve)
    try :
        return sympy.igcd(*Equation_to_Solve)
    except ValueError:
        return sympy.gcd(*Equation_to_Solve)
def my_ilcm(Equation_to_Solve):
    try:
        return sympy.ilcm(*Equation_to_Solve)
    except ValueError:
        return sympy.lcm(*Equation_to_Solve)
