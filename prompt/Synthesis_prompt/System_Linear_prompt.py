Math_Teacher_Prompt = """I want you to act as Math Teacher. Your goal is to create new high quality math problems to help students learn math.Please create a new linear system based on the given Word Problems. Then transform the new linear system and symbolic form.When doing this you MUST follow these Principle: 

Principle:
1. Do not solve the linear system.
2. Create only one new problem similar to the given problem.
3. Symbolic Form is written in the form of [[expression, expression, variable, variable, solve]] and wrap by [[]]. 
4. There MUST be * between the coefficient and the variable. Example: 2*(2*x + 3) -7. 
5. DO NOT use the symbol //,$ and word in the expression.

Your output should be in the following format:
Word Problem: <Your created word problem>
Define the variables and formulate the linear system of equations: <Your created linear system of equations>
Symbolic Form: <Transformed linear system of equations to symbolic form>
""".strip()

WordProblem_Prompt = Math_Teacher_Prompt + """
Task:Create a new word problem for the linear system of equations and transform the problem to a symbolic form. Be as creative as possible and try to use any kind of topics for variation.
You will get rewarded for creativity and variety of the word problems.

Word Problem: The length of a rectangle is equal to triple the width. Which system of equations can be used to find the dimensions of the rectangle if the perimeter is 86 centimeters?
Define the variables and formulate the linear system of equations:
Let variable x represent the length of the rectangle and variable y represent the width of the rectangle. 
The length of a rectangle is equal to triple the width. So the equation is x = 3*y. 
The perimeter of the rectangle is 86 centimeters. So the equation is 2*x + 2*y = 86. 
System of equations: {x = 3*y, 2*x + 2*y = 86} 
Symbolic Form: [[x - 3*y, 2*x + 2*y - 86, x, y, solve]]

Word Problem: Emma and Liam are saving money. Emma starts with $80 and saves $10 per week. Liam starts with $120 and saves $6 per week. After how many weeks will they have the same amount of money?
Define the variables and formulate the linear system of equations:
Let variable x represent the number of weeks to have the same amount of money as variable y represent the amount of money. 
The amount of money Emma starts with is $80. So the equation is 80 + 10*x = y. 
The amount of money Liam starts with is $120. So the equation is 120 + 6*x = y. 
System of equations: {80 + 10*x = y, 120 + 6*x = y} 
Symbolic Form: [[80 + 10*x - y, 120 + 6*x - y, x, y, solve]]

Word Problem:  At the end of the 2000 NBA regular season, the Houston comets had 22 more victories than losses. The number of victories they had was three less than six time the number of losses. How many regular season games did the Houston comets play during the 2000 NBA season?
Define the variables and formulate the linear system of equations:
Let variable x represent the number of victories and variable y represent the number of losses.
The Houston comets had 22 more victories than losses. So the equation is x - y = 22.
The number of victories they had was three less than six time the number of losses. So the equation is x = 6*y - 3.
System of equations: {x - y = 22, x = 6*y - 3}
Symbolic Form: [[x - y - 22, x - 6*y + 3, x, y, solve]]

Word Problem: A farmer raises both chickens and pigs on his farm. He counts a total of 30 heads and 90 legs among the animals in his barn. Assuming that each chicken has one head and two legs, while each pig has one head and four legs, how many chickens and how many pigs does the farmer have?
Define the variables and formulate the linear system of equations:
Let variable x represent the number of chickens and variable y represent the number of pigs.
The total number of heads is 30. So the equation is x + y = 30.
The total number of legs is 90. So the equation is 2*x + 4*y = 90.
System of equations: {x + y = 30, 2*x + 4*y = 90}
Symbolic Form: [[x + y - 30, 2*x + 4*y - 90, x, y, solve]]

Word Problem:The price, e, of an entertainment system at Extreme Electronics is $220 less than twice the price, u, of the same system at Ultra Electronics. The difference in price between the system at Extreme Electronics and Ultra Electronics is $175. What is the price of the system at each store?
Define the variables and formulate the linear system of equations:
Let variable x represent the price of the system at Extreme Electronics and variable y represent the price of the system at Ultra Electronics.
The price, e, of an entertainment system at Extreme Electronics is $220 less than twice the price, u, of the same system at Ultra Electronics. So the equation is x = 2*y - 220.
The difference in price between the system at Extreme Electronics and Ultra Electronics is $175. So the equation is x - y = 175.
System of equations: {x = 2*y - 220, x - y = 175}
Symbolic Form: [[x - 2*y + 220, x - y - 175, x, y, solve]]

Word Problem: The Rocket Coaster has 15 cars, some that hold 4 people and some that hold 6 people.There is room for 72 people. How many 4-person cars and how many 6-person cars are there?
Define the variables and formulate the linear system of equations:
Let variable x represent the number of 4-person cars and variable y represent the number of 6-person cars.
The total number of cars is 15. So the equation is x + y = 15.
The total number of people is 72. So the equation is 4*x + 6*y = 72.
System of equations: {x + y = 15, 4*x + 6*y = 72}
Symbolic Form: [[x + y - 15, 4*x + 6*y - 72, x, y, solve]]

Word Problem:A business has two loans totaling $85,000. One loan has a rate of 6% and the other has a rate of 4.5% This year, the business expects to pay $4,650 in interest on the two loans. How much is each loan?
Define the variables and formulate the linear system of equations:
Let variable x represent the amount of the loan at 6% and variable y represent the amount of the loan at 4.5%.
The total amount of the two loans is $85,000. So the equation is x + y = 85000.
This year, the business expects to pay $4,650 in interest on the two loans. So the equation is 0.06*x + 0.045*y = 4650.
System of equations: {x + y = 85000, 0.06*x + 0.045*y = 4650}
Symbolic Form: [[x + y - 85000, 0.06*x + 0.045*y - 4650, x, y, solve]]

"""