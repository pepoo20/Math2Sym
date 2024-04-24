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

def divisible(x, y):
    if x % y == 0:
        return "{x} is divisible by {y}".format(x=x, y=y)
    else:
        return "{x} is not divisible by {y}".format(x=x, y=y)


def my_igcd(Equation_to_Solve):
    return sympy.igcd(*Equation_to_Solve)

def my_ilcm(Equation_to_Solve):
    try:
        return sympy.ilcm(*Equation_to_Solve)
    except ValueError:
        return sympy.lcm(*Equation_to_Solve)

def my_lcm(Equation_to_Solve):
    return sympy.lcm(*Equation_to_Solve)

