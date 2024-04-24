import unittest

from sympy import simplify, igcd, solveset, S,symbols,solve
from solve_main import extract_equation
x = symbols('x')

class TestSolver(unittest.TestCase):

    def test_linear(self):
        equation = "[[2*x + 1, 7/4, x, solve]]"
        expected = solve(2*x + 1 - 7/4, x)
        self.assertEqual(expected, extract_equation(equation))

    def test_inequality(self):
        equation = "[[x**3 - x, <=, 3*x**2 - 3, x, solve]]"
        expected = solveset(x**3 - x <= 3*x**2 - 3,x, domain=S.Reals)
        self.assertEqual(expected, extract_equation(equation))

    def test_igcd(self):
        equation = "[[2, 20, 5, igcd]]"
        expected = igcd(2,20, 5)
        self.assertEqual(expected, extract_equation(equation))

    def test_inequality_2(self):
        equation = "[[(3*x + 1)/2 - (x - 2)/3, <, (1 - 2*x)/4, x, solve]]"
        expected = solveset((3*x + 1)/2 - (x - 2)/3 <(1 - 2*x)/4,x, domain=S.Reals)
        self.assertEqual(expected, extract_equation(equation))

    def test_inequalitySystem(self):
        equation = "[[6*x + 5/7 < 4*x + 7, (8*x + 3)/2 < 2*x + 5, x, solve]]"
        # Here you would calculate the expected result manually or with a known good method
        list_of_equations = ['6*x + 5/7 < 4*x + 7', '(8*x + 3)/2 < 2*x + 5']
        expected = solve(list_of_equations, x)
        self.assertEqual(expected, extract_equation(equation))

    # def test_equation6(self):
    #     equation = "[[cos(10*x) + 2*cos(4*x)**2 + 6*cos(3*x)*cos(x) - cos(x) - 8*cos(x)*cos(3*x)**3, x, simplify]]"
    #     expected = simplify("cos(10*x) + 2*cos(4*x)**2 + 6*cos(3*x)*cos(x) - cos(x) - 8*cos(x)*cos(3*x)**3")
    #     self.assertEqual(expected, extract_equation(equation))

# Add more tests as needed for other equations

if __name__ == '__main__':
    unittest.main()