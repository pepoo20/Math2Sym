Math_Teacher_Prompt = """I want you to act as Math Teacher. Your goal is to create new high quality math problems to help students learn math.Please create a new linear system based on the given Word Problems. Then transform the new linear system and symbolic form.When doing this you MUST follow these Principle: 

Principle:
1. Do not solve the linear system.
2. Create only one new problem similar to the given problem.
3. There MUST be * between the coefficient and the variable. ex: 2*x
4. Symbolic form must be in the form of [[equation1, equation2, variable1, variable2, solve]]
5. DO NOT use the sign /,$ and words for numbers. Use only numbers.
6. When naming variables, use lowercase letters.

Your output should be in the following format:
Word Problem: <Your created word problem>
Break down the word problem into smaller information: <Explain the word problem>
Identify problem type: <Determining the type of problem>
Define the variables and formulate the linear system of equations: <Formulate the linear system of equations>
System of equations: <Linear system of equations>
Symbolic Form: <Symbolic Form>

"""

WordProblem_Prompt = Math_Teacher_Prompt + """
Task: Create a math word problem that can be solved using a system of linear equations based on the given word problems. Then, thinking step by step how the word problem can be solve by using linear system of equations. Then transform the word problem to linear system of equations and symbolic form.Try to be creative when creating the word problem.
Do not create problems about books. Be creative when creating the word problem and vary the numbers and context of the problems.

Word Problem:A company has allocated a budget of $50,000 for advertising on two different platforms: television and online. The television advertising campaign is expected to generate a 7% increase in sales, while the online advertising campaign is expected to generate a 4.5% increase in sales. The company aims to achieve a total sales increase of $3000 from these advertising efforts. How much money should be invested in each advertising platform?

Break down the word problem into smaller information:
1. Our goal is to determine how much money should be invested in each advertising platform to achieve a total sales increase of $3,000.
2. The company has allocated a budget of $50,000 for advertising on television and online.
3. The television advertising campaign is expected to generate a 7% increase in sales.
4. The online advertising campaign is expected to generate a 4.5% increase in sales.
Identify problem type: To solve this problem, we need to find the unknown quantities - the amount of money to be invested in each advertising platform. The problem provides information related to the unknown quantities, such as the total budget allocated for advertising, the expected sales increases from each platform, and the total sales increase target. We can set up a system of linear equations based on this information to determine the optimal allocation of funds.
Define the variables and formulate the linear system of equations:
Let x be the amount of money invested in the television advertising campaign.
Let y be the amount of money invested in the online advertising campaign.
The company has allocated a budget of $50,000 for advertising: x + y = 50000
The television advertising campaign is expected to generate a 7% increase in sales: 0.07*x
The online advertising campaign is expected to generate a 4.5% increase in sales: 0.045*y
The company aims to achieve a total sales increase of $3000: 0.07*x + 0.045*y = 3000
System of equations: {x + y = 50000, 0.07*x + 0.045*y = 3000}
Symbolic Form: [[x + y - 50000, 0.07*x + 0.045*y - 3000, x, y, solve]]

Word Problem:Arnold invested $64,000, some at 5.5% interest and the rest at 9%. How much did he invest at each rate if he received $4,500 in interest in one year?

Break down the word problem into smaller information:
1. Our goal is to determine how much Arnold invested at each interest rate to receive $4500 in interest in one year.
2. Arnold invested $64000 in total.
3. He invested some money at 5.5% interest and the rest at 9%.
Identify problem type: To solve this problem, we need to find the unknown quantities - the amount of money Arnold invested at each interest rate. The problem provides information related to the unknown quantities, such as the total amount of money Arnold invested, the interest rates, and the total interest earned. We can set up a system of linear equations based on this information to determine the optimal allocation of funds.
Define the variables and formulate the linear system of equations:
Let x be the amount of money invested at 5.5% interest.
Let y be the amount of money invested at 9% interest.
Arnold invested $64000 in total: x + y = 64000
The interest rate for the first investment is 5.5%: 0.055*x
The interest rate for the second investment is 9%: 0.09*y
Arnold received $4500 in interest in one year: 0.055*x + 0.09*y = 4500
System of equations: {x + y = 64000, 0.055*x + 0.09*y = 4500}
Symbolic Form: [[x + y - 64000, 0.055*x + 0.09*y - 4500, x, y, solve]]

Word Problem:Sarah is planning to save money for a down payment on a house in one years. She has $25,000 to invest and wants to maximize her returns. She decides to invest a portion of the money in a high-risk stock portfolio that has an expected annual return of 15%, and the remainder in a low-risk government bond that offers a 3% annual return. Sarah's goal is to earn a total of $2750 in interest and capital gains over the one-year period. How much money should she allocate to each investment option to achieve her target?

Break down the word problem into smaller information:
1. Our goal is to determine how much money Sarah should allocate to each investment option to earn $2750 in interest and capital gains over one year.
2. Sarah has $25000 to invest.
3. She wants to invest a portion of the money in a high-risk stock portfolio with an expected annual return of 15%.
4. The remainder will be invested in a low-risk government bond with a 3% annual return.
Identify problem type: To solve this problem, we need to find the unknown quantities - the amount of money Sarah should allocate to each investment option. The problem provides information about the total amount of money Sarah has to invest, the expected annual returns on each investment, and the total amount of interest and capital gains she wants to earn. We can set up a system of linear equations based on this information to determine the optimal allocation of funds.
Define the variables and formulate the linear system of equations:
Let x be the amount of money invested in the high-risk stock portfolio.
Let y be the amount of money invested in the low-risk government bond.
Sarah has $25000 to invest: x + y = 25000
The high-risk stock portfolio has an expected annual return of 15%: 0.15*x
The low-risk government bond has a 3% annual return: 0.03*y
Sarah wants to earn $2750 in interest and capital gains over one year: 0.15*x + 0.03*y = 2750
System of equations: {x + y = 25000, 0.15*x + 0.03*y = 2750}
Symbolic Form: [[x + y - 25000, 0.15*x + 0.03*y - 2750, x, y, solve]]

Word Problem:Andrea invested a total of $65,800 in two different mutual funds. One fund focuses on high-growth technology stocks and has an average annual return of 4.5%. The other fund is a more conservative balanced fund with an average annual return of 2%. After one year, Andrea earned a total of $2878.50 in interest from her investments. How much money did she invest in each mutual fund?

Break down the word problem into smaller information:
1. Our goal is to determine how much money Andrea invested in each mutual fund to earn $2878.50 in interest after one year.
2. Andrea invested a total of $65,800 in two different mutual funds.
3. One fund focuses on high-growth technology stocks with a 4.5% average annual return.
4. The other fund is a more conservative balanced fund with a 2% average annual return.
Identify problem type: To solve this problem, we need to find the unknown quantities - the amount of money Andrea invested in each mutual fund. The problem provides information related to the unknown quantities, such as the total amount of money invested, the average annual returns of the funds, and the total interest earned. We can set up a system of linear equations based on this information to determine the optimal allocation of funds.
Define the variables and formulate the linear system of equations:
Let x be the amount of money invested in the high-growth technology stocks fund.
Let y be the amount of money invested in the balanced fund.
Andrea invested a total of $65,800 in two mutual funds: x + y = 65800
The high-growth technology stocks fund has a 4.5% average annual return: 0.045*x
The balanced fund has a 2% average annual return: 0.02*y
Andrea earned $2878.50 in interest after one year: 0.045*x + 0.02*y = 2878.50
System of equations: {x + y = 65800, 0.045*x + 0.02*y = 2878.50}
Symbolic Form: [[x + y - 65800, 0.045*x + 0.02*y - 2878.50, x, y, solve]]

Word Problem: After inheriting a sum of money, Michael decides to invest it in two different types of accounts. He puts part of the money in a high-yield savings account with a 3% annual interest rate and the rest in a stock market index fund with an expected return of 7% per year. After one year, the total interest and returns from both accounts amount to $4,200. If he invested a total of $70,000, how much did he put in each type of account?

Break down the word problem into smaller information:
1. Our goal is to determine how much Michael invested in each type of account to earn $4200 in interest and returns after one year.
2. Michael invested a total of $70,000.
3. He put part of the money in a high-yield savings account with a 3% annual interest rate.
4. The rest of the money was invested in a stock market index fund with an expected return of 7% per year.
Identify problem type: To solve this problem, we need to find the unknown quantities - the amount of money Michael invested in each type of account. The problem provides information related to the unknown quantities, such as the total amount of money invested, the interest rates, and the total interest and returns earned. We can set up a system of linear equations based on this information to determine the optimal allocation of funds.
Define the variables and formulate the linear system of equations:
Let x be the amount of money invested in the high-yield savings account.
Let y be the amount of money invested in the stock market index fund.
Michael invested a total of $70,000: x + y = 70000
The high-yield savings account has a 3% annual interest rate: 0.03*x
The stock market index fund has an expected return of 7% per year: 0.07*y
Michael earned $4,200 in interest and returns after one year: 0.03*x + 0.07*y = 4200
System of equations: {x + y = 70000, 0.03*x + 0.07*y = 4200}
Symbolic Form: [[x + y - 70000, 0.03*x + 0.07*y - 4200, x, y, solve]]

Word Problem:
"""

Normal =Math_Teacher_Prompt + """

Task: Create a math word problem that can be solved using a system of linear equations based on the given word problems. Then, thinking step by step how the word problem can be solve by using linear system of equations. Then transform the word problem to linear system of equations and symbolic form.
Be creative when creating the word problem and vary the numbers and context of the problems.
Do not create problems about books.

Word Problem: Emma and Liam are saving money. Emma starts with $80 and saves $10 per week. Liam starts with $120 and saves $6 per week. After how many weeks will they have the same amount of money?

Break down the word problem into smaller information:
1. Our goal is to find out after how many weeks Emma and Liam will have the same amount of money.
2. Emma starts with $80 and saves $10 per week.
3. Liam starts with $120 and saves $6 per week.
4. The total amount of money they have will be the sum of the starting amount and the savings per week multiplied by the number of weeks.
Identify problem type: To solve this problem, find the unknown quantity - number of weeks when Emma and Liam will have the same amount of money.Declare one more unknown quantity which is the total amount of money when they have the same amount. With all the information given relate to the unknown quantities we need to use a system of linear equations to solve the problem.
Define the variables and formulate the linear system of equations:
Let x be the number of weeks.
Let y be the total amount of money they will have after x weeks.
Emma's Equation:
Starting Amount: $80 (This is a constant value, independent of the number of weeks)
Savings per Week: $10 (This rate is multiplied by the number of weeks to determine the total amount saved)
Total Amount: Starting Amount + Savings per Week * Number of Weeks = 80 + 10*x
Liam's Equation:
Starting Amount: $120 (This is a constant value, independent of the number of weeks)
Savings per Week: $6 (This rate is multiplied by the number of weeks to determine the total amount saved)
Total Amount: Starting Amount + Savings per Week * Number of Weeks = 120 + 6*x
System of equations: {80 + 10*x = y, 120 + 6*x = y}
Symbolic Form: [[80 + 10*x - y, 120 + 6*x - y, x, y, solve]]

Word Problem:The price, e, of an entertainment system at Extreme Electronics is $220 less than twice the price, u, of the same system at Ultra Electronics. The difference in price between the system at Extreme Electronics and Ultra Electronics is $175. What is the price of the system at each store?

Break down the word problem into smaller information:
1. Our goal is to determine the price of the entertainment system at Extreme Electronics and Ultra Electronics.
2. The price of the system at Extreme Electronics is $220 less than twice the price of the system at Ultra Electronics.
3. The difference in price between the two systems is $175.
Identify problem type: To solve this problem, we need to find the unknown quantities - the price of the system at Extreme Electronics and Ultra Electronics. The problem provides information related to the unknown quantities, such as the relationship between the prices of the systems at the two stores and the price difference. We can set up a system of linear equations based on this information to determine the prices of the systems at each store.
Define the variables and formulate the linear system of equations:
Let e be the price of the system at Extreme Electronics.
Let u be the price of the system at Ultra Electronics.
The price of the system at Extreme Electronics is $220 less than twice the price of the system at Ultra Electronics: e = 2*u - 220
The difference in price between the two systems is $175: e - u = 175
System of equations: {e = 2*u - 220, e - u = 175}
Symbolic Form: [[e - 2*u + 220, e - u - 175, e, u, solve]]

Word Problem:It takes three hours for a boat to go 18 miles downstream, and nine hours to return. What is the rate of the boat in calm water and the rate of the current?

Break down the word problem into smaller information:
1. Our goal is to determine the rate of the boat in calm water and the rate of the current.
2. The boat travels downstream for 3 hours and covers a distance of 18 miles.
3. The boat travels upstream for 9 hours and covers a distance of 18 miles.
Identify problem type: We need to find two unknown quantities: the rate of the boat in calm water and the rate of the current. The problem provides information about relationships between these quantities. We can set up a system of linear equations based on the given information to solve the problem.
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
Symbolic Form: [[3*b + 3*c - 18, 9*b - 9*c - 18, b, c, solve]]

Word Problem: The Rocket Coaster has 15 cars, some that hold 4 people and some that hold 6 people.There is room for 72 people. How many 4-person cars and how many 6-person cars are there?

Break down the word problem into smaller information:
1. Our goal is to determine how many 4-person cars and 6-person cars are there.
2. The Rocket Coaster has 15 cars in total.
3. The total capacity of the coaster is 72 people.
4. There are two types of cars: 4-person cars and 6-person cars.
Identify problem type: We need to find two unknown quantities: the number of 4-person cars and the number of 6-person cars. The problem provides information about relationships between these quantities. We can set up a system of linear equations based on the given information to solve the problem.
Define the variables and formulate the linear system of equations:
Let x be the number of 4-person cars.
Let y be the number of 6-person cars.
Total cars = number of 4-person cars + number of 6-person cars
The Rocket Coaster has 15 cars in total: x + y = 15
Total capacity = (number of 4-person cars * 4) + (number of 6-person cars * 6)
The total capacity of the coaster is 72 people and each 4-person car holds 4 people and each 6-person car holds 6 people: 4*x + 6*y = 72
System of equations: {x + y = 15, 4*x + 6*y = 72}
Symbolic Form: [[x + y - 15, 4*x + 6*y - 72, x, y, solve]]

Word Problem:  At the end of the 2000 NBA regular season, the Houston comets had 22 more victories than losses. The number of victories they had was three less than six time the number of losses. How many regular season games did the Houston comets play during the 2000 NBA season?

Break down the word problem into smaller information:
1. Our goal is to determine the number of regular season games the Houston Comets played during the 2000 NBA season.
2. The Houston Comets had 22 more victories than losses.
3. The number of victories was three less than six times the number of losses.
Identify problem type: To solve this problem, we need to find the unknown quantity - the number of regular season games played by the Houston Comets. The problem provides information related to the unknown quantity, such as the relationship between the number of victories and losses. We can set up a system of linear equations based on this information to determine the number of games played.
Define the variables and formulate the linear system of equations:
Let x be the number of losses.
Let y be the number of victories.
The Houston Comets had 22 more victories than losses: y = x + 22
The number of victories was three less than six times the number of losses: y = 6*x - 3
System of equations: {y = x + 22, y = 6*x - 3}
Symbolic Form: [[y - x - 22, y - 6*x + 3, x, y, solve]]

Word Problem:
""".strip()
