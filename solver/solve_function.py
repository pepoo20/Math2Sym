
from sympy import symbols, solveset, S, Eq, solve, solve_univariate_inequality
import sympy
Relation = ['<', '>', '<=', '>=', '=']
def GetEquationAndSymbol(Equation_to_Solve):
    Equation = Equation_to_Solve[0]
    Symbol = []
    symbol_appear = 0
    have_rational = False
    if any(relation in str(Equation) for relation in Relation):
        have_rational = True
    if all(relation not in Equation_to_Solve for relation in Relation):
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
        have_rational = True
        Equation = ' '.join([str(elem) for elem in Equation_to_Solve[:-1]]) 
        Symbol = Equation_to_Solve[-1]
    return Equation, Symbol, have_rational

def SystemLinearMoreThanTwoEquations(Equation_to_Solve):
    equation_list = []
    symbol_list = []
    for nums,expr in enumerate(Equation_to_Solve):
        if isinstance(expr, sympy.Symbol):
            if expr in symbol_list:
                equation_list.append(expr)
                symbol_appear +=1
            else:
                symbol_list.append(expr)
                symbol_appear = nums
        else:
            equation_list.append(expr)
    return solve(equation_list, symbol_list)

def SolveLeastThan2SymbolEquations(Equation_to_Solve):
    Equation, Symbol, have_rational = GetEquationAndSymbol(Equation_to_Solve)
    if isinstance(Equation, sympy.Eq):
        Equation = Equation.args
    if (Equation == '' or Equation == [] or Equation == None or Equation == False):
        return "No result found"
    if have_rational:
        return solve(Equation, Symbol, domain=S.Reals,relational=True)
    
    return solve(Equation, Symbol)
def Count_comma(Equation_to_Solve):
    count = 0
    for i in str(Equation_to_Solve):
        if str(i) == ',':
            count += 1
    return count
def Solve(Equation_to_Solve):
    Commas = Count_comma(Equation_to_Solve)
    if Commas >=4 :
        return SystemLinearMoreThanTwoEquations(Equation_to_Solve)
    else:
        return SolveLeastThan2SymbolEquations(Equation_to_Solve)