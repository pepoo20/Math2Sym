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

temp = """
Word Problem: Bryan wants to make peppermint stick pickles for his friends. The snack is made by inserting a peppermint stick into the middle of a pickle. If a peppermint stick costs $0.40 and a pickle costs $2.30,what is greatest number of peppermint stick pickles Bryan can make if he has $20 to buy the ingredients?
Define the variables and formulate the inequality:
Let denote the number of peppermint stick pickles Bryan can make by variable p. 
"peppermint stick costs $0.40" can be represented as: 0.40*p 
"pickle costs $2.30" can be represented as: 2.30p 
"he has $20 to buy the ingredients" can be represented as: 0.40*p + 2.30*p <= 20 
Inequality: 0.40*p + 2.30*p <= 20 
Symbolic Form: [[0.40*p + 2.30*p, <= , 20 , p , solve]]

Word Problem: A car rental company charges $25 per day to rent a car. If a customer has $200 to spend on a rental, how many days can the customer rent the car?
Define the variables and formulate the inequality:
Let denote the number of days by variable d.
"charges $25 per day to rent a car" can be represented as: 25*d
"has $200 to spend on a rental" can be represented as: 25*d <= 200
Inequality: 25*d <= 200
Symbolic Form: [[25*d, <= , 200 , d , solve]]

"""
Word_Problem_Compound_Inequalities =  """
Task: Rewrite the following word problems into Symbolic Form trying to do like the given example.
Your output should be in the following format:
Word Problem: <Given WordProblem>
Define the variables and formulate the compound inequality:<Your created compound inequality>
Symbolic Form: <Transformed compound inequality to Symbolic Form>


Word Problem: Mia is a baker who wants to make a profit of at least $200 but no more than $300 on a large order of cupcakes for a wedding. She has already spent $150 on ingredients and the decorations. Each cupcake she sells will bring in a profit of $2. How many cupcakes does Mia need to sell to make her desired profit?
Define the variables and formulate the compound inequality:
Let denote the number of cupcakes Mia needs to sell by variable c.
"She has already spent $150 on ingredients and the decorations" can be represented as: $150
"Each cupcake she sells will bring in a profit of $2" can be represented as: 2*c
"Mia wants to make a profit of at least $200 but no more than $300" can be represented as: $200 <= (2*c - $150) <= $300
Compound Inequality: 200 <= (2*c - 150) <= 300
Symbolic Form: [[(2*c - 150) - 200 >= 0, (2*c - 150) - 300 <= 0 , c , solve]]

Word Problem: A number is at least 5 and at most 15. Write a compound inequality that shows the range of numbers that satisfy this condition.
Define the variables and formulate the compound inequality:
Let denote the number by variable x.
"at least 5" can be represented as: x >= 5
"at most 15" can be represented as: x <= 15
Compound Inequality: 5 <= x <= 15
Symbolic Form: [[x - 5 >= 0, x - 15 <= 0 , x , solve]]

Word Problem: Ralph needs to earn a B in his Geology class. His current test scores are 91, 79. His final exam is worth 4 test scores. In order to earn a B Ralph's average must lie between 80 and 89 inclusive. What range of scores can Ralph receive on the final exam to earn a B in the course?
Define the variables and formulate the compound inequality:
Let denote the score on the final exam by variable f.
"His current test scores are 91, 79" can be represented as: (91 + 79) = 170
"His final exam is worth 4 test scores" can be represented as: 4*f
"Ralph's average must lie between 80 and 89 inclusive" can be represented as: 80 <= (170 + 4*f)/6 <= 89
Compound Inequality: 80 <= (170 + 4*f)/6 <= 89
Symbolic Form: [[(170 + 4*f)/6 - 80 >= 0, (170 + 4*f)/6 - 89 <= 0 , f , solve]]

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

Word Problem: An electronics store is giving a $50 discount coupon for all smart watches. Emma is considering various smart watches with prices ranging from $220 to $310. How much can she anticipate to pay after applying the discount coupon?
Define the variables and formulate the compound inequality:
Let denote the price of the smart watch by variable p.
"prices ranging from $220 to $310" can be represented as: 220 <= p <= 310
"store is giving a $50 discount coupon for all smart watches" can be represented as: 220 <= p + 50 <= 310
Compound Inequality: 220 <= p + 50 <= 310
Symbolic Form: [[p + 50 - 220 >= 0, p + 50 - 310 <= 0 , p , solve]]

Word Problem:A local energy company has introduced a new billing system to encourage energy conservation. The system has three tiers: Eco-Friendly Usage, Standard Usage, and High Usage. The usage is measured in kilowatt-hours (kWh). During the summer months, a customer will pay a base fee of $15.50 plus $0.12 per kWh for Eco-Friendly Usage. The bill for Eco-Friendly Usage would be between or equal to $21.50 and $39.50. How many kWh can the customer use if they want their usage to stay in the Eco-Friendly range?
Define the variables and formulate the compound inequality:
Let denote the usage in kWh by variable u.
"base fee of $15.50 plus $0.12 per kWh for Eco-Friendly Usage" can be represented as: 15.50 + 0.12*u
"bill for Eco-Friendly Usage would be between or equal to $21.50 and $39.50" can be represented as: 21.50 <= 15.50 + 0.12*u <= 39.50
Compound Inequality: 21.50 <= 15.50 + 0.12*u <= 39.50
Symbolic Form: [[15.50 + 0.12*u - 21.50 >= 0, 15.50 + 0.12*u - 39.50 <= 0 , u , solve]]

Word Problem:
""".strip()


TEMP= """
inputs:
Solve this compound inequalities: 7*x + 4 > 10 and 3*x -6 < 6 
Symbolic Form: [[7*x + 4 -10 > 0, 3*x -6 -6 < 0, x, solve]]<|endoftext|>Inequality: 12*x + 0 <= 16*x  -36
Symbolic Form: [[12*x + 0, <= , 16*x  -36 , x , solve]]<|endoftext|>

Word Problem:Your family needs 2 gallons of water this week, but you don't want to buy any more than 8 gallons. Write an inequality representing the possible gallons of water you could buy this week.
Define the variables and formulate the compound inequality:
Let denote the gallons of water you could buy this week by variable g.
"needs 2 gallons of water this week" can be represented as: 2 <= g
"don't want to buy any more than 8 gallons" can be represented as: g <= 8
Compound Inequality: 2 <= g <= 8
Symbolic Form: [[g - 2 >= 0, g - 8 <= 0 , g , solve]]

Word Problem: Every tiger, can eat 15% to 25% of his bodyweight, each week inclusive.  If  a tiger weighs 300, write an inequality that represents the amount of food the tiger can eat in pounds.
Define the variables and formulate the compound inequality:
Let denote the amount of food the tiger can eat in pounds by variable f.
"can eat 15% to 25% of his bodyweight" can be represented as: 0.15*300 <= f <= 0.25*300
Compound Inequality: 45 <= f <= 75
Symbolic Form: [[f - 45 >= 0, f - 75 <= 0 , f , solve]]

Word Problem: Maria is baking cookies for a school event. She has already baked 23 cookies. She plans to bake one big batch of cookies that will produce 4 times the amount she has already baked. To have enough cookies for everyone, she needs to have a total of at least 120 but no more than 150 cookies. What range of cookies can Maria bake in her big batch to have enough for the event?

Define the variables and formulate the compound inequality:
Let denote the number of cookies in the big batch by variable b.
"She has already baked 23 cookies" can be represented as: 23
"She plans to bake one big batch of cookies that will produce 4 times the amount she has already baked" can be represented as: 4*23 = 92, so the big batch contains b = 92 cookies.
"To have enough cookies for everyone, she needs to have a total of at least 120 but no more than 150 cookies" can be represented as: 120 <= 23 + b <= 150

Compound Inequality: 120 <= 23 + 92b <= 150
Symbolic Form: [[120 - 23 - 92b <= 0, 150 - 23 - 92*b >= 0 , b , solve]]

Word Problem: Mia is a baker who wants to make a profit of at least $200 but no more than $300 on a large order of cupcakes for a wedding. She has already spent $150 on ingredients and the decorations. Each cupcake she sells will bring in a profit of $2. How many cupcakes does Mia need to sell to make her desired profit?
Define the variables and formulate the compound inequality:
Let denote the number of cupcakes Mia needs to sell by variable c.
"She has already spent $150 on ingredients and the decorations" can be represented as: $150
"Each cupcake she sells will bring in a profit of $2" can be represented as: 2c
"Mia wants to make a profit of at least $200 but no more than $300" can be represented as: $200 <= (2c - $150) <= $300
Compound Inequality: 200 <= (2c - 150) <= 300
Symbolic Form: [[(2*c - 150) - 200 >= 0, (2c - 150) - 300 <= 0 , c , solve]]

Word Problem:Your family needs 2 gallons of water this week, but you don't want to buy any more than 8 gallons. Write an inequality representing the possible gallons of water you could buy this week.
Define the variables and formulate the compound inequality:
Let denote the gallons of water you could buy this week by variable g.
"needs 2 gallons of water this week" can be represented as: 2 <= g
"don't want to buy any more than 8 gallons" can be represented as: g <= 8
Compound Inequality: 2 <= g <= 8
Symbolic Form: [[g - 2 >= 0, g - 8 <= 0 , g , solve]]

Word Problem: A ski shop carries skis that are between 150 and 220cm long. They recommend that the skis be 1.25 longer than your height.Calculate the tallest height that a person can be and still rent skis from the shop.
Define the variables and formulate the compound inequality:
Let denote the height of the person by variable h.
"skis that are between 150 and 220cm long" can be represented as: 150 <= h*1.25 <= 220
Compound Inequality: 150 <= h*1.25 <= 220
Symbolic Form: [[h*1.25 - 150 >= 0, h*1.25 - 220 <= 0 , h , solve]]

Word Problem: A square plot of land is being prepared for planting. The perimeter of the plot must be between 40 meters and 60 meters inclusively. Find the range of possible side lengths for the square plot.
Define the variables and formulate the compound inequality:
Let denote the side length of the square plot by variable s.
"perimeter of the plot must be between 40 meters and 60 meters inclusively" can be represented as: 40 <= 4*s <= 60
Compound Inequality: 40 <= 4*s <= 60
Symbolic Form: [[4*s - 40 >= 0, 4*s - 60 <= 0 , s , solve]]

Word Problem: 
"""

Inequalities_Basic_Prompt = """
Task: Rewrite the following inequalities into Symbolic Form trying to do like the given example.
Question: Inequality: 9*x + 16 <= 3*x  -20
Symbolic Form: [[9*x + 16, <= , 3*x  -20 , x , solve]]

Question:Inequality: -32*x  -18 < -37*x  -3
Symbolic Form: [[-32*x  -18, < , -37*x  -3 , x , solve]]

Question:Solve the inequality: -7*y  -32 <= -6*y 
Symbolic Form : [[-7*y -32, <= , -6*y  , y, solve]]

Question:
"""

Compound_Inequalities_Basic_Prompt = """
Task: Rewrite the following compound inequalities into Symbolic Form trying to do like the given example.
Question:Solve this compound inequalities:  4*y -17 < 19 and -39*y  <= -47 
Symbolic Form: [[4*y -17  -19 < 0, -39*y  + 47 <= 0, y, solve]]

Question: Solve this compound inequalities:  -18 < 6*z + 18 < 17 
Symbolic Form: [[6*z + 18 + 18 > 0, 6*z + 18  -17 < 0, z, solve]]

Question: Solve this compound inequalities: 12*y -3 > 9 and 4*y  < 7 
Symbolic Form: [[12*y -3 -9 > 0, 4*y  -7 < 0, x, solve]]

Question: Solve this compound inequalities: 3 < x -72 < 7 
Symbolic Form: [[x -72 -3 > 0, x -72 -7 < 0, x, solve]]

Question:
"""