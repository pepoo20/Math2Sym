Direct_Cot = """Please act as a professional math teacher.Your goal is to accurately solve a math word problem.
To achieve the goal, you have two jobs.

# Write detailed solution to a Given Question. 
# Write the final answer to this question. 

# Ensure the solution is step-by-step. 
Given Question: given question 
Your output should be in the following format: 

SOLUTION: <your detailed solution to the given question> 
FINAL ANSWER: <your final answer> 
"""

Inequalities_Num_Symbolic = """Task: Do not solve problem. Symbolic Form has the structure of [[expression, inequality symbols, expression, variable, solve]] . Convert the Last Question into Symbolic Form same like given example.Given example:
Question: Inequality: 9*x + 16 <= 3*x  -20
Symbolic Form: [[9*x + 16, <= , 3*x  -20 , x , solve]]

Question:Inequality: -32*x  -18 < -37*x  -3
Symbolic Form: [[-32*x  -18, < , -37*x  -3 , x , solve]]

Question:Solve the inequality: -7*y  -32 <= -6*y 
Symbolic Form : [[-7*y -32, <= , -6*y  , y, solve]]

Question:Inequality: 17*x  -41 > -41
Symbolic Form: [[17*x  -41, > , 0*x  -41 , x , solve]]

Question:Solve the inequality: -16*z + 6 > -14*z + 32 
Symbolic Form : [[-16*z +6, > , -14*z + 32, z, solve]]
"""

Inequalites_Word_Symbolic = """
Task: Do not solve the problem. The Symbolic Form has the structure of [[expression, inequality symbols, expression, variable, solve]]. Your task is to formulate the word problem as an inequality and then convert it into Symbolic Form, similar to the given example.Given example:
Word Problem: What numbers satisfy the condition: eight time a number plus negative two is greater than fifteen?

Break down the word problem into smaller information:
1. Our goal is to find the numbers that satisfy the condition.
2. Eight times a number plus negative two is greater than fifteen.
Define the variables and formulate the inequality:
Let x be the number.
Eight times a number plus negative two is greater than fifteen can be written as 8*x - 2 > 15
Inequality: 8*x - 2 > 15
Symbolic Form: [[8*x - 2, >, 15, x, solve]]

Word Problem:Brice has $30 to take his brother and his friends to the movies. If each ticket costs $4.00, and he must buy tickets for himself and his brother, what is the greatest number of friends he can invite?

Break down the word problem into smaller information:
1. Our goal is to find the greatest number of friends Brice can invite.
2. Brice has $30 to take his brother and his friends to the movies.
3. Each ticket costs $4.00.
4. He must buy tickets for himself and his brother.
Define the variables and formulate the inequality:
Let x be the number of friends Brice can invite.
Total cost = Cost of tickets for Brice and his brother + Cost of tickets for his friends
Each ticket costs $4 so the cost of tickets for Brice and his brother is 2*4
Cost of tickets for his friends is x*4
Total cost = 2*4 + x*4
Brice has $30 so we accept at 30 and less so the is '=' sign in the inequality then 2*4 + x*4 <= 30
Inequality: 2*4 + x*4 <= 30
Symbolic Form: [[2*4 + x*4, <=, 30, x, solve]]

Word Problem:A group of friends wants to go on a camping trip. The campsite charges a flat fee of $75 for the group, plus $12 per person for the duration of their stay. Additionally, they estimate that they will need $180 for food and supplies. The friends have already saved $200 for the trip, and they plan to raise the rest of the money by having a bake sale. If they sell each baked item for $3, how many items must they sell to have enough money for the camping trip?

Break down the word problem into smaller information:
1. Our goal is to find the number of items they must sell to have enough money for the camping trip.
2. The campsite charges a flat fee of $75 for the group, plus $12 per person for the duration of their stay.
3. They estimate that they will need $180 for food and supplies.
4. The friends have already saved $200 for the trip.
5. They plan to raise the rest of the money by having a bake sale.
6. They sell each baked item for $3.
Define the variables and formulate the inequality:
Let x be the number of items they must sell.
Total cost = Cost of campsite + Cost of food and supplies + Earnings from bake sale
The campsite charges a flat fee of $75 for the group, plus $12 per person for the duration of their stay so the cost of the campsite is 75 + 12*x
They estimate that they will need $180 for food and supplies so the cost of food and supplies is 180
The friends have already saved $200 for the trip so the total amount they have saved is 200
They plan to raise the rest of the money by having a bake sale so the earnings from the bake sale is x*3
The total cost should be less than or equal to the total amount they have saved so the total cost <= 200
Inequality: 75 + 12*x + 180 + x*3 <= 200
Symbolic Form: [[75 + 12*x + 180 + x*3, <=, 200, x, solve]]

Word Problem: A car rental company charges $25 per day to rent a car. If a customer has $200 to spend on a rental, how many days can the customer rent the car?

Break down the word problem into smaller information:
1. Our goal is to find the number of days the customer can rent the car.
2. The car rental company charges $25 per day to rent a car.
3. The customer has $200 to spend on a rental.
Define the variables and formulate the inequality:
Let x be the number of days the customer can rent the car.
Total cost = Cost per day * Number of days
The car rental company charges $25 per day so the cost per day is 25
The customer has $200 to spend on a rental so the total amount the customer has is 200
The total cost should be less than or equal to the total amount the customer has so the total cost <= 200
Inequality: 25*x <= 200
Symbolic Form: [[25*x, <=, 200, x, solve]]

Word Problem: A small tourist boat has a maximum capacity of 1,500 pounds, according to the boat's safety guidelines. If the average weight of one passenger, including their luggage, is 200 pounds, how many passengers can safely board the boat?

Break down the word problem into smaller information:
1. Our goal is to find the number of passengers that can safely board the boat.
2. The small tourist boat has a maximum capacity of 1,500 pounds.
3. The average weight of one passenger, including their luggage, is 200 pounds.
Define the variables and formulate the inequality:
Let x be the number of passengers that can safely board the boat.
Total weight = Weight per passenger * Number of passengers
The average weight of one passenger, including their luggage, is 200 pounds so the weight per passenger is 200
The small tourist boat has a maximum capacity of 1,500 pounds so the total weight should be less than or equal to 1,500
Inequality: 200*x <= 1500
Symbolic Form: [[200*x, <=, 1500, x, solve]]


"""

GCD_Num_Symbolic = """Task: Do not solve the problem directly.Your answer must be the Symbolic Form not a number.Symbolic Form has the structure of [[expression, expression, expression, igcd]]. Convert the Question into Symbolic Form same like given example.Given example:
Question:Calculate the greatest common divisor of 18, 27.
Symbolic Form: [[18, 27, igcd]]
Question:Calculate the greatest common divisor of 466, 708, 30.
Symbolic Form: [[466, 708, 30, igcd]].
Question:Calculate the greatest common divisor of 43, 56, 33.
Symbolic Form: [[43, 56, 33, igcd]].
Question: Find the greatest common divisor of 15, 30, 45.
Symbolic Form: [[15, 30, 45, igcd]].
Question: Find the greatest common divisor of 12, 18, 24.
Symbolic Form: [[12, 18, 24, igcd]]
"""

GCD_Word_Symbolic = """
Task: Do not solve problem. Convert the Last Word Problem into Symbolic Form same like given example.Given example:
Word Problem:Find the greatest possible length that can be used to measure exactly the lengths 84 feet, 98 feet and 126 feet.
Find the greatest common factor of 84, 98 and 126.
Symbolic Form: [[84, 98, 126, igcd]]

Word Problem: A warehouse has three shelves that can hold 8, 12, or 16 skateboards. Each shelf has sections holding the same number of skateboards. What is the greatest number of skateboards that can be put in a section?
Find the greatest common factor of 8, 12 and 16.
Symbolic Form: [[8, 12, 16, igcd]]

Word Problem: A summer camp has 24 boys and 36 girls enrolled. The camp organizers want to divide the campers into groups for various activities, with each group having an equal number of campers and an equal number of boys and girls. What is the greatest number of groups the organizers can form while satisfying these conditions?
Find the greatest common factor of 24 and 36.
Symbolic Form: [[24, 36, igcd]]

Word Problem: A motorcycle dealership has 30 Yamaha R1s and 42 Honda CBRs in their inventory. The dealership wants to arrange the motorcycles in rows so that each row contains the same number of motorcycles and an equal number of each motorcycle type. What is the greatest number of rows that can be formed under these conditions?
Find the greatest common factor of 30 and 42.
Symbolic Form: [[30, 42, igcd]]
"""

LCM_Num_Symbolic = """
Task: Do not solve problem. Symbolic Form has the structure of [[expression, expression, expression, ilcm]] . Convert the problem into Symbolic Form same like given example.Given example:
Question:What is the smallest common multiple of 43, 56, 33?
Symbolic Form: [[43, 56, 33, ilcm]]

Question:What is the smallest common multiple of 18, 27?
Symbolic Form: [[18, 27, ilcm]]

Question:What is the smallest common multiple of 466, 708, 30?
Symbolic Form: [[466, 708, 30, ilcm]]
"""

LCM_Word_Symbolic = """
Task: Do not solve problem . Convert the Last Word Problem into Symbolic Form same like given example.Given example:Word Problem: Omar is planting trees. He has enough trees to plant 6, 7, or 14 trees in each row. What is the least number of trees Omar could have ?
Find the least common multiple of 6, 7 and 14.
Symbolic Form: [[6, 7, 14, ilcm]]
Word Problem: A farmer has 10 cows, 15 sheep, and 20 chickens. He wants to put the animals into pens so that each pen has the same number of each kind of animal. What is the least number of animals that can be in each pen?
Find the least common multiple of 10, 15 and 20.
Symbolic Form: [[10, 15, 20, ilcm]]

Word Problem: A train to Los Angeles leaves a station every 10 minutes. Another train to San Francisco leaves the same station every 8 minutes. If it is 9:00 am right now, at what time will both trains leave the station together?
Find the least common multiple of 10 and 8.
Symbolic Form: [[10, 8, ilcm]]

Word Problem: At a summer camp, the arts and crafts instructor wants to organize a schedule for the pottery and woodworking classes. The pottery class meets every 6 days, and the woodworking class meets every 8 days. If both classes were last held on the same day, after how many days will they next meet on the same day?
Find the least common multiple of 6 and 8.
Symbolic Form: [[6, 8, ilcm]]

Word Problem:A bakery makes blueberry muffins every 3 days, and another bakery makes blueberry muffins every 4 days. If both bakeries started making blueberry muffins on the same day, how many times in 24 days will they both make blueberry muffins on the same day?
Find the least common multiple of 3 and 4.
Symbolic Form: [[3, 4, ilcm]]
"""

SystemLinear_Num_Symbolic = """
Task: Do not solve problem. Symbolic Form has the structure of [[expression, expression, variable, variable, solve]] . Convert the Last Question into Symbolic Form same like given example.Given example:
Question: Solve the given system of equations by addition: 3*x + 4*y = 5,2*x - 3*y = 7
Symbolic Form: [[3*x + 4*y -5, 2*x - 3*y -7, x, y, solve]]

Question: Solve the given system of equations by addition:12*x + 13*y = 4,-y = -3  
Symbolic Form: [[12*x + 13*y -4, -y + 3, x, y, solve]]

Question: Solve the given system of equations by elimination 
-3*y = 66
-75*x -52*y = 77 
Symbolic Form: [[ -3*y -66,-75*x -52*y -77, x, y, solve]]

Question: Solve the given system of equations by substitution: 4*y = -12,-13*x  = 4 
Symbolic Form: [[ 4*y + 12,-13*x  -4, x, y, solve]]

Question: Solve the given system of equations by addition: 
9*y = -3
-5*x + 6*y = 13  
Symbolic Form: [[ 9*y + 3,-5*x + 6*y -13, x, y, solve]]

Question: Solve the given system of equations :-8*x -17*y = 0,-4*x -8*y = 8  
Symbolic Form: [[-8*x -17*y - 0,-4*x -8*y -8, x, y, solve]]
"""

SystemLinear_Word_Symbolic = """
Task: Do not solve problem. Symbolic Form has the structure of [[expression, expression, variable, variable, solve]]. Your task is formulate the Word Problem to System of equations then convert its into Symbolic Form same like given example.Given example:

Word Problem:The price, e, of an entertainment system at Extreme Electronics is $220 less than twice the price, u, of the same system at Ultra Electronics. The difference in price between the system at Extreme Electronics and Ultra Electronics is $175. What is the price of the system at each store?
Define the variables and formulate the linear system of equations:
Let e be the price of the system at Extreme Electronics.
Let u be the price of the system at Ultra Electronics.
The price of the system at Extreme Electronics is $220 less than twice the price of the system at Ultra Electronics: e = 2*u - 220
The difference in price between the two systems is $175: e - u = 175
System of equations: {e = 2*u - 220, e - u = 175}
The answer is:Symbolic Form: [[e - 2*u + 220, e - u - 175, e, u, solve]]

Word Problem: After inheriting a sum of money, Michael decides to invest it in two different types of accounts. He puts part of the money in a high-yield savings account with a 3% annual interest rate and the rest in a stock market index fund with an expected return of 7% per year. After one year, the total interest and returns from both accounts amount to $4,200. If he invested a total of $70,000, how much did he put in each type of account?

Define the variables and formulate the linear system of equations:
Let x be the amount of money invested in the high-yield savings account.
Let y be the amount of money invested in the stock market index fund.
Michael invested a total of $70,000: x + y = 70000
The high-yield savings account has a 3% annual interest rate: 0.03*x
The stock market index fund has an expected return of 7% per year: 0.07*y
Michael earned $4,200 in interest and returns after one year: 0.03*x + 0.07*y = 4200
System of equations: {x + y = 70000, 0.03*x + 0.07*y = 4200}
The answer is:Symbolic Form: [[x + y - 70000, 0.03*x + 0.07*y - 4200, x, y, solve]]

Word Problem:It takes three hours for a boat to go 18 miles downstream, and nine hours to return. What is the rate of the boat in calm water and the rate of the current?
Define the variables and formulate the linear system of equations:
To establish the equations, we need to understand the relationship between distance, rate, and time:
Distance = Rate * Time
Let b be the rate of the boat in calm water.
Let c be the rate of the current.
When the boat travels downstream, its speed is the sum of the boat's rate in calm water and the current's rate:
Downstream speed = Boat's rate (b) + Current's rate (c)
When the boat travels upstream, its speed is the difference between the boat's rate in calm water and the current's rate:
Upstream speed = Boat's rate (b) - Current's rate (c)
Downstream travel
Distance = (Boat's rate + Current's rate) * Time
18 = (b + c) * 3
18 = 3*b + 3*c
Upstream travel
Distance = (Boat's rate - Current's rate) * Time
18 = (b - c) * 9
18 = 9*b - 9*c
System of equations: {3*b + 3*c = 18, 9*b - 9*c = 18}
The answer is:Symbolic Form: [[3*b + 3*c - 18, 9*b - 9*c - 18, b, c, solve]]

Word Problem: A fruit juice company wants to create a new blend of apple juice using two different concentrates. They have a 30% apple juice concentrate and a 60% apple juice concentrate. The company needs to produce 500 liters of a 40% apple juice blend. How many liters of the 30% concentrate and how many liters of the 60% concentrate should be used?

Define the variables and formulate the linear system of equations:
Let x be the amount of the 30% apple juice concentrate.
Let y be the amount of the 60% apple juice concentrate.
The total volume of the apple juice blend = Volume of 30% concentrate + Volume of 60% concentrate
The company needs to produce 500 liters of a 40% apple juice blend: x + y = 500
Total amount of apple juice = (Volume of 30% concentrate * 30%) + (Volume of 60% concentrate * 60%)
The desired apple juice concentration is 40%: 0.4*(x + y)
The 30% apple juice concentrate: 0.3*x
The 60% apple juice concentrate: 0.6*y
The target is to create a 40% apple juice blend from the 30% and 60% concentrates: 0.4*(x + y) = 0.3*x + 0.6*y
System of equations: {x + y = 500, 0.4*(x + y) = 0.3*x + 0.6*y}
The answer is:Symbolic Form: [[x + y - 500, 0.4*(x + y) - 0.3*x - 0.6*y, x, y, solve]]

Word Problem: The Rocket Coaster has 15 cars, some that hold 4 people and some that hold 6 people.There is room for 72 people. How many 4-person cars and how many 6-person cars are there?

Define the variables and formulate the linear system of equations:
Let x be the number of 4-person cars.
Let y be the number of 6-person cars.
Total cars = number of 4-person cars + number of 6-person cars
The Rocket Coaster has 15 cars in total: x + y = 15
Total capacity = (number of 4-person cars * 4) + (number of 6-person cars * 6)
The total capacity of the coaster is 72 people and each 4-person car holds 4 people and each 6-person car holds 6 people: 4*x + 6*y = 72
System of equations: {x + y = 15, 4*x + 6*y = 72}
The answer is:Symbolic Form: [[x + y - 15, 4*x + 6*y - 72, x, y, solve]]
"""

CompoundInequalities_Num_Symbolic = """
Task: Do not solve problem. Symbolic Form has the structure of [[expression, inequality symbols, expression, variable, solve]] . Convert the problem into Symbolic Form same like given example.Given example:
Question:Solve this compound inequalities:  4*y -17 < 19 and -39*y  <= -47 
Symbolic Form: [[4*y -17 < -19, -39*y <= 47, y, solve]]

Question: Solve this compound inequalities:  -18 < 6*z + 18 < 17 
Symbolic Form: [[-18 < 6*z + 18, 6*z + 18 < 17, z, solve]]

Question: Solve this compound inequalities: 12*y -3 > 9 and 4*y  < 7 
Symbolic Form: [[12*y -3 > 9, 4*y  < 7, y, solve]]

Question: Solve this compound inequalities: 3 < x -72 < 7 
Symbolic Form: [[x -72 -3 > 0, x -72 -7 < 0, x, solve]]

Question:Solve this compound inequalities:  -43 <= -5*z + 457 <= 33 
Symbolic Form: [[-43 <= -5*z + 457, -5*z + 457 <= 33, z, solve]]
"""

CompoundInequalities_Word_Symbolic = """
Task: Do not solve problem. Symbolic Form has the structure of [[expression, expression, variable, solve]].
Convert the problem into Symbolic Form same like given example.Given example:
Word Problem:If a number is multiplied by -2 and then 10 is subtracted from the result, the difference falls between -2 and 15. Find the possible range of the number.
Define the variables and formulate the compound inequality:
Let x be the number.
The difference is calculated as -2*x - 10
We finding range for number falls between -2 and 15 so the difference is -2 < -2*x - 10 < 15
Compound Inequality: -2 < -2*x - 10 < 15
The answer is:Symbolic Form: [[-2 < -2*x - 10, -2*x - 10 < 15, x, solve]]

Word Problem: A ski shop carries skis that are between 150 and 220cm long. They recommend that the skis be 1.25 longer than your height.Calculate the tallest height that a person can be and still rent skis from the shop.
Define the variables and formulate the compound inequality:
Let x be the height of the person.
between 150 and 220cm long can be written as 150 <= Ski length <= 220
The skis should be 1.25 times longer than your height so the ski length is 1.25*x
Compound Inequality: 150 <= 1.25*x <= 220
The answer is:Symbolic Form: [[150 <= 1.25*x, 1.25*x <= 220, x, solve]]

Word Problem: Mia is a baker who wants to make a profit of at least $200 but no more than $300 on a large order of cupcakes for a wedding. She has already spent $150 on ingredients and the decorations. Each cupcake she sells will bring in a profit of $2. How many cupcakes does Mia need to sell to make her desired profit?
Define the variables and formulate the compound inequality:
Let x be the number of cupcakes Mia needs to sell.
at least $200 but no more than $300 so the profit is 200 <= Profit <= 300
Profit = Total revenue - Total cost
Total revenue = Profit from selling cupcakes
Each cupcake she sells will bring in a profit of $2 so the profit from selling cupcakes is x*2
Total cost = Cost of ingredients and decorations
She has already spent $150 on ingredients and the decorations so the cost of ingredients and decorations is 150
Profit = x*2 - 150
We can find the number of cupcakes Mia needs to sell by solving the compound inequality: 200 <= x*2 - 150 <= 300
The answer is:Symbolic Form: [[200 <= x*2 - 150, x*2 - 150 <= 300, x, solve]]

Word Problem:The sum of three times a number and five is between negative one and fifteen.Find the range of numbers that satisfy this condition.
Define the variables and formulate the compound inequality:
Let x be the number.
The sum of three times a number and five is 3*x + 5
range of acceptable sums is between negative one and fifteen so the sum is -1 < 3*x + 5 < 15
Compound Inequality: -1 < 3*x + 5 < 15
The answer is:Symbolic Form: [[-1 < 3*x + 5, 3*x + 5 < 15, x, solve]]

Word Problem: An electronics store is giving a $50 discount coupon for all smart watches. Emma is considering various smart watches with prices ranging from $220 to $310. How much can she anticipate to pay after applying the discount coupon?
Define the variables and formulate the compound inequality:
Let x be the price of the smart watch.
ranging from $220 to $310 so the price of the smart watch is 220 <= x <= 310
The store is giving a $50 discount coupon for all smart watches so the price after the discount coupon is x - 50
Combining the inequalities and the discount coupon: 220 <= x - 50 <= 310
The answer is:Symbolic Form: [[220 <= x - 50, x - 50 <= 310, x, solve]]
"""

Inequalities_Num_Direct_5_Shot = """
Please act as a professional math teacher. Your goal is to accurately solve a math word problem.
To achieve the goal, you have two jobs:

1. Write a detailed solution to a given question.
2. Write the final answer to this question.

Ensure the solution is step-by-step.

Given Question: {Insert given question here}
Your output should be in the following format:

SOLUTION: <your detailed solution to the given question>
FINAL ANSWER: <your final answer>

Follow these examples to solve the given question.

### Example 1:
Question: Inequality: 9*x + 16 <= 3*x - 20

SOLUTION:
Step 1: Start by isolating the variable x on one side of the inequality. Subtract 3x from both sides:
9x + 16 - 3x <= 3x - 20 - 3x
6x + 16 <= -20

Step 2: Subtract 16 from both sides to further isolate 6x:
6x + 16 - 16 <= -20 - 16
6x <= -36

Step 3: Divide both sides by 6 to solve for x:
x <= -36 / 6
x <= -6

FINAL ANSWER: x <= -6

### Example 2:
Question: Inequality: -32*x - 18 < -37*x - 3

SOLUTION:
Step 1: Begin by moving the variable terms to one side by adding 37x to both sides:
-32x + 37x - 18 < -37x + 37x - 3
5x - 18 < -3

Step 2: Add 18 to both sides to isolate 5x:
5x - 18 + 18 < -3 + 18
5x < 15

Step 3: Divide both sides by 5 to solve for x:
x < 15 / 5
x < 3

FINAL ANSWER: x < 3

### Example 3:
Question: Solve the inequality: -7*y - 32 <= -6*y

SOLUTION:
Step 1: Move the variable terms to one side by adding 7y to both sides:
-7y + 7y - 32 <= -6y + 7y
-32 <= y

FINAL ANSWER: y >= -32

### Example 4:
Question: Inequality: 17*x - 41 > -41

SOLUTION:
Step 1: Add 41 to both sides to isolate the term with x:
17x - 41 + 41 > -41 + 41
17x > 0

Step 2: Divide both sides by 17 to solve for x:
x > 0 / 17
x > 0

FINAL ANSWER: x > 0

### Example 5:
Question: Solve the inequality: -16*z + 6 > -14*z + 32

SOLUTION:
Step 1: Begin by moving the variable terms to one side by adding 14z to both sides:
-16z + 14z + 6 > -14z + 14z + 32
-2z + 6 > 32

Step 2: Subtract 6 from both sides to isolate -2z:
-2z + 6 - 6 > 32 - 6
-2z > 26

Step 3: Divide both sides by -2 and reverse the inequality sign:
z < 26 / -2
z < -13

FINAL ANSWER: z < -13
Given Question: 
"""

Inequalities_Word_Direct_5_Shot = """
Please act as a professional math teacher. Your goal is to accurately solve a math word problem.
To achieve the goal, you have two jobs:

1. Write a detailed solution to a given question.
2. Write the final answer to this question.

Ensure the solution is step-by-step.

Your output should be in the following format:

SOLUTION: <your detailed solution to the given question>
FINAL ANSWER: <your final answer>

Follow these examples to solve the given question.

### Example 1:
Word Problem: Brice has $30 to take his brother and his friends to the movies. If each ticket costs $4.00, and he must buy tickets for himself and his brother, what is the greatest number of friends he can invite?

SOLUTION:
Step 1: Let x be the number of friends Brice can invite. The total cost of the tickets is given by:
4(x + 2)  (since he buys tickets for himself, his brother, and x friends).

Step 2: Write the inequality for the total cost:
4(x + 2) <= 30

Step 3: Simplify and solve the inequality:
4x + 8 <= 30
4x <= 22
x <= 22/4
x <= 5.5

Step 4: Since x must be a whole number, round down to the nearest integer.
x <= 5 

FINAL ANSWER: Brice can invite up to 5 friends.

### Example 2:
Word Problem: What numbers satisfy the condition: nine less than negative four times a number is strictly greater than negative one?

SOLUTION:
Step 1: Let x represent the unknown number. Translate the word problem into an inequality:
-4x - 9 > -1

Step 2: Add 9 to both sides to begin isolating x:
-4x > -1 + 9
-4x > 8

Step 3: Divide both sides by -4, remembering to reverse the inequality sign:
x < 8/-4
x < -2

FINAL ANSWER: x < -2 

### Example 3:
Word Problem: The elevator in Yehires apartment building has a sign that says the maximum weight is 2,100 pounds. If the average weight of one person is 150 pounds, how many people can safely ride the elevator?

SOLUTION:
Step 1: Let x represent the number of people. Write the inequality for the total weight:
150x <= 2100

Step 2: Solve the inequality:
x <= 2100/150
x <= 14

FINAL ANSWER: Up to 14 people can safely ride the elevator.

### Example 4:
Word Problem: Brenda has $500 in her bank account. Every week, she withdraws $40 for expenses. Without making any deposits, how many weeks can she withdraw this money if she wants to maintain a balance of at least $200?

SOLUTION:
Step 1: Let x be the number of weeks Brenda can withdraw money. Write the inequality for the remaining balance:
500 - 40x >= 200

Step 2: Subtract 500 from both sides to begin isolating x:
-40x >= 200 - 500
-40x >= -300

Step 3: Divide both sides by -40, remembering to reverse the inequality sign:
x <= -300/-40
x <= 7.5

Step 4: Since x must be a whole number, round down to the nearest integer.
x <= 7 

FINAL ANSWER: Brenda can withdraw money for up to 7 weeks.

### Example 5:
Word Problem: Five student government officers want to go to the state convention. It will cost them $110 for registration, $375 for transportation and food, and $42 per person for the hotel. There is $450 budgeted for the convention in the student government savings account. They can earn the rest of the money they need by having a car wash. If they charge $5 per car, how many cars must they wash in order to have enough money to pay for the trip?

SOLUTION:
Step 1: Calculate the total cost of the trip:
Total cost = $110 + $375 + 5 * $42 = $695.

Step 2: Let x be the number of cars they need to wash. Write the inequality for the money needed:
450 + 5x >= 695

Step 3: Subtract 450 from both sides to begin isolating x:
5x >= 245

Step 4: Divide both sides by 5 to solve for x:
x >= 245/5
x >= 49

FINAL ANSWER: They must wash at least 49 cars.

Given Question:
"""

GCD_NUM_Direct_5_Shot = """
Please act as a professional math teacher. Your goal is to accurately solve a math word problem.
To achieve the goal, you have two jobs:

1. Write a detailed solution to a given question.
2. Write the final answer to this question.

Ensure the solution is step-by-step.

Given Question: {Insert given question here}
Your output should be in the following format:

SOLUTION: <your detailed solution to the given question>
FINAL ANSWER: <your final answer>

Follow these examples to solve the given question.

Example 1:
Question: Calculate the greatest common divisor of 18, 27.

SOLUTION: Step 1: Find the prime factorization of each number.

18 = 2 * 3^2
27 = 3^3
Step 2: Identify the common prime factors and their lowest powers.

The common prime factor is 3, and the lowest power is 3^2.
Step 3: The greatest common divisor is the product of the common prime factors.

GCD = 3^2 = 9
FINAL ANSWER: 9

### Example 2:
Question: Calculate the greatest common divisor of 466, 708, 30.

SOLUTION:
Step 1: Find the prime factorization of each number.
466 = 2 * 233
708 = 2^2 * 3 * 59
30 = 2 * 3 * 5

Step 2: Identify the common prime factors and their lowest powers.
The only common prime factor is 2.

Step 3: The greatest common divisor is the product of the common prime factors.
GCD = 2^1 = 2

FINAL ANSWER: 2

### Example 3:
Question: Calculate the greatest common divisor of 43, 56, 33.

SOLUTION:
Step 1: Find the prime factorization of each number.
43 is a prime number, so it remains 43.
56 = 2^3 * 7
33 = 3 * 11

Step 2: Identify the common prime factors.
There are no common prime factors among these numbers.

Step 3: If there are no common prime factors, the greatest common divisor is 1.
GCD = 1

FINAL ANSWER: 1

### Example 4:
Question: Find the greatest common divisor of 15, 30, 45.

SOLUTION:
Step 1: Find the prime factorization of each number.
15 = 3 * 5
30 = 2 * 3 * 5
45 = 3^2 * 5

Step 2: Identify the common prime factors and their lowest powers.
The common prime factors are 3 and 5, with the lowest powers being 3^1 and 5^1.

Step 3: The greatest common divisor is the product of the common prime factors.
GCD = 3^1 * 5^1 = 15

FINAL ANSWER: 15

### Example 5:
Question: Find the greatest common divisor of 12, 18, 24.

SOLUTION:
Step 1: Find the prime factorization of each number.
12 = 2^2 * 3
18 = 2 * 3^2
24 = 2^3 * 3

Step 2: Identify the common prime factors and their lowest powers.
The common prime factors are 2 and 3, with the lowest powers being 2^1 and 3^1.

Step 3: The greatest common divisor is the product of the common prime factors.
GCD = 2^1 * 3^1 = 6

FINAL ANSWER: 6

Given Question:
"""

GCD_Word_Direct_5_Shot = """    
Please act as a professional math teacher. Your goal is to accurately solve a math word problem.
To achieve the goal, you have two jobs:

1. Write a detailed solution to a given question.
2. Write the final answer to this question.

Ensure the solution is step-by-step.

Given Question: {Insert given question here}
Your output should be in the following format:

SOLUTION: <your detailed solution to the given question>
FINAL ANSWER: <your final answer>

Follow these examples to solve the given question.

### Example 1:
Word Problem: Find the greatest possible length that can be used to measure exactly the lengths 84 feet, 98 feet, and 126 feet.

SOLUTION:
Step 1: Find the prime factorization of each number.
- 84 = 2^2 * 3 * 7
- 98 = 2 * 7^2
- 126 = 2 * 3 * 7^2

Step 2: Identify the common prime factors and their lowest powers.
- The common prime factors are 2 and 7, with the lowest powers being 2^1 and 7^1.

Step 3: The greatest common divisor is the product of the common prime factors.
- GCD = 2^1 * 7^1 = 14

FINAL ANSWER: 14 feet

### Example 2:
Word Problem: A warehouse has three shelves that can hold 8, 12, or 16 skateboards. Each shelf has sections holding the same number of skateboards. What is the greatest number of skateboards that can be put in a section?

SOLUTION:
Step 1: Find the prime factorization of each number.
- 8 = 2^3
- 12 = 2^2 * 3
- 16 = 2^4

Step 2: Identify the common prime factors and their lowest powers.
- The common prime factor is 2, with the lowest power being 2^2.

Step 3: The greatest common divisor is the product of the common prime factors.
- GCD = 2^2 = 4

FINAL ANSWER: 4 skateboards per section

### Example 3:
Word Problem: A motorcycle dealership has 30 Yamaha R1s and 42 Honda CBRs in their inventory. The dealership wants to arrange the motorcycles in rows so that each row contains the same number of motorcycles and an equal number of each motorcycle type. What is the greatest number of rows that can be formed under these conditions?

SOLUTION:
Step 1: Find the prime factorization of each number.
- 30 = 2 * 3 * 5
- 42 = 2 * 3 * 7

Step 2: Identify the common prime factors and their lowest powers.
- The common prime factors are 2 and 3, with the lowest powers being 2^1 and 3^1.

Step 3: The greatest common divisor is the product of the common prime factors.
- GCD = 2^1 * 3^1 = 6

Step 4: To find the number of rows, divide the number of motorcycles by the GCD.
- Number of rows = GCD = 6

FINAL ANSWER: The dealership can form 6 rows.

### Example 4:
Word Problem:Henry bought 27 apples and 36 pears and wishes to make fruit baskets for friends. He would like to make identical baskets. What is the greatest number of fruit baskets Henry can make?

SOLUTION:
Step 1: Find the prime factorization of each number.
- 27 = 3^3
- 36 = 2^2 * 3^2

Step 2: Identify the common prime factors and their lowest powers.
- The common prime factor is 3, with the lowest power being 3^2.

Step 3: The greatest common divisor is the product of the common prime factors.
- GCD = 3^2 = 9

Step 4: To find the number of baskets, divide the number of fruits by the GCD.
- Number of baskets = GCD = 9

FINAL ANSWER: Henry can make 9 fruit baskets.

### Example 5:
Word Problem: A farmer has 24 cows, 36 sheep, and 48 pigs. He wants to build pens that can hold the same number of animals and an equal number of each type of animal. What is the greatest number of animals that can be put in each pen?

SOLUTION:

Step 1: Find the prime factorization of each number.
- 24 = 2^3 * 3
- 36 = 2^2 * 3^2
- 48 = 2^4 * 3

Step 2: Identify the common prime factors and their lowest powers.
- The common prime factors are 2 and 3, with the lowest powers being 2^2 and 3^1.

Step 3: The greatest common divisor is the product of the common prime factors.
- GCD = 2^2 * 3^1 = 12

FINAL ANSWER: Each pen can hold 12 animals.

Given Question:
"""

System_Linear_Num_Direct_5_Shot = """    
Please act as a professional math teacher. Your goal is to accurately solve a math word problem.
To achieve the goal, you have two jobs:

1. Write a detailed solution to a given question.
2. Write the final answer to this question.

Ensure the solution is step-by-step.

Given Question: {Insert given question here}
Your output should be in the following format:

SOLUTION: <your detailed solution to the given question>
FINAL ANSWER: <your final answer>

Follow these examples to solve the given question.

### Example 1:
Question: Solve the given system of equations by addition: 3*x + 4*y = 5, 2*x - 3*y = 7

SOLUTION:
Step 1: Multiply the equations to make the coefficients of one variable opposites.
- Multiply the first equation by 3: 9*x + 12*y = 15
- Multiply the second equation by 4: 8*x - 12*y = 28

Step 2: Add the two equations to eliminate y.
- (9*x + 12*y) + (8*x - 12*y) = 15 + 28
- 17*x = 43

Step 3: Solve for x.
- x = 43 / 17
- x = 43/17

Step 4: Substitute x back into one of the original equations to solve for y.
- 3*(43/17) + 4*y = 5
- 129/17 + 4*y = 5
- 4*y = 5 - (129/17)
- y = (5-(129/17)) / 4
- y = -11/17
FINAL ANSWER: x = 43/17, y = -11/17.

### Example 2:
Question: Solve the given system of equations by addition: 12*x + 16*y -6, -y = -3  

SOLUTION:
Step 1: Recognize that -y = -3 simplifies to y = 3.

Step 2: Substitute y = 3 into the first equation.
- 12*x + 13*(3) = 4
- 12*x + 39 = 4

Step 3: Solve for x.
- 12*x = 4 - 39
- 12*x = -35
- x = -35/12

FINAL ANSWER: x = -35/12, y = 3

### Example 3:
Question: Solve the given system of equations by substitution: 
4*y = -12, -13*x = 4 

SOLUTION:
Step 1: Solve the first equation for y.
- y = -12 / 4
- y = -3

Step 2: Solve the second equation for x.
- x = 4 / -13
- x = -4/13

FINAL ANSWER: x = -4/13, y = -3

### Example 4:
Question: Solve the given system of equations by addition: 
9*y = -3, -5*x + 6*y = 13  

SOLUTION:
Step 1: Solve the first equation for y.
- y = -3 / 9
- y = -1/3

Step 2: Substitute y = -1/3 into the second equation.
- -5*x + 6*(-1/3) = 13
- -5*x - 2 = 13

Step 3: Solve for x.
- -5*x = 13 + 2
- -5*x = 15
- x = -15/5
- x = -3

FINAL ANSWER: x = -3, y = -1/3

### Example 5:
Question: Solve the given system of equations: 
-8*x - 17*y = 0, -4*x - 8*y = 8 

SOLUTION:
Step 1: Multiply the second equation by 2 to make the coefficients of x the same.
- -8*x - 16*y = 16

Step 2: Subtract the second equation from the first to eliminate x.
- (-8*x - 17*y) - (-8*x - 16*y) = 0 - 16
- -y = -16

Step 3: Solve for y.
- y = 16

Step 4: Substitute y = 16 into one of the original equations to solve for x.
- -8*x - 17*(16) = 0
- -8*x - 272 = 0
- -8*x = 272
- x = -272/8
- x = -34

FINAL ANSWER: x = -34, y = 16
Given Question:
"""

System_Linear_Word_Direct_5_Shot = """
Please act as a professional math teacher. Your goal is to accurately solve a math word problem.
To achieve the goal, you have two jobs:

1. Write a detailed solution to a given question.
2. Write the final answer to this question.

Ensure the solution is step-by-step.

Given Question: {Insert given question here}
Your output should be in the following format:

SOLUTION: <your detailed solution to the given question>
FINAL ANSWER: <your final answer>

Follow these examples to solve the given question.

### Example 1:
Word Problem: The Rocket Coaster has 15 cars, some that hold 4 people and some that hold 6 people. There is room for 72 people. How many 4-person cars and how many 6-person cars are there?

SOLUTION:
Step 1: Let x be the number of 4-person cars and y be the number of 6-person cars.
Step 2: Set up the system of equations based on the given information:
    - x + y = 15  (Equation 1: Total number of cars)
    - 4x + 6y = 72  (Equation 2: Total number of people)

Step 3: Solve Equation 1 for x:
    - x = 15 - y

Step 4: Substitute x = 15 - y into Equation 2:
    - 4(15 - y) + 6y = 72
    - 60 - 4y + 6y = 72
    - 2y = 12
    - y = 6

Step 5: Substitute y = 6 into Equation 1 to find x:
    - x + 6 = 15
    - x = 9

FINAL ANSWER: There are 9 four-person cars and 6 six-person cars.

### Example 2:
Word Problem: The price, e, of an entertainment system at Extreme Electronics is $220 less than twice the price, u, of the same system at Ultra Electronics. The difference in price between the system at Extreme Electronics and Ultra Electronics is $175. What is the price of the system at each store?

SOLUTION:
Step 1: Set up the equations based on the given information:
    - e = 2u - 220  (Equation 1)
    - e - u = 175  (Equation 2)

Step 2: Substitute Equation 1 into Equation 2:
    - (2u - 220) - u = 175
    - u - 220 = 175
    - u = 395

Step 3: Substitute u = 395 into Equation 1 to find e:
    - e = 2(395) - 220
    - e = 790 - 220
    - e = 570

FINAL ANSWER: The price of the system at Extreme Electronics is $570, and the price at Ultra Electronics is $395.

### Example 3:
Word Problem: A farmer raises both chickens and pigs on his farm. He counts a total of 30 heads and 90 legs among the animals in his barn. Assuming that each chicken has one head and two legs, while each pig has one head and four legs, how many chickens and how many pigs does the farmer have?

SOLUTION:
Step 1: Let x be the number of chickens and y be the number of pigs.
Step 2: Set up the system of equations based on the given information:
    - x + y = 30  (Equation 1: Total number of heads)
    - 2x + 4y = 90  (Equation 2: Total number of legs)

Step 3: Solve Equation 1 for x:
    - x = 30 - y

Step 4: Substitute x = 30 - y into Equation 2:
    - 2(30 - y) + 4y = 90
    - 60 - 2y + 4y = 90
    - 2y = 30
    - y = 15

Step 5: Substitute y = 15 into Equation 1 to find x:
    - x + 15 = 30
    - x = 15

FINAL ANSWER: The farmer has 15 chickens and 15 pigs.

### Example 4:
Word Problem: The length of a rectangle is equal to triple the width. Which system of equations can be used to find the dimensions of the rectangle if the perimeter is 86 centimeters?

SOLUTION:
Step 1: Let l be the length and w be the width of the rectangle.
Step 2: Set up the equations based on the given information:
    - l = 3w  (Equation 1: The length is triple the width)
    - 2l + 2w = 86  (Equation 2: The perimeter of the rectangle)

Step 3: Substitute Equation 1 into Equation 2:
    - 2(3w) + 2w = 86
    - 6w + 2w = 86
    - 8w = 86
    - w = 86 / 8
    - w = 10.75 cm

Step 4: Substitute w = 10.75 into Equation 1 to find l:
    - l = 3(10.75)
    - l = 32.25 cm

FINAL ANSWER: The width of the rectangle is 10.75 cm, and the length is 32.25 cm.
    
Given Question:
"""

LCM_NUM_Direct_5_Shot = """
Please act as a professional math teacher. Your goal is to accurately solve a math word problem.
To achieve this goal, you have two jobs:

1. Write a detailed solution to the given question.
2. Write the final answer to this question.

Ensure the solution is step-by-step.

Given Question: <insert given question here>

Your output should be in the following format:

SOLUTION: <your detailed solution to the given question>
FINAL ANSWER: <your final answer>

Follow these examples to solve the given question.

Example 1:
Question: What is the smallest common multiple of 43, 56, 33?

SOLUTION:
To find the smallest common multiple (LCM) of three numbers, we need to find the LCM of their prime factors.

1. First, find the prime factorization of each number:
   - 43 is a prime number.
   - 56 = 2 * 2 * 2 * 7 = 2^3 * 7
   - 33 = 3 * 11

2. Identify all the unique prime factors: 2, 3, 7, 11, and 43.

3. For each unique prime factor, take the highest power that appears in the factorizations:
   - 2^3 (from 56)
   - 3 (from 33)
   - 7 (from 56)
   - 11 (from 33)
   - 43 (from 43)

4. Multiply these together to find the LCM:
   LCM = 2^3 * 3 * 7 * 11 * 43

5. Calculate the result:
   - LCM = 8 * 3 = 24
   - 24 * 7 = 168
   - 168 * 11 = 1848
   - 1848 * 43 = 79,464

FINAL ANSWER: 79,464

Example 2:
Question: What is the smallest common multiple of 18, 27?

SOLUTION:
To find the LCM of two numbers, we need to find the LCM of their prime factors.

1. First, find the prime factorization of each number:
   - 18 = 2 * 3 * 3 = 2 * 3^2
   - 27 = 3 * 3 * 3 = 3^3

2. Identify all the unique prime factors: 2 and 3.

3. For each unique prime factor, take the highest power that appears in the factorizations:
   - 2 (from 18)
   - 3^3 (from 27)

4. Multiply these together to find the LCM:
   LCM = 2 * 3^3

5. Calculate the result:
   - LCM = 2 * 27 = 54

FINAL ANSWER: 54

Example 3:
Question: What is the smallest common multiple of 466, 708, 30?

SOLUTION:
To find the LCM of three numbers, we need to find the LCM of their prime factors.

1. First, find the prime factorization of each number:
   - 466 = 2 * 233
   - 708 = 2 * 2 * 3 * 59 = 2^2 * 3 * 59
   - 30 = 2 * 3 * 5

2. Identify all the unique prime factors: 2, 3, 5, 59, and 233.

3. For each unique prime factor, take the highest power that appears in the factorizations:
   - 2^2 (from 708)
   - 3 (from 708 and 30)
   - 5 (from 30)
   - 59 (from 708)
   - 233 (from 466)

4. Multiply these together to find the LCM:
   LCM = 2^2 * 3 * 5 * 59 * 233

5. Calculate the result:
   - LCM = 4 * 3 = 12
   - 12 * 5 = 60
   - 60 * 59 = 3540
   - 3540 * 233 = 824,820

FINAL ANSWER: 824,820
"""

LCM_WORD_Direct_5_Shot = """
Please act as a professional math teacher. Your goal is to accurately solve a math word problem.
To achieve this goal, you have two jobs:

1. Write a detailed solution to the given question.
2. Write the final answer to this question.

Ensure the solution is step-by-step.

Given Question: <insert given question here>

Your output should be in the following format:

SOLUTION: <your detailed solution to the given question>
FINAL ANSWER: <your final answer>

Follow these examples to solve the given question.

Example 1:
Word Problem: Six bells commence tolling together and toll at intervals of 2, 4, 6, 8, 10, and 12 seconds respectively. In 30 minutes, how many times do they toll together? (excluding the one at start)

SOLUTION:
To solve this problem, we need to find the least common multiple (LCM) of the intervals at which the bells toll. The bells toll together whenever the total time elapsed is a multiple of the LCM of their intervals.

1. Find the prime factorization of each interval:
   - 2 = 2
   - 4 = 2^2
   - 6 = 2 * 3
   - 8 = 2^3
   - 10 = 2 * 5
   - 12 = 2^2 * 3

2. Identify the highest powers of all prime factors:
   - 2^3 (from 8)
   - 3 (from 6 and 12)
   - 5 (from 10)

3. Calculate the LCM using the highest powers of each prime:
   LCM = 2^3 * 3 * 5 = 120 seconds

4. Convert 30 minutes to seconds:
   30 minutes = 30 * 60 = 1800 seconds

5. Determine how many times the bells toll together in 1800 seconds:
   Number of tolls = 1800 / 120 = 15

6. Exclude the initial toll at the start:
   15 - 1 = 14

FINAL ANSWER: 14

Example 2:
Word Problem: A farmer has 10 cows, 15 sheep, and 20 chickens. He wants to put the animals into pens so that each pen has the same number of each kind of animal. What is the least number of animals that can be in each pen?

SOLUTION:
To find the least number of animals that can be in each pen, we need to find the greatest common divisor (GCD) of the numbers of each type of animal.

1. Find the GCD of 10, 15, and 20:
   - Prime factorization of 10 = 2 * 5
   - Prime factorization of 15 = 3 * 5
   - Prime factorization of 20 = 2^2 * 5
   - The common prime factor is 5.

2. The greatest common divisor is 5.

3. Divide the number of each animal by the GCD to find the number of animals in each pen:
   - 10 / 5 = 2 cows
   - 15 / 5 = 3 sheep
   - 20 / 5 = 4 chickens

4. Calculate the total number of animals in each pen:
   2 + 3 + 4 = 9

FINAL ANSWER: 9

Example 3:
Word Problem: A train to Los Angeles leaves a station every 10 minutes. Another train to San Francisco leaves the same station every 8 minutes. If it is 9:00 am right now, at what time will both trains leave the station together?

SOLUTION:
To determine when both trains will leave the station together, we need to find the least common multiple (LCM) of their departure intervals.

1. Find the LCM of 10 and 8:
   - Prime factorization of 10 = 2 * 5
   - Prime factorization of 8 = 2^3
   - The LCM is 2^3 * 5 = 40 minutes

2. Calculate the time after 9:00 am when both trains leave together:
   9:00 am + 40 minutes = 9:40 am

FINAL ANSWER: 9:40 am

Example 4:
Word Problem: At a summer camp, the arts and crafts instructor wants to organize a schedule for the pottery and woodworking classes. The pottery class meets every 6 days, and the woodworking class meets every 8 days. If both classes were last held on the same day, after how many days will they next meet on the same day?

SOLUTION:
To find when both classes will next meet on the same day, we need to find the least common multiple (LCM) of 6 and 8.

1. Find the LCM of 6 and 8:
   - Prime factorization of 6 = 2 * 3
   - Prime factorization of 8 = 2^3
   - The LCM is 2^3 * 3 = 24 days

FINAL ANSWER: 24 days

Example 5:
Word Problem: A bakery makes blueberry muffins every 3 days, and another bakery makes blueberry muffins every 4 days. If both bakeries started making blueberry muffins on the same day, how many times in 24 days will they both make blueberry muffins on the same day?

SOLUTION:
To solve this problem, we need to find the least common multiple (LCM) of 3 and 4 and then determine how many multiples of this LCM fit into 24 days.

1. Find the LCM of 3 and 4:
   - Prime factorization of 3 = 3
   - Prime factorization of 4 = 2^2
   - The LCM is 2^2 * 3 = 12 days

2. Determine how many times they will both make muffins in 24 days:
   Number of times = 24 / 12 = 2

FINAL ANSWER: 2

"""

Compound_Inequalities_Num_Direct_5_Shot = """
Please act as a professional math teacher. Your goal is to accurately solve a math word problem.
To achieve this goal, you have two jobs:

1. Write a detailed solution to the given question.
2. Write the final answer to this question.

Ensure the solution is step-by-step.

Given Question: <insert given question here>

Your output should be in the following format:

SOLUTION: <your detailed solution to the given question>
FINAL ANSWER: <your final answer>

Follow these examples to solve the given question.

Example 1:
Question: Solve this compound inequalities: 4*y - 17 < 19 and -39*y <= -47

SOLUTION:
To solve the compound inequalities, solve each inequality separately.

1. Solve the first inequality: 4*y - 17 < 19
   - Add 17 to both sides:
     4*y - 17 + 17 < 19 + 17
     4*y < 36
   - Divide both sides by 4:
     y < 9

2. Solve the second inequality: -39*y <= -47
   - Divide both sides by -39 (remember to flip the inequality sign):
     y >= -47 / -39
     y >= 47/39

3. Combine the two solutions:
   y >= 47/39 and y < 9

4. Express the final solution as an interval:
   y in [47/39, 9)

FINAL ANSWER: y in [47/39, 9)

Example 2:
Question: Solve this compound inequalities: -18 < 6*z + 18 < 17

SOLUTION:
To solve this compound inequality, solve each part of the inequality separately.

1. Solve the left part of the inequality: -18 < 6*z + 18
   - Subtract 18 from both sides:
     -18 - 18 < 6*z + 18 - 18
     -36 < 6*z
   - Divide both sides by 6:
     -36 / 6 < z
     -6 < z

2. Solve the right part of the inequality: 6*z + 18 < 17
   - Subtract 18 from both sides:
     6*z + 18 - 18 < 17 - 18
     6*z < -1
   - Divide both sides by 6:
     z < -1/6

3. Combine the two solutions:
   -6 < z < -1/6

4. Express the final solution as an interval:
   z in (-6, -1/6)

FINAL ANSWER: z in (-6, -1/6)

Example 3:
Question: Solve this compound inequalities: 12*y - 3 > 9 and 4*y < 7

SOLUTION:
To solve the compound inequalities, solve each inequality separately.

1. Solve the first inequality: 12*y - 3 > 9
   - Add 3 to both sides:
     12*y - 3 + 3 > 9 + 3
     12*y > 12
   - Divide both sides by 12:
     y > 1

2. Solve the second inequality: 4*y < 7
   - Divide both sides by 4:
     y < 7/4

3. Combine the two solutions:
   y > 1 and y < 7/4

4. Express the final solution as an interval:
   y in (1, 7/4)

FINAL ANSWER: y in (1, 7/4)

Example 4:
Question: Solve this compound inequalities: 3 < x - 72 < 7

SOLUTION:
To solve this compound inequality, solve each part of the inequality separately.

1. Solve the left part of the inequality: 3 < x - 72
   - Add 72 to both sides:
     3 + 72 < x - 72 + 72
     75 < x

2. Solve the right part of the inequality: x - 72 < 7
   - Add 72 to both sides:
     x - 72 + 72 < 7 + 72
     x < 79

3. Combine the two solutions:
   75 < x < 79

4. Express the final solution as an interval:
   x in (75, 79)

FINAL ANSWER: x in (75, 79)

Example 5:
Question: Solve this compound inequalities: -43 <= -5*z + 457 <= 33

SOLUTION:
To solve this compound inequality, solve each part of the inequality separately.

1. Solve the left part of the inequality: -43 <= -5*z + 457
   - Subtract 457 from both sides:
     -43 - 457 <= -5*z + 457 - 457
     -500 <= -5*z
   - Divide both sides by -5 (remember to flip the inequality sign):
     -500 / -5 >= z
     100 >= z
   - Rewrite it as:
     z <= 100

2. Solve the right part of the inequality: -5*z + 457 <= 33
   - Subtract 457 from both sides:
     -5*z + 457 - 457 <= 33 - 457
     -5*z <= -424
   - Divide both sides by -5 (remember to flip the inequality sign):
     z >= -424 / -5
     z >= 424/5

3. Combine the two solutions:
   424/5 <= z <= 100

4. Express the final solution as an interval:
   z in [424/5, 100]

FINAL ANSWER: z in [424/5, 100]

Given Question:
"""

Compound_Inequalities_Word_Direct_5_Shot = """
Please act as a professional math teacher. Your goal is to accurately solve a math word problem.
To achieve this goal, you have two jobs:

1. Write a detailed solution to the given question.
2. Write the final answer to this question.

Ensure the solution is step-by-step.

Given Question: <insert given question here>

Your output should be in the following format:

SOLUTION: <your detailed solution to the given question>
FINAL ANSWER: <your final answer>

Follow these examples to solve the given question.

Example 1:
Word Problem: A number is at least 5 and at most 15. Write a compound inequality that shows the range of numbers that satisfy this condition.

SOLUTION:
To express the condition "a number is at least 5 and at most 15," we can write a compound inequality that includes both of these statements:

1. The number is at least 5: x >= 5
2. The number is at most 15: x <= 15

Combining these two inequalities, we get:
5 <= x <= 15

FINAL ANSWER: 5 <= x <= 15

Example 2:
Word Problem: Mia is a baker who wants to make a profit of at least $200 but no more than $300 on a large order of cupcakes for a wedding. She has already spent $150 on ingredients and the decorations. Each cupcake she sells will bring in a profit of $2. How many cupcakes does Mia need to sell to make her desired profit?

SOLUTION:
To find the number of cupcakes Mia needs to sell, let's define x as the number of cupcakes sold.

1. Profit made from selling x cupcakes: 2*x dollars
2. Total profit after subtracting the cost of ingredients and decorations: 2*x - 150

We want this profit to be at least $200 but no more than $300:
200 <= 2*x - 150 <= 300

To solve for x, first add 150 to all parts of the inequality:
200 + 150 <= 2*x <= 300 + 150
350 <= 2*x <= 450

Next, divide every part of the inequality by 2:
350/2 <= x <= 450/2
175 <= x <= 225

FINAL ANSWER: Mia needs to sell between 175 and 225 cupcakes.

Example 3:
Word Problem: A ski shop carries skis that are between 150 and 220 cm long. They recommend that the skis be 1.25 times longer than your height. Calculate the tallest height that a person can be and still rent skis from the shop.

SOLUTION:
Let h represent the height of the person.

1. The length of the skis should be 1.25 times the person's height: 1.25*h
2. The skis should be between 150 cm and 220 cm long: 150 <= 1.25*h <= 220

To solve for h, divide all parts of the inequality by 1.25:
150 / 1.25 <= h <= 220 / 1.25
120 <= h <= 176

FINAL ANSWER: The tallest height a person can be to rent skis from the shop is 176 cm.

Example 4:
Word Problem: An electronics store is giving a $50 discount coupon for all smart watches. Emma is considering various smart watches with prices ranging from $220 to $310. How much can she anticipate to pay after applying the discount coupon?

SOLUTION:
Let p represent the price of the smart watch.

1. The price after applying the $50 discount: p - 50
2. The original prices range from $220 to $310: 220 <= p <= 310

To calculate the price after discount, subtract 50 from each bound of the price range:
220 - 50 <= p - 50 <= 310 - 50
170 <= p - 50 <= 260

FINAL ANSWER: Emma can anticipate paying between $170 and $260 after applying the discount.

Example 5:
Word Problem: A car rental company charges between $30 and $50 per day for renting a car. The company also requires a deposit of at least $100 but no more than $200. Write a compound inequality that represents the total cost of renting a car for a day, including the deposit.

SOLUTION:
Let c represent the total cost of renting a car for a day, including the deposit.

1. The daily rental cost ranges from $30 to $50: 30 <= c <= 50
2. The deposit required ranges from $100 to $200: 100 <= c <= 200

To represent the total cost, including the deposit, we add the rental cost and the deposit:
130 <= c <= 250

FINAL ANSWER: The compound inequality representing the total cost of renting a car for a day, including the deposit, is 130 <= c <= 250.

Given Question:
"""
