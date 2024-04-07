from sympy import symbols, cos, simplify, trigsimp, factor, solveset, S, Eq, solve, solve_univariate_inequality
# from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor
import sympy


# transformation = (standard_transformations + (implicit_multiplication_application,) + (convert_xor,))
def GetExpression(Equation_to_Solve):
    Equation = Equation_to_Solve[0]
    Symbol = []
    symbol_appear = 0
    for nums,expr in enumerate(Equation_to_Solve[1:]):   
        if len(str(expr)) == 1:
            if str(expr).isdigit():
                pass
            else:
                if isinstance(expr, sympy.Symbol):
                    Symbol.append(expr)
                    symbol_appear = nums
        else:
            pass
    return Equation_to_Solve[:(symbol_appear+1)]
def symplify_trigometry(expr):
    print("in trigometry")
    expr = GetExpression(expr)
    simplified_expr = trigsimp(expr)
    print(simplified_expr)
    expand_expr = simplified_expr[0].expand(trig=True)
    print(expand_expr)

    return simplified_expr
    