
from sympy import symbols, solveset, S, Eq, solve, solve_univariate_inequality
import sympy
Relation = ['<', '>', '<=', '>=', '=']
def GetEquationAndSymbol(Equation_to_Solve):
    Equation = Equation_to_Solve[0]
    Symbol = []
    symbol_appear = 0
    have_rational = False
    is_system = False
    if any(relation in str(Equation) for relation in Relation):
        # print("is system")
        have_rational = True
        is_system = True
    if all(relation not in Equation_to_Solve for relation in Relation):
        # print("Relation not in Equation_to_Solve")
        for nums,expr in enumerate(Equation_to_Solve[1:]):
            
            if len(str(expr)) == 1:
                if str(expr).isdigit():
                    Equation = Eq(Equation, expr)
                else:
                    if isinstance(expr, sympy.Symbol):
                        if expr in Symbol:
                            Equation = Eq(Equation, expr)
                            symbol_appear +=1
                        else:
                            Symbol.append(expr)
                            symbol_appear = nums
            else:
                Equation = Eq(Equation, expr)
    else:
        # print("Relation in Equation_to_Solve")
        have_rational = True
        Equation = ' '.join([str(elem) for elem in Equation_to_Solve[:-1]]) 
        # if something false check this
        Symbol = Equation_to_Solve[-1]
    if is_system:
        return Equation_to_Solve[:(symbol_appear+1)],Symbol, have_rational, is_system
    return Equation, Symbol, have_rational, is_system

def Solve(Equation_to_Solve):
    Equation, Symbol, have_rational, is_system = GetEquationAndSymbol(Equation_to_Solve)
    if isinstance(Equation, sympy.Eq) and len(Symbol) > 1:
        Equation = Equation.args
    if (Equation == '' or Equation == [] or Equation == None or Equation == False):
        return "No result found"
    # print("Before Solve")
    # print("Equation", Equation)
    # print("Symbol", Symbol)
    if have_rational:
        if is_system:
            return solve(Equation, Symbol, domain=S.Reals,relational=True)
        return solve(Equation, Symbol, domain=S.Reals,relational=True)
    # print("use solve")
    return solve(Equation, Symbol)