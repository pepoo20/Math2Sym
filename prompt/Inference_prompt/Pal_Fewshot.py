Inequalities_Num = """Following the previous example solving Problem/Question by using python, Solve the last problem/question using similar approach.Question: Inequality: 9*x + 16 <= 3*x  -20

# solution in Python:

def solution():
    # Inequality: 9*x + 16 <= 3*x  -20
    from sympy import symbols, solve
    x = symbols('x')
    solution = solve(9*x + 16 <= 3*x  -20, x)
    return solution

Question:Inequality: -32*x  -18 < -37*x  -3

# solution in Python:

def solution():
    # Inequality: -32*x  -18 < -37*x  -3
    from sympy import symbols, solve
    x = symbols('x')
    solution = solve(-32*x  -18 < -37*x  -3, x)
    return solution

Question:Solve the inequality: -7*y  -32 <= -6*y 

# solution in Python:

def solution():
    # Solve the inequality: -7*y  -32 <= -6*y 
    from sympy import symbols, solve
    y = symbols('y')
    solution = solve(-7*y  -32 <= -6*y, y)
    return solution

Question:Inequality: 17*x  -41 > -41

# solution in Python:

def solution():
    # Inequality: 17*x  -41 > -41
    from sympy import symbols, solve
    x = symbols('x')
    solution = solve(17*x  -41 > -41, x)
    return solution

Question:Solve the inequality: -16*z + 6 > -14*z + 32 

# solution in Python:

def solution():
    # Solve the inequality: -16*z + 6 > -14*z + 32
    from sympy import symbols, solve
    z = symbols('z')
    solution = solve(-16*z + 6 > -14*z + 32, z)
    return solution
"""

Inequalites_Word = """
Following the previous example solving Problem/Question by using python, Solve the last problem/question using similar approach.Word Problem:Brice has $30 to take his brother and his friends to the movies. If each ticket costs $4.00, and he must buy tickets for himself and his brother, what is the greatest number of friends he can invite?

# solution in Python:

def solution():
    # Brice has $30 to take his brother and his friends to the movies. If each ticket costs $4.00, and he must buy tickets for himself and his brother, what is the greatest number of friends he can invite?
    from sympy import symbols, solve
    x = symbols('x')
    solution = solve(4*x+4*2 <= 30, x)
    return solution

Word Problem: What numbers satisfy the condition: nine less than negative four times a number is strictly greater than negative one?

# solution in Python:

def solution():
    # What numbers satisfy the condition: nine less than negative four times a number is strictly greater than negative one?
    from sympy import symbols, solve
    x = symbols('x')
    solution = solve(-4*x - 9 > -1, x)
    return solution

Word Problem:The elevator in Yehires apartment building has a sign that says the maximum weight is 2,100 pounds. If the average weight of one person is 150 pounds, how many people can safely ride the elevator?

# solution in Python:

def solution():
    # The elevator in Yehires apartment building has a sign that says the maximum weight is 2,100 pounds. If the average weight of one person is 150 pounds, how many people can safely ride the elevator?
    from sympy import symbols, solve
    x = symbols('x')
    solution = solve(150*x <= 2100, x)
    return solution

Word Problem: Brenda has $500 in her bank account.  Every week, she withdraws $40 for expenses.  Without making any deposits, how many weeks can she withdraw this money if she wants to maintain a balance of at least $200? 

# solution in Python:

def solution():
    # Brenda has $500 in her bank account.  Every week, she withdraws $40 for expenses.  Without making any deposits, how many weeks can she withdraw this money if she wants to maintain a balance of at least $200?
    from sympy import symbols, solve
    x = symbols('x')
    solution = solve(500 - 40*x >= 200, x)
    return solution

Word Problem: Five student government officers want to go to the state convention. It will cost them $110 for registration, $375 for transportation and food, and $42 per person for the hotel. There is $450 budgeted for the convention in the student government savings account. They can earn the rest of the money they need by having a car wash. If they charge $5 per car, how many cars must they wash in order to have enough money to pay for the trip?

# solution in Python:

def solution():
    # Five student government officers want to go to the state convention. It will cost them $110 for registration, $375 for transportation and food, and $42 per person for the hotel. There is $450 budgeted for the convention in the student government savings account. They can earn the rest of the money they need by having a car wash. If they charge $5 per car, how many cars must they wash in order to have enough money to pay for the trip?
    from sympy import symbols, solve
    x = symbols('x')
    solution = solve(110 + 375 + 42*5 <= 450 + 5*x, x)
    return solution
"""

GCD_Num = """Following the previous example solving Problem/Question by using python, Solve the last problem/question using similar approach.Question:Calculate the greatest common divisor of 18, 27.

# solution in Python:

def solution():
    # Calculate the greatest common divisor of 18, 27.
    from sympy import igcd
    solution = igcd(18, 27)
    return solution

Question:Calculate the greatest common divisor of 466, 708, 30.

# solution in Python:

def solution():
    # Calculate the greatest common divisor of 466, 708, 30.
    from sympy import igcd
    solution = igcd(466, 708, 30)
    return solution

Question:Calculate the greatest common divisor of 43, 56, 33.

# solution in Python:

def solution():
    # Calculate the greatest common divisor of 43, 56, 33.
    from sympy import igcd
    solution = igcd(43, 56, 33)
    return solution

Question: Find the greatest common divisor of 15, 30, 45.

# solution in Python:

def solution():
    # Find the greatest common divisor of 15, 30, 45.
    from sympy import igcd
    solution = igcd(15, 30, 45)
    return solution

Question: Find the greatest common divisor of 12, 18, 24.

# solution in Python:

def solution():
    # Find the greatest common divisor of 12, 18, 24.
    from sympy import igcd
    solution = igcd(12, 18, 24)
    return solution"""

GCD_Word = """
Following the previous example solving Problem/Question by using python, Solve the last problem/question using similar approach.Word Problem:Find the greatest possible length that can be used to measure exactly the lengths 84 feet, 98 feet and 126 feet.

# solution in Python:

def solution():
    # Find the greatest possible length that can be used to measure exactly the lengths 84 feet, 98 feet and 126 feet.
    from sympy import igcd
    solution = igcd(84, 98, 126)
    return solution


Word Problem: A warehouse has three shelves that can hold 8, 12, or 16 skateboards. Each shelf has sections holding the same number of skateboards. What is the greatest number of skateboards that can be put in a section?

# solution in Python:

def solution():
    # A warehouse has three shelves that can hold 8, 12, or 16 skateboards. Each shelf has sections holding the same number of skateboards. What is the greatest number of skateboards that can be put in a section?
    from sympy import igcd
    solution = igcd(8, 12, 16)
    return solution

Word Problem: Kiara baked 30 oatmeal cookies and 48 chocolate chip cookies to package in plastic containers for her friends at school. She wants to divide the cookies into identical containers so that each container has the same number of each kind of cookie. If she wants each container to have the greatest number of cookies possible, how many plastic containers does she need?

# solution in Python:

def solution():
    # Kiara baked 30 oatmeal cookies and 48 chocolate chip cookies to package in plastic containers for her friends at school. She wants to divide the cookies into identical containers so that each container has the same number of each kind of cookie. If she wants each container to have the greatest number of cookies possible, how many plastic containers does she need?
    from sympy import igcd
    solution = igcd(30, 48)
    return solution

Word Problem: A motorcycle dealership has 30 Yamaha R1s and 42 Honda CBRs in their inventory. The dealership wants to arrange the motorcycles in rows so that each row contains the same number of motorcycles and an equal number of each motorcycle type. What is the greatest number of rows that can be formed under these conditions?

# solution in Python:

def solution():
    # A motorcycle dealership has 30 Yamaha R1s and 42 Honda CBRs in their inventory. The dealership wants to arrange the motorcycles in rows so that each row contains the same number of motorcycles and an equal number of each motorcycle type. What is the greatest number of rows that can be formed under these conditions?
    from sympy import igcd
    solution = igcd(30, 42)
    return solution


Word Problem: Sara has 16 red flowers and 24 yellow flowers. She wants to make bouquets with the same number of each color flower in each bouquet. What is the greatest number of bouquets she can make?

# solution in Python:

def solution():
    # Sara has 16 red flowers and 24 yellow flowers. She wants to make bouquets with the same number of each color flower in each bouquet. What is the greatest number of bouquets she can make?
    from sympy import igcd
    solution = igcd(16, 24)
    return solution
"""

LCM_Num = """Following the previous example solving Problem/Question by using python, Solve the last problem/question using similar approach.Question:What is the smallest common multiple of 43, 56, 33?

# solution in Python:

def solution():
    # What is the smallest common multiple of 43, 56, 33?
    from sympy import ilcm
    solution = ilcm(43, 56, 33)
    return solution

Question:What is the smallest common multiple of 18, 27?

# solution in Python:

def solution():
    # What is the smallest common multiple of 18, 27?
    from sympy import ilcm
    solution = ilcm(18, 27)
    return solution

Question:What is the smallest common multiple of 466, 708, 30?

# solution in Python:

def solution():
    # What is the smallest common multiple of 466, 708, 30?
    from sympy import ilcm
    solution = ilcm(466, 708, 30)
    return solution

Question:What is the smallest common multiple of 43, 56, 33?

# solution in Python:

def solution():
    # What is the smallest common multiple of 43, 56, 33?
    from sympy import ilcm
    solution = ilcm(43, 56, 33)
    return solution

Question:What is the smallest common multiple of 18, 27?

# solution in Python:

def solution():
    # What is the smallest common multiple of 18, 27?
    from sympy import ilcm
    solution = ilcm(18, 27)
    return solution

Question:What is the smallest common multiple of 466, 708, 30?

# solution in Python:

def solution():
    # What is the smallest common multiple of 466, 708, 30?
    from sympy import ilcm
    solution = ilcm(466, 708, 30)
    return solution
"""

LCM_Word = """
Following the previous example solving Problem/Question by using python, Solve the last problem/question using similar approach.Word Problem: Six bells commence tolling together and toll at intervals of 2, 4, 6, 8 10 and 12 seconds respectively. In 30 minutes, how many times do they toll together ? (excluding the one at start)

# solution in Python:

def solution():
    # Six bells commence tolling together and toll at intervals of 2, 4, 6, 8 10 and 12 seconds respectively. In 30 minutes, how many times do they toll together ? (excluding the one at start)
    from sympy import ilcm
    solution = ilcm(2, 4, 6, 8, 10, 12)
    return solution

Word Problem: A farmer has 10 cows, 15 sheep, and 20 chickens. He wants to put the animals into pens so that each pen has the same number of each kind of animal. What is the least number of animals that can be in each pen?

# solution in Python:

def solution():
    # A farmer has 10 cows, 15 sheep, and 20 chickens. He wants to put the animals into pens so that each pen has the same number of each kind of animal. What is the least number of animals that can be in each pen?
    from sympy import ilcm
    solution = ilcm(10, 15, 20)
    return solution

Word Problem: A train to Los Angeles leaves a station every 10 minutes. Another train to San Francisco leaves the same station every 8 minutes. If it is 9:00 am right now, at what time will both trains leave the station together?

# solution in Python:

def solution():
    # A train to Los Angeles leaves a station every 10 minutes. Another train to San Francisco leaves the same station every 8 minutes. If it is 9:00 am right now, at what time will both trains leave the station together?
    from sympy import ilcm
    solution = ilcm(10, 8)
    return solution


Word Problem: At a summer camp, the arts and crafts instructor wants to organize a schedule for the pottery and woodworking classes. The pottery class meets every 6 days, and the woodworking class meets every 8 days. If both classes were last held on the same day, after how many days will they next meet on the same day?

# solution in Python:

def solution():
    # At a summer camp, the arts and crafts instructor wants to organize a schedule for the pottery and woodworking classes. The pottery class meets every 6 days, and the woodworking class meets every 8 days. If both classes were last held on the same day, after how many days will they next meet on the same day?
    from sympy import ilcm
    solution = ilcm(6, 8)
    return solution


Word Problem:A bakery makes blueberry muffins every 3 days, and another bakery makes blueberry muffins every 4 days. If both bakeries started making blueberry muffins on the same day, how many times in 24 days will they both make blueberry muffins on the same day?

# solution in Python:

def solution():
    # A bakery makes blueberry muffins every 3 days, and another bakery makes blueberry muffins every 4 days. If both bakeries started making blueberry muffins on the same day, how many times in 24 days will they both make blueberry muffins on the same day?
    from sympy import ilcm
    solution = ilcm(3, 4)
    return solution

Word Problem:Today, both the soccer team and the basketball team had games. The soccer team plays every three days, and the basketball team plays every five days. When will both teams have games on the same day again?

# solution in Python:

def solution():
    # Today, both the soccer team and the basketball team had games. The soccer team plays every three days, and the basketball team plays every five days. When will both teams have games on the same day again?
    from sympy import ilcm
    solution = ilcm(3, 5)
    return solution
"""

SystemLinear_Num = """
Following the previous example solving Problem/Question by using python, Solve the last problem/question using similar approach.Question: Solve the given system of equations by addition: 3*x + 4*y = 5,2*x - 3*y = 7

# solution in Python:

def solution():
    # Solve the given system of equations by addition: 3*x + 4*y = 5,2*x - 3*y = 7
    from sympy import symbols, Eq, solve
    x, y = symbols('x y')
    eq1 = Eq(3*x + 4*y, 5)
    eq2 = Eq(2*x - 3*y, 7)
    solution = solve((eq1, eq2), (x, y))
    return solution

Question: Solve the given system of equations by addition:12*x + 13*y = 4,-y = -3  

# solution in Python:

def solution():
    # Solve the given system of equations by addition:12*x + 13*y = 4,-y = -3
    from sympy import symbols, Eq, solve
    x, y = symbols('x y')
    eq1 = Eq(12*x + 13*y, 4)
    eq2 = Eq(-y, -3)
    solution = solve((eq1, eq2), (x, y))
    return solution

Question: Solve the given system of equations by elimination 
-3*y = 66
-75*x -52*y = 77 

# solution in Python:

def solution():
    # Solve the given system of equations by elimination -3*y = 66,-75*x -52*y = 77
    from sympy import symbols, Eq, solve
    x, y = symbols('x y')
    eq1 = Eq(-3*y, 66)
    eq2 = Eq(-75*x -52*y, 77)
    solution = solve((eq1, eq2), (x, y))
    return solution

Question: Solve the given system of equations by substitution: 4*y = -12,-13*x  = 4 

# solution in Python:

def solution():
    # Solve the given system of equations by substitution: 4*y = -12,-13*x  = 4
    from sympy import symbols, Eq, solve
    x, y = symbols('x y')
    eq1 = Eq(4*y, -12)
    eq2 = Eq(-13*x, 4)
    solution = solve((eq1, eq2), (x, y))
    return solution


Question: Solve the given system of equations by addition: 
9*y = -3
-5*x + 6*y = 13  

# solution in Python:

def solution():
    # Solve the given system of equations by addition: 9*y = -3,-5*x + 6*y = 13
    from sympy import symbols, Eq, solve
    x, y = symbols('x y')
    eq1 = Eq(9*y, -3)
    eq2 = Eq(-5*x + 6*y, 13)
    solution = solve((eq1, eq2), (x, y))
    return solution

Question: Solve the given system of equations :-8*x -17*y = 0,-4*x -8*y = 8  

# solution in Python:

def solution():
    # Solve the given system of equations :-8*x -17*y = 0,-4*x -8*y = 8
    from sympy import symbols, Eq, solve
    x, y = symbols('x y')
    eq1 = Eq(-8*x -17*y, 0)
    eq2 = Eq(-4*x -8*y, 8)
    solution = solve((eq1, eq2), (x, y))
    return solution
"""

SystemLinear_Word = """
Following the previous example solving Problem/Question by using python, Solve the last problem/question using similar approach.Word Problem: The Rocket Coaster has 15 cars, some that hold 4 people and some that hold 6 people. There is room for 72 people. How many 4-person cars and how many 6-person cars are there?

# solution in Python:

def solution():
    # The Rocket Coaster has 15 cars, some that hold 4 people and some that hold 6 people. There is room for 72 people. How many 4-person cars and how many 6-person cars are there?
    from sympy import symbols, Eq, solve
    x, y = symbols('x y')
    eq1 = Eq(x + y, 15)
    eq2 = Eq(4*x + 6*y, 72)
    solution = solve((eq1, eq2), (x, y))
    return solution

Word Problem:The price, e, of an entertainment system at Extreme Electronics is $220 less than twice the price, u, of the same system at Ultra Electronics. The difference in price between the system at Extreme Electronics and Ultra Electronics is $175. What is the price of the system at each store?

# solution in Python:

def solution():
    # The price, e, of an entertainment system at Extreme Electronics is $220 less than twice the price, u, of the same system at Ultra Electronics. The difference in price between the system at Extreme Electronics and Ultra Electronics is $175. What is the price of the system at each store?
    from sympy import symbols, Eq, solve
    x, y = symbols('x y')
    eq1 = Eq(x - 2*y, -220)
    eq2 = Eq(x - y, 175)
    solution = solve((eq1, eq2), (x, y))
    return solution

Word Problem:A business has two loans totaling $85,000. One loan has a rate of 6% and the other has a rate of 4.5% This year, the business expects to pay $4,650 in interest on the two loans. How much is each loan?

# solution in Python:

def solution():
    # A business has two loans totaling $85,000. One loan has a rate of 6% and the other has a rate of 4.5% This year, the business expects to pay $4,650 in interest on the two loans. How much is each loan?
    from sympy import symbols, Eq, solve
    x, y = symbols('x y')
    eq1 = Eq(x + y, 85000)
    eq2 = Eq(0.06*x + 0.045*y, 4650)
    solution = solve((eq1, eq2), (x, y))
    return solution

Word Problem: A farmer raises both chickens and pigs on his farm. He counts a total of 30 heads and 90 legs among the animals in his barn. Assuming that each chicken has one head and two legs, while each pig has one head and four legs, how many chickens and how many pigs does the farmer have?

# solution in Python:

def solution():
    # A farmer raises both chickens and pigs on his farm. He counts a total of 30 heads and 90 legs among the animals in his barn. Assuming that each chicken has one head and two legs, while each pig has one head and four legs, how many chickens and how many pigs does the farmer have?
    from sympy import symbols, Eq, solve
    x, y = symbols('x y')
    eq1 = Eq(x + y, 30)
    eq2 = Eq(2*x + 4*y, 90)
    solution = solve((eq1, eq2), (x, y))
    return solution

Word Problem: The length of a rectangle is equal to triple the width. Which system of equations can be used to find the dimensions of the rectangle if the perimeter is 86 centimeters?

# solution in Python:

def solution():
    # The length of a rectangle is equal to triple the width. Which system of equations can be used to find the dimensions of the rectangle if the perimeter is 86 centimeters?
    from sympy import symbols, Eq, solve
    x, y = symbols('x y')
    eq1 = Eq(2*x + 2*y, 86)
    eq2 = Eq(3*x, y)
    solution = solve((eq1, eq2), (x, y))
    return solution
"""


CompoundInequalities_Num = """
Following the previous example solving Problem/Question by using python, Solve the last problem/question using similar approach.Question:Solve this compound inequalities:  4*y -17 < 19 and -39*y  <= -47 

# solution in Python:

def solution():
    # Solve this compound inequalities: 4*y -17 < 19 and -39*y  <= -47
    from sympy import symbols, solve
    y = symbols('y')
    solution = solve(4*y -17 < 19, -39*y  <= -47, y)
    return solution    

Question: Solve this compound inequalities:  -18 < 6*z + 18 < 17 

# solution in Python:

def solution():
    # Solve this compound inequalities: -18 < 6*z + 18 < 17
    from sympy import symbols, solve
    z = symbols('z')
    solution = solve(-18 < 6*z + 18 < 17, z)
    return solution

Question: Solve this compound inequalities: 12*y -3 > 9 and 4*y  < 7 

# solution in Python:

def solution():
    # Solve this compound inequalities: 12*y -3 > 9 and 4*y  < 7
    from sympy import symbols, solve
    y = symbols('y')
    solution = solve(12*y -3 > 9, 4*y  < 7, y)
    return solution

Question: Solve this compound inequalities: 3 < x -72 < 7 

# solution in Python:

def solution():
    # Solve this compound inequalities: 3 < x -72 < 7
    from sympy import symbols, solve
    x = symbols('x')
    solution = solve(3 < x -72 < 7, x)
    return solution

Question:Solve this compound inequalities:  -43 <= -5*z + 457 <= 33 

# solution in Python:

def solution():
    # Solve this compound inequalities: -43 <= -5*z + 457 <= 33
    from sympy import symbols, solve
    z = symbols('z')
    solution = solve(-43 <= -5*z + 457 <= 33, z)
    return solution
"""

CompoundInequalities_Word = """
Following the previous example solving Problem/Question by using python, Solve the last problem/question using similar approach.Word Problem: A number is at least 5 and at most 15. Write a compound inequality that shows the range of numbers that satisfy this condition.

# solution in Python:

def solution():
    # A number is at least 5 and at most 15. Write a compound inequality that shows the range of numbers that satisfy this condition.
    from sympy import symbols, solve,S
    x = symbols('x')
    Eq1 = x >= 5
    Eq2 = x <= 15
    solution = solve((Eq1, Eq2), x, domain=S.Reals)
    return solution

Word Problem: Mia is a baker who wants to make a profit of at least $200 but no more than $300 on a large order of cupcakes for a wedding. She has already spent $150 on ingredients and the decorations. Each cupcake she sells will bring in a profit of $2. How many cupcakes does Mia need to sell to make her desired profit?

# solution in Python:

def solution():
    # Mia is a baker who wants to make a profit of at least $200 but no more than $300 on a large order of cupcakes for a wedding. She has already spent $150 on ingredients and the decorations. Each cupcake she sells will bring in a profit of $2. How many cupcakes does Mia need to sell to make her desired profit?
    from sympy import symbols, solve,S
    x = symbols('x')
    Eq1 = 2*x + 150 >= 200
    Eq2 = 2*x + 150 <= 300
    solution = solve((Eq1, Eq2), x, domain=S.Reals)
    return solution

Word Problem: A ski shop carries skis that are between 150 and 220cm long. They recommend that the skis be 1.25 longer than your height.Calculate the tallest height that a person can be and still rent skis from the shop.

# solution in Python:

def solution():
    # A ski shop carries skis that are between 150 and 220cm long. They recommend that the skis be 1.25 longer than your height.Calculate the tallest height that a person can be and still rent skis from the shop.
    from sympy import symbols, solve,S 
    x = symbols('x')
    Eq1 = 1.25*x <= 220
    Eq2 = 1.25*x >= 150
    solution = solve((Eq1, Eq2), x, domain=S.Reals)
    return solution

Word Problem: An electronics store is giving a $50 discount coupon for all smart watches. Emma is considering various smart watches with prices ranging from $220 to $310. How much can she anticipate to pay after applying the discount coupon?

# solution in Python:

def solution():
    # An electronics store is giving a $50 discount coupon for all smart watches. Emma is considering various smart watches with prices ranging from $220 to $310. How much can she anticipate to pay after applying the discount coupon?
    from sympy import symbols, solve,S
    x = symbols('x')
    Eq1 = x - 50 >= 220
    Eq2 = x - 50 <= 310
    solution = solve((Eq1, Eq2), x, domain=S.Reals)
    return solution

Word Problem:A local energy company has introduced a new billing system to encourage energy conservation. The system has three tiers: Eco-Friendly Usage, Standard Usage, and High Usage. The usage is measured in kilowatt-hours (kWh). During the summer months, a customer will pay a base fee of $15.50 plus $0.12 per kWh for Eco-Friendly Usage. The bill for Eco-Friendly Usage would be between or equal to $21.50 and $39.50. How many kWh can the customer use if they want their usage to stay in the Eco-Friendly range?

# solution in Python:

def solution():
    # A local energy company has introduced a new billing system to encourage energy conservation. The system has three tiers: Eco-Friendly Usage, Standard Usage, and High Usage. The usage is measured in kilowatt-hours (kWh). During the summer months, a customer will pay a base fee of $15.50 plus $0.12 per kWh for Eco-Friendly Usage. The bill for Eco-Friendly Usage would be between or equal to $21.50 and $39.50. How many kWh can the customer use if they want their usage to stay in the Eco-Friendly range?
    from sympy import symbols, solve,S
    x = symbols('x')
    Eq1 = 0.12*x + 15.50 >= 21.50
    Eq2 = 0.12*x + 15.50 <= 39.50
    solution = solve((Eq1, Eq2), x, domain=S.Reals)
    return solution
"""