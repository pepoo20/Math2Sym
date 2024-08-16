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


Inequalities_Num = """Task: Do not solve problem. Symbolic Form has the structure of [[expression, inequality symbols, expression, variable, solve]] . Convert the Last Question into Symbolic Form same like given example.Given example:
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

Inequalites_Word = """
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

GCD_Num = """Task: Do not solve the problem directly.Your answer must be the Symbolic Form not a number.Symbolic Form has the structure of [[expression, expression, expression, igcd]]. Convert the Question into Symbolic Form same like given example.Given example:
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

GCD_Word = """
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

LCM_Num = """
Task: Do not solve problem. Symbolic Form has the structure of [[expression, expression, expression, ilcm]] . Convert the problem into Symbolic Form same like given example.Given example:
Question:What is the smallest common multiple of 43, 56, 33?
Symbolic Form: [[43, 56, 33, ilcm]]

Question:What is the smallest common multiple of 18, 27?
Symbolic Form: [[18, 27, ilcm]]

Question:What is the smallest common multiple of 466, 708, 30?
Symbolic Form: [[466, 708, 30, ilcm]]

Question:What is the smallest common multiple of 43, 56, 33?
Symbolic Form: [[43, 56, 33, ilcm]]

Question:What is the smallest common multiple of 18, 27?
Symbolic Form: [[18, 27, ilcm]]

Question:What is the smallest common multiple of 466, 708, 30?
Symbolic Form: [[466, 708, 30, ilcm]]
"""

LCM_Word = """
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

SystemLinear_Num = """
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

SystemLinear_Word = """
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


CompoundInequalities_Num = """
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

CompoundInequalities_Word = """
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