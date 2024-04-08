Math_Teacher_Prompt = """I want you to act as Math Teacher. Your goal is to rewrite a given problem into a Symbolic Form.
You must follow these principles:
1. Do not solve the linear system.
2. Symbolic Form is written in the form of [[expression, expression, variable, variable, solve]] and wrap by [[]]. 
3. There MUST be * between the coefficient and the variable. Example: 2*(2*x + 3) -7. 
4. DO NOT use the symbol //,$ and word in the expression.

Your output should be in the following format:
Word Problem: <Given WordProblem>
Define the variables and formulate the linear system of equations: <Your created linear system of equations>
Symbolic Form: <Transformed linear system of equations to symbolic form>


""".strip()

WordProblem_SystemEquations = Math_Teacher_Prompt + """

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
The total amount of the two loans is $85,000. So the equation is x + y = 85,000.
This year, the business expects to pay $4,650 in interest on the two loans. So the equation is 0.06*x + 0.045*y = 4,650.
System of equations: {x + y = 85,000, 0.06*x + 0.045*y = 4,650}
Symbolic Form: [[x + y - 85,000, 0.06*x + 0.045*y - 4,650, x, y, solve]]

"""

Temp_Problem = """
1
Word Problem:  Two numbers have a sum of 50. One number is 10 more than the other. What are the two numbers?
Define the variables and formulate the linear system of equations:
Let variable x represent the first number and variable y represent the second number.
The sum of the two numbers is 50. So the equation is x + y = 50.
One number is 10 more than the other. So the equation is x - y = 10.
System of equations: {x + y = 50, x - y = 10}
Symbolic Form: [[x + y - 50, x - y - 10, x, y, solve]]

2.
Word Problem:  At the end of the 2000 NBA regular season, the Houston comets had 22 more victories than losses. The number of victories they had was three less than six time the number of losses. How many regular season games did the Houston comets play during the 2000 NBA season?
Define the variables and formulate the linear system of equations:
Let variable x represent the number of victories and variable y represent the number of losses.
The Houston comets had 22 more victories than losses. So the equation is x - y = 22.
The number of victories they had was three less than six time the number of losses. So the equation is x = 6*y - 3.
System of equations: {x - y = 22, x = 6*y - 3}
Symbolic Form: [[x - y - 22, x - 6*y + 3, x, y, solve]]

3.

Word Problem: A total of 1,595 first- and second-year college students gathered at a pep rally. The number of freshmen exceeded the number of sophomores by 15 . How many freshmen and sophomores were in attendance?
Define the variables and formulate the linear system of equations:
Let variable x represent the number of freshmen and variable y represent the number of sophomores.
The total number of students is 1,595. So the equation is x + y = 1595.
The number of freshmen exceeded the number of sophomores by 15. So the equation is x - y = 15.
System of equations: {x + y = 1595, x - y = 15}
Symbolic Form: [[x + y - 1595, x - y - 15, x, y, solve]]

4.
Word Problem:How much cleaning fluid concentrate, with  60% alcohol content, must be mixed with water to obtain a  24-ounce mixture with  15% alcohol content?
Define the variables and formulate the linear system of equations:
Let variable x represent the amount of cleaning fluid concentrate (60% alcohol content) and variable y represent the amount of water.
The total volume of the mixture is 24 ounces. So the equation is x + y = 24.
The resulting mixture has 15% alcohol content. So the total amount of alcohol in the mixture is 0.15*24 = 3.6 ounces.
The amount of alcohol in the cleaning fluid concentrate is 0.60*x.
Since only cleaning fluid concentrate and water are mixed,the total amount of alcohol must come from these two sources. So the equation is 0.60*x + 0*y = 3.6.
System of equations: {x + y = 24, 0.60*x + 0*y = 3.6}
Symbolic Form: [[x + y - 24, 0.60*x + 0*y - 3.6, x, y, solve]]

5.
Word Problem: A store sells oranges and apples. Oranges cost $1.00 each and apples cost $2.00 each. In the first sale of the day, 15 fruits were sold in total, and the price was $25. How many of each type of frust was sold?
Define the variables and formulate the linear system of equations:
Let variable x represent the number of oranges sold and variable y represent the number of apples sold.
"Oranges cost $1.00 each" so the cost of x oranges is 1*x.
"Apples cost $2.00 each" so the cost of y apples is 2*y.
The total cost of the fruits sold is $25.00. So the equation is 1*x + 2*y = 25.
The total number of fruits sold is 15. So the equation is x + y = 15.
System of equations: {1*x + 2*y = 25, x + y = 15}
Symbolic Form: [[1*x + 2*y - 25, x + y - 15, x, y, solve]] 

6.

Word Problem:The Slytherin and the Gryffindor are going to the Pizza Palace for dinner. The Slytherin order 3 slices of pizza and 3 colas and have a bill that totals $15. The Gryffindor order 4 slices of pizza and 3 colas and have a bill that totals $18. How much does a slice of pizza and a cola cost?
Define the variables and formulate the linear system of equations:
Let variable x represent the cost of a slice of pizza and variable y represent the cost of a cola.
The Slytherin order 3 slices of pizza and 3 colas and have a bill that totals $15. So the equation is 3*x + 3*y = 15.
The Gryffindor order 4 slices of pizza and 3 colas and have a bill that totals $18. So the equation is 4*x + 3*y = 18.
System of equations: {3*x + 3*y = 15, 4*x + 3*y = 18}
Symbolic Form: [[3*x + 3*y - 15, 4*x + 3*y - 18, x, y, solve]]

7.
Word Problem:The price, e, of an entertainment system at Extreme Electronics is $220 less than twice the price, u, of the same system at Ultra Electronics. The difference in price between the system at Extreme Electronics and Ultra Electronics is $175. What is the price of the system at each store?
Define the variables and formulate the linear system of equations:
Let variable x represent the price of the system at Extreme Electronics and variable y represent the price of the system at Ultra Electronics.
The price, e, of an entertainment system at Extreme Electronics is $220 less than twice the price, u, of the same system at Ultra Electronics. So the equation is x = 2*y - 220.
The difference in price between the system at Extreme Electronics and Ultra Electronics is $175. So the equation is x - y = 175.
System of equations: {x = 2*y - 220, x - y = 175}
Symbolic Form: [[x - 2*y + 220, x - y - 175, x, y, solve]]

8.
Word Problem:It takes three hours for a boat to go 18 miles downstream, and nine hours to return. What is the rate of the boat in calm water and the rate of the current?
Define the variables and formulate the linear system of equations:
Let variable x represent the rate of the boat in calm water and variable y represent the rate of the current.
The rate of the boat in calm water is x and the rate of the current is y. The distance is 18 miles.
The time it takes to go 18 miles downstream is 3 hours. So the equation is x + y = 18/3.
The time it takes to return is 9 hours. So the equation is x - y = 18/9.
System of equations: {x + y = 18/3, x - y = 18/9}
Symbolic Form: [[x + y - 18/3, x - y - 18/9, x, y, solve]]

9.

Word Problem:At a restaurant the cost for a breakfast taco and a small glass of milk is $2.10. The cost for 2 tacos and 3 small glasses of milk is $5.15. Which pair of equations can be used to determine t, the cost of a taco, and m, the cost of a small glass of milk? 
Define the variables and formulate the linear system of equations:
Let variable t represent the cost of a breakfast taco and variable m represent the cost of a small glass of milk. 
The cost for a breakfast taco and a small glass of milk is $2.10. So the equation is t + m = 2.10. 
The cost for 2 tacos and 3 small glasses of milk is $5.15. So the equation is 2*t + 3*m = 5.15. 
System of equations: {t + m = 2.10, 2*t + 3*m = 5.15} 
Symbolic Form: [[t + m - 2.10, 2*t + 3*m - 5.15, t, m, solve]]

10.
Word Problem: You and a friend go to Tacos Galore for lunch. You order three soft tacos and three burritos and your total bill is $11.25. Your friend's bill is $10.00 for four soft tacos and two burritos. How much do soft tacos cost? How much do burritos cost? 
Define the variables and formulate the linear system of equations:
Let variable t represent the cost of a soft taco and variable b represent the cost of a burrito. 
You order three soft tacos and three burritos and your total bill is $11.25. So the equation is 3*t + 3*b = 11.25. 
Your friend's bill is $10.00 for four soft tacos and two burritos. So the equation is 4*t + 2*b = 10.00. 
System of equations: {3*t + 3*b = 11.25, 4*t + 2*b = 10.00} 
Symbolic Form: [[3*t + 3*b - 11.25, 4*t + 2*b - 10.00, t, b, solve]]

11.
Word Problem: The length of a rectangle is equal to triple the width. Which system of equations can be
used to find the dimensions of the rectangle if the perimeter is 86 centimeters?
Define the variables and formulate the linear system of equations:
Let variable x represent the length of the rectangle and variable y represent the width of the rectangle. 
The length of a rectangle is equal to triple the width. So the equation is x = 3*y. 
The perimeter of the rectangle is 86 centimeters. So the equation is 2*x + 2*y = 86. 
System of equations: {x = 3*y, 2*x + 2*y = 86} 
Symbolic Form: [[x - 3*y, 2*x + 2*y - 86, x, y, solve]]

12.
Word Problem:A baker sells plain cakes for $7 and decorated cakes for $11. On a busy Saturday the baker started with 120 cakes, and sold all but three. His takings for the day were $991. How many plain cakes did he sell that day, and how many were decorated before they were sold? 
Define the variables and formulate the linear system of equations:
Let variable x represent the number of plain cakes sold and variable y represent the number of decorated cakes sold. 
The baker started with 120 cakes, and sold all but three. So the equation is x + y = 120 - 3. 
The baker sells plain cakes for $7 and decorated cakes for $11. So the equation is 7*x + 11*y = 991. 
System of equations: {x + y = 120 - 3, 7*x + 11*y = 991} 
Symbolic Form: [[x + y - 120 + 3, 7*x + 11*y - 991, x, y, solve]]

13. 
Word Problem: Two small pitchers and one large pitcher can hold 8 cups of water. One large pitcher minus one small pitcher constitutes 2 cups of water. How many cups of water can each pitcher hold?
Define the variables and formulate the linear system of equations:
Let variable x represent the number of cups of water a small pitcher can hold and variable y represent the number of cups of water a large pitcher can hold.
Two small pitchers and one large pitcher can hold 8 cups of water. So the equation is 2*x + 1*y = 8.
One large pitcher minus one small pitcher constitutes 2 cups of water. So the equation is y - x = 2.
System of equations: {2*x + 1*y = 8, y - x = 2}
Symbolic Form: [[2*x + 1*y - 8, y - x - 2, x, y, solve]]

14.
Word Problem: Since my uncles farmyard appears to be overrun with dogs, and chickens, I asked him how many of each he had. He responded that his dogs and chickens had a total of 148 legs and 60 heads. How many dogs and how many chickens does my uncle have?
Define the variables and formulate the linear system of equations:
Let variable x represent the number of dogs and variable y represent the number of chickens.
The total number of legs is 148. So the equation is 4*x + 2*y = 148.
The total number of heads is 60. So the equation is x + y = 60.
System of equations: {4*x + 2*y = 148, x + y = 60}
Symbolic Form: [[4*x + 2*y - 148, x + y - 60, x, y, solve]]

15. 
Word Problem: Emma and Liam are saving money. Emma starts with $80 and saves $10 per week. Liam starts with $120 and saves $6 per week. After how many weeks will they have the same amount of money?
Let variable x represent the number of weeks to have the same amount of money as variable y represent the amount of money. 
The amount of money Emma starts with is $80. So the equation is 80 + 10*x = y. 
The amount of money Liam starts with is $120. So the equation is 120 + 6*x = y. 
System of equations: {80 + 10*x = y, 120 + 6*x = y} 
Symbolic Form: [[80 + 10*x - y, 120 + 6*x - y, x, y, solve]]

16.
Word Problem: The state fair is a popular field trip destination. This year the senior class at High School A and the senior class at High School B both planned trips there. The senior class at High School A rented and filled 8 vans and 8 buses with 240 students. High School B rented and filled 4 vans and 1 bus with 54 students. Every van had the same number of students in it as did the buses. Find the number of students in each van and in each bus.
Define the variables and formulate the linear system of equations:
Let variable x represent the number of students in each van and variable y represent the number of students in each bus.
The senior class at High School A rented and filled 8 vans and 8 buses with 240 students. So the equation is 8*x + 8*y = 240.
High School B rented and filled 4 vans and 1 bus with 54 students. So the equation is 4*x + 1*y = 54.
System of equations: {8*x + 8*y = 240, 4*x + 1*y = 54}
Symbolic Form: [[8*x + 8*y - 240, 4*x + 1*y - 54, x, y, solve]]

17.
Word Problem: Mr.Chandra bought 2 lbs. of cheddar cheese and 3 lbs. of chicken loaf. He paid $26.35. Mrs.Houston paid $18.35 for 1.5 lbs. of cheese, and 2 lbs. of chicken loaf. What was the price per pound of each item?
Define the variables and formulate the linear system of equations:
Let variable x represent the price per pound of cheddar cheese and variable y represent the price per pound of chicken loaf.
Mr.Chandra bought 2 lbs. of cheddar cheese and 3 lbs. of chicken loaf. So the equation is 2*x + 3*y = 26.35.
Mrs.Houston paid $18.35 for 1.5 lbs. of cheese, and 2 lbs. of chicken loaf. So the equation is 1.5*x + 2*y = 18.35.
System of equations: {2*x + 3*y = 26.35, 1.5*x + 2*y = 18.35}
Symbolic Form: [[2*x + 3*y - 26.35, 1.5*x + 2*y - 18.35, x, y, solve]]

18.
Word Problem: A farmer raises both chickens and pigs on his farm. He counts a total of 30 heads and 90 legs among the animals in his barn. Assuming that each chicken has one head and two legs, while each pig has one head and four legs, how many chickens and how many pigs does the farmer have?
Define the variables and formulate the linear system of equations:
Let variable x represent the number of chickens and variable y represent the number of pigs.
The total number of heads is 30. So the equation is x + y = 30.
The total number of legs is 90. So the equation is 2*x + 4*y = 90.
System of equations: {x + y = 30, 2*x + 4*y = 90}
Symbolic Form: [[x + y - 30, 2*x + 4*y - 90, x, y, solve]]

19.
Word Problem: A bookstore sells both hardcover and paperback books. The hardcover books are priced at $25 each and the paperback books are priced at $15 each. On a particular day, the bookstore sold a total of 100 books and made a total revenue of $2250. How many hardcover and paperback books were sold?
Define the variables and formulate the linear system of equations:
Let variable x represent the number of hardcover books sold and variable y represent the number of paperback books sold.
The hardcover books are priced at $25 each. So the equation is 25*x.
The paperback books are priced at $15 each. So the equation is 15*y.
The total number of books sold is 100. So the equation is x + y = 100.
The total revenue is $2250. So the equation is 25*x + 15*y = 2250.
System of equations: {x + y = 100, 25*x + 15*y = 2250}
Symbolic Form: [[x + y - 100, 25*x + 15*y - 2250, x, y, solve]]

20.
Word Problem: A gardener sells rose plants and tulip plants. The rose plants are priced at $20 each and the tulip plants are priced at $15 each. On a particular day, the gardener sold a total of 50 plants and made a total revenue of $800. How many rose and tulip plants were sold?
Define the variables and formulate the linear system of equations:
Let variable x represent the number of rose plants sold and variable y represent the number of tulip plants sold.
The rose plants are priced at $20 each. So the equation is 20*x.
The tulip plants are priced at $15 each. So the equation is 15*y.
The total number of plants sold is 50. So the equation is x + y = 50.
The total revenue is $800. So the equation is 20*x + 15*y = 800.
System of equations: {x + y = 50, 20*x + 15*y = 800}
Symbolic Form: [[x + y - 50, 20*x + 15*y - 800, x, y, solve]]

21. 
Word Problem: The Rocket Coaster has 15 cars, some that hold 4 people and some that hold 6 people.There is room for 72 people. How many 4-person cars and how many 6-person cars are there?

Define the variables and formulate the linear system of equations:
Let variable x represent the number of 4-person cars and variable y represent the number of 6-person cars.
The total number of cars is 15. So the equation is x + y = 15.
The total number of people is 72. So the equation is 4*x + 6*y = 72.
System of equations: {x + y = 15, 4*x + 6*y = 72}
Symbolic Form: [[x + y - 15, 4*x + 6*y - 72, x, y, solve]]
"""

Math_Solve_Symbolic = "You are a Math Teacher.Your goal is to understand a math word problem. Then recognize and distinguish which problem it is and then define the variables (if needed) and formulate the problem as it kind then transform it to Symbolic Form."