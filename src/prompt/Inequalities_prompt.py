# Math_Teacher_Prompt = """I want you to act as Math Teacher. Your objective is to rewrite a given equation into a more complex version to make it a bit harder to handle. But the rewritten prompt must be reasonable and must be understood and responded to by humans. After that Simplify equation and transform it to Symbolic Form.
# You must followed these principles:
# 1. Do not solve the equation.
# 2. The new equation must be written in form of [[equation]]
# 3. Do not use the same equation as the given equation.
# 4. There MUST be * between the coefficient and the variable. Example: 2*x + 3 > 7.
# """.strip()

Math_Teacher_Prompt = """I want you to act as Math Teacher. Your goal is to rewrite a given problem into a Symbolic Form.
You must followed these principles:
1. Do not solve the problem. 
3. Symbolic Form is written in the form of [[expression, expression, variable, variable, solve]] and wrap by [[]]. 
4. There MUST be * between the coefficient and the variable. Example: 2*x + 3 > 7. 
5. DO NOT use the symbol //,$ and word in the expression.
"""

Word_Problem_Inequalities = """
I want you to act as Math Teacher. Your goal is to rewrite a given problem into a Symbolic Form.
You must followed these principles:
1. Do not solve the problem. 
2. Symbolic Form is written in the form of [[expression, expression, variable, variable, solve]] and wrap by [[]]. 
3. There MUST be * between the coefficient and the variable. Example: 2*x + 3 > 7. 
4. DO NOT use the symbol //,$ and word in the expression.

Task: Rewrite the following word problems into Symbolic Form trying to do like the given example.
Your output should be in the following format:
Word Problem: <Given WordProblem>
Define the variables and formulate the inequality:<Your created inequality>
Symbolic Form: <Transformed inequality to Symbolic Form>

Word Problem: What numbers satisfy the condition: nine less than negative four times a number is strictly greater than negative one?
Define the variables and formulate the inequality:
Let denote the number by variable x.
"nine less than negative four times a number" can be represented as: -4*x - 9 
"is strictly greater than negative one" can be represented as: -4*x - 9 > -1 
Inequality: -4*x - 9 > -1 
Symbolic Form: [[-4*x - 9, > , -1 , x , solve]] 

Word Problem:Brice has $30 to take his brother and his friends to the movies. If each ticket costs $4.00, and he must buy tickets for himself and his brother, what is the greatest number of friends he can invite?
Define the variables and formulate the inequality:
Let denote the number of friends Brice can invite by variable f. 
"each ticket costs $4.00" can be represented as: 4*f 
"he must buy tickets for himself and his brother" can be represented as: 4*2 
"has $30 to take his brother and his friends to the movies" can be represented as: 4*2 + 4*f <= 30 
Inequality: 4*2 + 4*f <= 30 
Symbolic Form: [[4*2 + 4*f, <= , 30 , f , solve]] 

Word Problem: Allison practices her violin for at least 12 hours per week. She practices for three fourths of an hou reach session. If Allison has already practiced 3 hours this week, how many more sessions remain for her to meet or exceed her weekly practice goal?
Define the variables and formulate the inequality:
Let denote the number of sessions by variable s.
"Allison practices her violin for at least 12 hours per week" can be represented as: 12
"practices for three fourths of an hou reach session" can be represented as: 3/4
"has already practiced 3 hours this week" can be represented as: 3
Inequality: 3 + (3/4)*s >= 12
Symbolic Form: [[3 + (3/4)*s, >= , 12 , s , solve]]

Word Problem:The elevator in Yehires apartment building has a sign that says the maximum weight is 2,100 pounds. If the average weight of one person is 150 pounds, how many people can safely ride the elevator?
Define the variables and formulate the inequality:
Let denote the number of people by variable p.
"maximum weight is 2,100 pounds" can be represented as: 150*p <= 2100
Inequality: 150*p <= 2100
Symbolic Form: [[150*p, <= , 2100 , p , solve]]

Word Problem: Brenda has $500 in her bank account.  Every week, she withdraws $40 for expenses.  Without making any deposits, how many weeks can she withdraw this money if she wants to maintain a balance of at least $200? 
Define the variables and formulate the inequality:
Let denote the number of weeks by variable w. 
"Every week, she withdraws $40 for expenses" can be represented as: 40*w 
"she wants to maintain a balance of at least $200" can be represented as: 500 - 40*w >= 200 
Inequality: 500 - 40*w >= 200 
Symbolic Form: [[500 - 40*w, >= , 200 , w , solve]] 


Word Problem: What numbers satisfy the condition: seven more than two-thirds of a number is strictly less than thirty?
Define the variables and formulate the inequality:
Let denote the number by variable y.
"seven more than two-thirds of a number" can be represented as: 2/3*y + 7
"is strictly less than thirty" so it became: 2/3*y + 7 < 30
Inequality: 2/3*y + 7 < 30
Symbolic Form: [[2/3*y + 7, < , 30 , y , solve]]

Word Problem:Five student government officers want to go to the state convention. It will cost them $110 for registration, $375 for transportation and food, and $42 per person for the hotel. There is $450 budgeted for the convention in the student government savings account. They can earn the rest of the money they need by having a car wash. If they charge $5 per car, how many cars must they wash in order to have enough money to pay for the trip?
Define the variables and formulate the inequality:
Let denote the number of cars they must wash by variable c.
"It will cost them $110 for registration, $375 for transportation and food, and $42 per person for the hotel" can be represented as: 110 + 375 + 42*5
"There is $450 budgeted for the convention in the student government savings account" so it became: 110 + 375 + 42*5 - 450
"They can earn the rest of the money they need by having a car wash and charge $5 per car" can be represented as: 5*c
Inequality: 5*c >= 110 + 375 + 42*5 - 450
Symbolic Form: [[5*c - 110 - 375 - 42*5 + 450 >= 0, c , solve]]

Word Problem:
""".strip()


Word_Problem_Compound_Inequalities =  """
I want you to act as Math Teacher. Your goal is to rewrite a given problem into a Symbolic Form.
You must followed these principles:
1. Do not solve the problem. 
2. Symbolic Form is written in the form of [[expression, expression, variable, variable, solve]] and wrap by [[]]. 
3. There MUST be * between the coefficient and the variable. Example: 2*x + 3 > 7. 
4. DO NOT use the symbol //,$ and word in the expression.

Task: Rewrite the following word problems into Symbolic Form trying to do like the given example.
Your output should be in the following format:
Word Problem: <Given WordProblem>
Define the variables and formulate the compound inequality:<Your created compound inequality>
Symbolic Form: <Transformed compound inequality to Symbolic Form>

Word Problem: A square plot of land is being prepared for planting. The perimeter of the plot must be between 40 meters and 60 meters inclusively. Find the range of possible side lengths for the square plot.
Define the variables and formulate the compound inequality:
Let denote the side length of the square plot by variable s.
"perimeter of the plot must be between 40 meters and 60 meters inclusively" can be represented as: 40 <= 4*s <= 60
Compound Inequality: 40 <= 4*s <= 60
Symbolic Form: [[4*s - 40 >= 0, 4*s - 60 <= 0 , s , solve]]

Word Problem: A number is at least 5 and at most 15. Write a compound inequality that shows the range of numbers that satisfy this condition.
Define the variables and formulate the compound inequality:
Let denote the number by variable x.
"at least 5" can be represented as: x >= 5
"at most 15" can be represented as: x <= 15
Compound Inequality: 5 <= x <= 15
Symbolic Form: [[x - 5 >= 0, x - 15 <= 0 , x , solve]]

Word Problem: Every tiger, can eat 15% to 25% of his bodyweight, each week inclusive.  If  a tiger weighs 300, write an inequality that represents the amount of food the tiger can eat in pounds.
Define the variables and formulate the compound inequality:
Let denote the amount of food the tiger can eat in pounds by variable f.
"can eat 15% to 25% of his bodyweight" can be represented as: 0.15*300 <= f <= 0.25*300
Compound Inequality: 45 <= f <= 75
Symbolic Form: [[f - 45 >= 0, f - 75 <= 0 , f , solve]]

Word Problem: Maria is saving money to buy a new laptop. The laptops she is considering cost between $500 and $800. She has already saved $150 and her parents have agreed to contribute up to $200 towards the purchase. How much Maria can expect to save to buy the laptop?
Define the variables and formulate the compound inequality:
Let denote the amount of money Maria needs to save by variable m.
"The laptops she is considering cost between $500 and $800" can be represented as: 500 <= m <= 800
"She has already saved $150" so it became : 500 <= m + 150 <= 800
"her parents have agreed to contribute up to $200 towards the purchase" so it became : 500 <= m + 150 + 200 <= 800
Compound Inequality: 500 <= m + 150 + 200 <= 800
Symbolic Form: [[m + 150 + 200 - 500 >= 0, m + 150 + 200 - 800 <= 0 , m , solve]]

Word Problem: A ski shop carries skis that are between 150 and 220cm long. They recommend that the skis be 1.25 longer than your height.Calculate the tallest height that a person can be and still rent skis from the shop.
Define the variables and formulate the compound inequality:
Let denote the height of the person by variable h.
"skis that are between 150 and 220cm long" can be represented as: 150 <= h*1.25 <= 220
Compound Inequality: 150 <= h*1.25 <= 220
Symbolic Form: [[h*1.25 - 150 >= 0, h*1.25 - 220 <= 0 , h , solve]]

Word Problem:Your family needs 2 gallons of water this week, but you don't want to buy any more than 8 gallons. Write an inequality representing the possible gallons of water you could buy this week.
Define the variables and formulate the compound inequality:
Let denote the gallons of water you could buy this week by variable g.
"needs 2 gallons of water this week" can be represented as: 2 <= g
"don't want to buy any more than 8 gallons" can be represented as: g <= 8
Compound Inequality: 2 <= g <= 8
Symbolic Form: [[g - 2 >= 0, g - 8 <= 0 , g , solve]]

Word Problem:A local energy company has introduced a new billing system to encourage energy conservation. The system has three tiers: Eco-Friendly Usage, Standard Usage, and High Usage. The usage is measured in kilowatt-hours (kWh). During the summer months, a customer will pay a base fee of $15.50 plus $0.12 per kWh for Eco-Friendly Usage. The bill for Eco-Friendly Usage would be between or equal to $21.50 and $39.50. How many kWh can the customer use if they want their usage to stay in the Eco-Friendly range?
Define the variables and formulate the compound inequality:
Let denote the usage in kWh by variable u.
"base fee of $15.50 plus $0.12 per kWh for Eco-Friendly Usage" can be represented as: 15.50 + 0.12*u
"bill for Eco-Friendly Usage would be between or equal to $21.50 and $39.50" can be represented as: 21.50 <= 15.50 + 0.12*u <= 39.50
Compound Inequality: 21.50 <= 15.50 + 0.12*u <= 39.50
Symbolic Form: [[15.50 + 0.12*u - 21.50 >= 0, 15.50 + 0.12*u - 39.50 <= 0 , u , solve]]

Word Problem:
""".strip()


Inequalities_Basic_Prompt = """
I want you to act as Math Teacher. Your goal is to rewrite a given problem into a Symbolic Form.
You must followed these principles:
1. Do not solve the problem. 
2. Symbolic Form is written in the form of [[expression, expression, variable, variable, solve]] and wrap by [[]]. 
3. There MUST be * between the coefficient and the variable. Example: 2*x + 3 > 7. 
4. DO NOT use the symbol //,$ and word in the expression.

Task: Rewrite the following inequalities into Symbolic Form trying to do like the given example.
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

Question:
"""

Compound_Inequalities_Basic_Prompt = """
I want you to act as Math Teacher. Your goal is to rewrite a given problem into a Symbolic Form.
You must followed these principles:
1. Do not solve the problem. 
2. Symbolic Form is written in the form of [[expression, expression, variable, variable, solve]] and wrap by [[]]. 
3. There MUST be * between the coefficient and the variable. Example: 2*x + 3 > 7. 
4. DO NOT use the symbol //,$ and word in the expression.

Task: Rewrite the following compound inequalities into Symbolic Form trying to do like the given example.
Question:Solve this compound inequalities:  4*y -17 < 19 and -39*y  <= -47 
Symbolic Form: [[4*y -17  -19 < 0, -39*y  + 47 <= 0, y, solve]]

Question: Solve this compound inequalities:  -18 < 6*z + 18 < 17 
Symbolic Form: [[6*z + 18 + 18 > 0, 6*z + 18  -17 < 0, z, solve]]

Question: Solve this compound inequalities: 12*y -3 > 9 and 4*y  < 7 
Symbolic Form: [[12*y -3 -9 > 0, 4*y  -7 < 0, x, solve]]

Question: Solve this compound inequalities: 3 < x -72 < 7 
Symbolic Form: [[x -72 -3 > 0, x -72 -7 < 0, x, solve]]

Question:Solve this compound inequalities: 3 < x -72 < 7 
Symbolic Form: [[x -72 -3 > 0, x -72 -7 < 0, x, solve]]

Question:Solve this compound inequalities: 12*y -3 > 9 and 4*y  < 7 
Symbolic Form: [[12*y -3 -9 > 0, 4*y  -7 < 0, x, solve]]

Question:Solve this compound inequalities:  -43 <= -5*z + 457 <= 33 
Symbolic Form: [[-5*z + 457 + 43 >= 0, -5*z + 457  -33 <= 0, z, solve]]

Question:
"""