Math_Teacher_Prompt = """I want you to act as Math Teacher. Your goal is to create high quality math problems to help students learn math.You will be given a math question. Please create a new question based on the Given Problems and following principles. Then transform the new question to Symbolic Form.Symbolic Form elements only include the equation, the inequality symbol, the constant, the variable, and the solve command.
You must followed these principles:
1. Do not solve the problem. 
2. Create only one new problem similar to the given problem.
3. There MUST be * between the coefficient and the variable. Example: 2*x + 3 > 7. 
4. DO NOT use the symbol //,$ and word in the symbolic form.
5. DO NOT perform any arithmetic operations or calculations while defining the variables and formulating the inequality.

Your output should be in the following format:
Topic: <Topic>
Word Problem: <Your Word Problem>
Break down the word problem into smaller information: <information>
Identify problem type: <Determining the type of problem>
Define the variables and formulate the inequality: <inequality>
Symbolic Form: <Symbolic Form>
"""

Word_Problem_Seed =Math_Teacher_Prompt+ """
Task : Create a new word problem and transform it to an inequality and Symbolic Form.Try to be creative as possible and use ONLY one variable in the word problem.
You will get rewarded for reasonable and variety of the word problem. 

Word Problem:A bookshelf has five shelves, and each shelf can hold up to 20 books. If Sally already has 30 books on the bookshelf, how many more books can she add?

Break down the word problem into smaller information:
1. Our goal is to find the number of books Sally can add to the bookshelf.
2. The bookshelf has five shelves, and each shelf can hold up to 20 books.
3. Sally already has 30 books on the bookshelf.
Identify problem type: The problem asks for the number of books Sally can add to the bookshelf which implies finding the maximum value that satisfies the constraints. Each shelf can hold up to 20 books is an upper bound constraint. We can use the inequality to solve this problem.
Define the variables and formulate the inequality:
Let x be the number of books Sally can add to the bookshelf.
Total capacity = Capacity of the bookshelf
The bookshelf has five shelves, and each shelf can hold up to 20 books so the capacity of the bookshelf is 5*20
Sally already has 30 books on the bookshelf so the number of books Sally can add to the bookshelf is x
The total capacity should be greater than or equal to the total amount of books so the total capacity >= 30 + x
Inequality: 5*20 >= 30 + x
Symbolic Form: [[5*20, >=, 30 + x, x, solve]]

Word Problem:Brice has 30$ to take his brother and his friends to the movies. If each ticket costs 4.00$, and he must buy tickets for himself and his brother, what is the greatest number of friends he can invite?
Break down the word problem into smaller information:
1. Our goal is to find the greatest number of friends Brice can invite.
2. Brice has 30 to take his brother and his friends to the movies.
3. Each ticket costs $4.
4. He must buy tickets for himself and his brother.
Identify problem type: The problem asks for the greatest number of friends Brice can invite which implies finding the maximum value that satisfies the constraints.Brice must buy tickets for himself and his brother is an constraint and Brice has a limited budget of 30$ this is a lower bound constraint. We can use the inequality to solve this problem.
Define the variables and formulate the inequality:
Let x be the number of friends Brice can invite.
Total cost = Cost of tickets for Brice and his brother + Cost of tickets for his friends
Each ticket costs $4 so the cost of tickets for Brice and his brother is 2*4
Cost of tickets for his friends is x*4
Total cost = 2*4 + x*4
Brice has 30 so we accept at 30 and less so the is '=' sign in the inequality then 2*4 + x*4 <= 30
Inequality: 2*4 + x*4 <= 30
Symbolic Form: [[2*4 + x*4, <=, 30, x, solve]]


Word Problem: What numbers satisfy the condition: seven more than two-thirds of a number is strictly less than thirty?

Break down the word problem into smaller information:
1. Our goal is to find the numbers that satisfy the condition.
2. Seven more than two-thirds of a number is strictly less than thirty.
Identify problem type: The problem asks for the numbers that satisfy the condition which implies finding the range of values that satisfy the constraints. Seven more than two-thirds of a number is strictly less than thirty is a constraint. We can use the inequality to solve this problem.
Define the variables and formulate the inequality:
Let x be the number.
Two-thirds of a number is (2/3)*x
Seven more than two-thirds of a number is (2/3)*x + 7
Strictly less than thirty is < 30 so the inequality is (2/3)*x + 7 < 30
Inequality: (2/3)*x + 7 < 30
Symbolic Form: [[(2/3)*x + 7, <, 30, x, solve]]

Word Problem: A small tourist boat has a maximum capacity of 1,500 pounds, according to the boat's safety guidelines. If the average weight of one passenger, including their luggage, is 200 pounds, how many passengers can safely board the boat?

Break down the word problem into smaller information:
1. Our goal is to find the number of passengers that can safely board the boat.
2. The boat has a maximum capacity of 1,500 pounds.
3. The average weight of one passenger, including their luggage, is 200 pounds.
Identify problem type: The problem asks for the number of passengers that can safely board the boat which implies finding the maximum value that satisfies the constraints. The boat has a maximum capacity of 1,500 pounds is an upper bound constraint. We can use the inequality to solve this problem.
Define the variables and formulate the inequality:
Let x be the number of passengers that can safely board the boat.
Total weight = Weight of the passengers
The average weight of one passenger, including their luggage, is 200 pounds so the weight of the passengers is x*200
The boat has a maximum capacity of 1,500 pounds so we accept at 1,500 and less so the is '=' sign in the inequality then x*200 <= 1,500
Inequality: x*200 <= 1,500
Symbolic Form: [[x*200, <=, 1,500, x, solve]]

Word Problem:A water tank can hold 2400 liters of water. If 300 liters of water are already in the tank, how many more liters of water can be added?

Break down the word problem into smaller information:
1. Our goal is to find the number of liters of water that can be added to the tank.
2. The water tank can hold 2400 liters of water.
3. 300 liters of water are already in the tank.
Identify problem type: The problem asks for the number of liters of water that can be added to the tank which implies finding the maximum value that satisfies the constraints. The water tank can hold 2400 liters of water is an upper bound constraint. We can use the inequality to solve this problem.
Define the variables and formulate the inequality:
Let x be the number of liters of water that can be added to the tank.
Total capacity = Capacity of the tank
The water tank can hold 2400 liters of water so the capacity of the tank is 2400
300 liters of water are already in the tank so the liters of water that can be added to the tank is x
The total capacity should be greater than or equal to the total amount of water so the total capacity >= 300 + x
Inequality: 2400 >= 300 + x
Symbolic Form: [[2400, >=, 300 + x, x, solve]]


Word Problem: A taxi charges a flat rate of $1.75, plus an additional $0.65 per mile. If Erica has at most \$10 to spend on the cab ride, how far could she travel?

Break down the word problem into smaller information:
1. Our goal is to find the distance Erica could travel.
2. The taxi charges a flat rate of $1.75, plus an additional $0.65 per mile.
3. Erica has at most $10 to spend on the cab ride.
Identify problem type: The problem asks for the distance Erica could travel which implies finding the maximum value that satisfies the constraints. Erica has at most $10 to spend on the cab ride is an upper bound constraint. We can use the inequality to solve this problem.
Define the variables and formulate the inequality:
Let x be the distance Erica could travel.
Total cost = Flat rate + Cost per mile
The taxi charges a flat rate of $1.75 so the flat rate is 1.75
An additional $0.65 per mile so the cost per mile is 0.65*x
Erica has at most $10 to spend on the cab ride so we accept at 10 and less so the is '=' sign in the inequality then 1.75 + 0.65*x <= 10
Inequality: 1.75 + 0.65*x <= 10
Symbolic Form: [[1.75 + 0.65*x, <=, 10, x, solve]]


Word Problem:
"""
atleast = Math_Teacher_Prompt+"""
Task : Create a new word problem and transform it to an inequality and Symbolic Form.Try to be creative as possible and use ONLY one variable in the word problem.
You will get rewarded for reasonable and variety of the word problem.

Word Problem: Brenda has $500 in her bank account.  Every week, she withdraws $40 for expenses.  Without making any deposits, how many weeks can she withdraw this money if she wants to maintain a balance of at least $200? 

Break down the word problem into smaller information:
1. Our goal is to find the number of weeks Brenda can withdraw this money if she wants to maintain a balance of at least $200.
2. Brenda has $500 in her bank account.
3. Every week, she withdraws $40 for expenses.
4. Without making any deposits.
Identify problem type: Maintain a balance of at least $200 implies that Brenda's balance should be greater than or equal to $200, we are not looking for a specific number of weeks but a minimum threshold. This is a lower bound constraint making it an inequality problem.
Define the variables and formulate the inequality:
Let x be the number of weeks Brenda can withdraw this money.
Total balance = Balance Brenda has + Balance Brenda needs to maintain
Brenda has $500 in her bank account so the balance Brenda has is 500
Every week, she withdraws $40 for expenses so the balance Brenda needs to maintain is x*40
for at least $200 we accept at 200 and more so the is '=' sign in the inequality then total balance >= 200
Inequality: 500 - x*40 >= 200
Symbolic Form: [[500 - x*40, >=, 200, x, solve]]

Word Problem: Allison practices her violin for at least 12 hours per week. She practices for three fourths of an hou reach session. If Allison has already practiced 3 hours this week, how many more sessions remain for her to meet or exceed her weekly practice goal?

Break down the word problem into smaller information:
1. Our goal is to find the number of sessions Allison needs to meet or exceed her weekly practice goal.
2. Allison practices her violin for at least 12 hours per week.
3. She practices for three fourths of an hour each session.
4. Allison has already practiced 3 hours this week.
Identify problem type: At least 12 hours per week implies that Allison practice time should be greater than or equal to 12 hours, we are not looking for a specific number of sessions but a minimum threshold. This is a lower bound constraint making it an inequality problem.
Define the variables and formulate the inequality:
Let x be the number of sessions Allison needs to meet or exceed her weekly practice goal.
Total hours = Hours Allison has already practiced + Hours Allison needs to practice
Allison has already practiced 3 hours this week so the hours Allison has already practiced is 3
Each session is three fourths of an hour so the hours Allison needs to practice is x*(3/4)
for at least 12 hours we accept at 12 hours and more so the is '=' sign in the inequality then total hours >= 12
Inequality: 3 + x*(3/4) >= 12
Symbolic Form: [[3 + x*(3/4), >=, 12, x, solve]]

Word Problem:Marco is saving up to buy a new gaming console that costs $350. He already has $120 saved and earns $15 per week by doing chores.How many weeks will it take Marco to save enough money to afford the gaming console if he doesn't spend any of his savings?

Break down the word problem into smaller information:
1. Our goal is to find the number of weeks Marco will take to save enough money to afford the gaming console.
2. The gaming console costs $350.
3. Marco already has $120 saved.
4. Marco earns $15 per week by doing chores.
Identify problem type: Marco will take to save enough money to afford the gaming console implies that Marco's savings should be greater than or equal to $350, we are not looking for a specific number of weeks but a minimum threshold. This is a lower bound constraint making it an inequality problem.
Define the variables and formulate the inequality:
Let x be the number of weeks Marco will take to save enough money to afford the gaming console.
Total savings = Savings Marco has + Savings Marco needs
Marco already has $120 saved so the savings Marco has is 120
Marco earns $15 per week by doing chores so the savings Marco needs is x*15
for at least $350 we accept at 350 and more so the is '=' sign in the inequality then total savings >= 350
Inequality: 120 + x*15 >= 350
Symbolic Form: [[120 + x*15, >=, 350, x, solve]]

Word Problem:The school drama club wants to put on a play, but they need to raise money for costumes, props, and other expenses. They estimate that they will need at least $800 for the production. The drama club has $250 in their account from previous fundraisers. They decide to raise the rest of the money by selling tickets to a special preview performance. If they charge $10 per ticket, how many tickets must they sell to have enough money to cover the expenses for the play?

Break down the word problem into smaller information:
1. Our goal is to find the number of tickets they must sell to have enough money to cover the expenses for the play.
2. The drama club needs at least $800 for the production.
3. The drama club has $250 in their account from previous fundraisers.
4. They decide to raise the rest of the money by selling tickets to a special preview performance.
5. They charge $10 per ticket.
Identify problem type: The problem asks for the number of tickets they must sell to have enough money to cover the expenses for the play which implies finding the minimum value that satisfies the constraints. The total funds for the production should be greater than or equal to the total cost of the production is a lower bound constraint. We can use the inequality to solve this problem.
Define the variables and formulate the inequality:
Let x be the number of tickets they must sell.
Total funds = Funds the drama club has + Earnings from ticket sales
The drama club has $250 in their account from previous fundraisers so the funds the drama club has is 250
They decide to raise the rest of the money by selling tickets to a special preview performance so the earnings from ticket sales is x*10
The total funds should be greater than or equal to the total cost of the production so the total funds >= 800
Inequality: 250 + x*10 >= 800
Symbolic Form: [[250 + x*10, >=, 800, x, solve]]

Word Problem:Keisha is training for a challenging mountain hike. She wants to climb a total elevation gain of at least 5000 meters before her hike. She has already climbed 1200 meters during her training so far. Keisha plans to hike a local trail with a 350-meter elevation gain each day to further her training.How many more days does Keisha need to hike the local trail to reach her goal of at least 5000 meters of total elevation gain before her big hike?

Break down the word problem into smaller information:
1. Our goal is to find the number of days Keisha needs to hike the local trail to reach her goal of at least 5000 meters of total elevation gain.
2. Keisha wants to climb a total elevation gain of at least 5000 meters.
3. She has already climbed 1200 meters during her training so far.
4. Keisha plans to hike a local trail with a 350-meter elevation gain each day.
Identify problem type: At least 5000 meters of total elevation gain implies that Keisha's total elevation gain should be greater than or equal to 5000 meters, we are not looking for a specific number of days but a minimum threshold. This is a lower bound constraint making it an inequality problem.
Define the variables and formulate the inequality:
Let x be the number of days Keisha needs to hike the local trail.
Total elevation gain = Elevation gain Keisha has already climbed + Elevation gain Keisha needs to climb
Keisha has already climbed 1200 meters so the elevation gain Keisha has already climbed is 1200
Keisha plans to hike a local trail with a 350-meter elevation gain each day so the elevation gain Keisha needs to climb is x*350
for at least 5000 meters we accept at 5000 meters and more so the is '=' sign in the inequality then total elevation gain >= 5000
Inequality: 1200 + x*350 >= 5000
Symbolic Form: [[1200 + x*350, >=, 5000, x, solve]]

Word Problem:
"""

Word_Problem_Compound_Seed = Math_Teacher_Prompt+ """
Task : Create a new word problem similar to the given problem about compound inequalities and transform it to an inequality and Symbolic Form.Be as creative as possible try to use any kind of topics for variation.
You will get rewarded for reasonable and variety of the word problem topic.
Note: Do not create problem about books.

Topic: Land Plot Perimeter
Word Problem: A square plot of land is being prepared for planting. The perimeter of the plot must be between 40 meters and 60 meters inclusively. Find the range of possible side lengths for the square plot.

Break down the word problem into smaller information:
1. Our goal is to find the range of possible side lengths for the square plot.
2. The perimeter of the plot must be between 40 meters and 60 meters inclusively.
Identify problem type: The perimeter of the plot must be between 40 meters and 60 meters inclusively sets the range of acceptable perimeters for the square plot. This implies the use of compound inequalities to solve the problem.
Define the variables and formulate the compound inequality:
Let x be the side length of the square plot.
The perimeter of a square is given by P = 4*x
between 40 and 60 meters inclusively so the perimeter is between 40 and 60 inclusive of the values so = sign is used in the inequality then 40 <= 4*x <= 60
Compound Inequality: 40 <= 4*x <= 60
Symbolic Form: [[40 <= 4*x, 4*x <= 60, x, solve]]

Topic: Final Exam Score
Word Problem: Ralph needs to earn a B in his Geology class. His current test scores are 91, 79. His final exam is worth 4 test scores. In order to earn a B Ralph's average must lie between 80 and 89 inclusive. What range of scores can Ralph receive on the final exam to earn a B in the course?

Break down the word problem into smaller information:
1. Our goal is to find the range of scores Ralph can receive on the final exam to earn a B in the course.
2. Ralph's average must lie between 80 and 89 inclusive.
3. His current test scores are 91, 79.
4. The final exam is worth 4 test scores.
Identify problem type: Ralph's average must lie between 80 and 89 inclusive sets the range of acceptable averages for Ralph. This define a specific range of values that Ralph's average should fall within, making it a compound inequality problem.
Define the variables and formulate the compound inequality:
Let x be the score Ralph can receive on the final exam.
between 80 and 89 inclusive of the values so = sign is used in the inequality then 80 <= Average <= 89
Ralph's average is calculated as Average = (91 + 79 + 4*x) / 6
Compound Inequality: 80 <= (91 + 79 + 4*x) / 6 <= 89
Symbolic Form: [[80 <= (91 + 79 + 4*x)/6, (91 + 79 + 4*x)/6 <= 89, x, solve]]

Topic: Ski Shop Height Limit
Word Problem: A ski shop carries skis that are between 150 and 220cm long. They recommend that the skis be 1.25 longer than your height.Calculate the tallest height that a person can be and still rent skis from the shop.

Break down the word problem into smaller information:
1. Our goal is to find the tallest height that a person can be and still rent skis from the shop.
2. The ski shop carries skis that are between 150 and 220cm long.
3. They recommend that the skis be 1.25 longer than your height.
Identify problem type: The ski shop carries skis that are between 150 and 220cm long sets the range of acceptable ski lengths for the customer. This implies the use of compound inequalities to solve the problem.
Define the variables and formulate the compound inequality:
Let x be the height of the person.
between 150 and 220cm long can be written as 150 <= Ski length <= 220
The skis should be 1.25 times longer than your height so the ski length is 1.25*x
Compound Inequality: 150 <= 1.25*x <= 220
Symbolic Form: [[150 <= 1.25*x, 1.25*x <= 220, x, solve]]

Topic: Desired Cake Profit
Word Problem: Mia is a baker who wants to make a profit of at least $200 but no more than $300 on a large order of cupcakes for a wedding. She has already spent $150 on ingredients and the decorations. Each cupcake she sells will bring in a profit of $2. How many cupcakes does Mia need to sell to make her desired profit?

Break down the word problem into smaller information:
1. Our goal is to find the number of cupcakes Mia needs to sell to make her desired profit.
2. Mia wants to make a profit of at least $200 but no more than $300.
3. She has already spent $150 on ingredients and the decorations.
4. Each cupcake she sells will bring in a profit of $2.
Identify problem type: Mia wants to make a profit of at least $200 but no more than $300 signifies that Mia's profit falls within a specific range, having a lower and upper bound.This implies the use of double inequalities or compound inequalities to solve the problem.
Define the variables and formulate the compound inequality:
Let x be the number of cupcakes Mia needs to sell.
at least $200 but no more than $300 so the profit is between 200 and 300 inclusive of the values so = sign is used in the inequality then 200 <= Profit <= 300
Profit = Total revenue - Total cost
Total revenue = Profit from selling cupcakes
Each cupcake she sells will bring in a profit of $2 so the profit from selling cupcakes is x*2
Total cost = Cost of ingredients and decorations
She has already spent $150 on ingredients and the decorations so the cost of ingredients and decorations is 150
Profit = x*2 - 150
We can find the number of cupcakes Mia needs to sell by solving the compound inequality: 200 <= x*2 - 150 <= 300
Symbolic Form: [[200 <= x*2 - 150, x*2 - 150 <= 300, x, solve]]

Topic: Smart Watch Price
Word Problem: An electronics store is giving a $50 discount coupon for all smart watches. Emma is considering various smart watches with prices ranging from $220 to $310. How much can she anticipate to pay after applying the discount coupon?

Break down the word problem into smaller information:
1. Our goal is to find the amount Emma can anticipate to pay after applying the discount coupon.
2. The smart watches have prices ranging from $220 to $310.
3. The store is giving a $50 discount coupon for all smart watches.
Identify problem type: Emma is considering various smart watches with prices ranging from $220 to $310 sets the range of acceptable prices for the smart watches. This defines the lower and upper bounds of the acceptable prices making it a compound inequality problem.
Define the variables and formulate the compound inequality:
Let x be the price of the smart watch.
ranging from $220 to $310 is taking the price between 220 and 310 inclusive of the values so = sign is used in the inequality then 220 <= x <= 310
The store is giving a $50 discount coupon for all smart watches so the price after the discount coupon is x - 50
Combining the inequalities and the discount coupon: 220 <= x - 50 <= 310
Symbolic Form: [[220 <= x - 50, x - 50 <= 310, x, solve]]

Word Problem: About 20\% of the time you sleep is spent in rapid eye movement (REM) sleep,which is associated with dreaming.If an adult sleeps 7 to 8 hours,how much time is spent in REM sleep?

Break down the word problem into smaller information:\newline 1. Our goal is to find the time spent in REM sleep.\newline 2. About 20% of the time you sleep is spent in REM sleep.\newline 3. An adult sleeps 7 to 8 hours.\newline Identify problem type: About 20% of the time you sleep is spent in REM sleep sets the range of acceptable time spent in REM sleep. This implies the use of compound inequalities to solve the problem.\newline Define the variables and formulate the compound inequality:\newline Let x be the time spent in REM sleep.\newline About 20% of the time you sleep is spent in REM sleep so the time spent in REM sleep is 0.20*x\newline An adult sleeps 7 to 8 hours so the time spent sleeping is between 7 and 8 inclusive of the values so = sign is used in the inequality then 7 <= x <= 8\newline Combining the inequalities and the time spent in REM sleep: 7 <= 0.20*x <= 8\newline Symbolic Form: [[7 <= 0.20*x, 0.20*x <= 8, x, solve]]

Word Problem:
"""
First_Compound = """
Word Problem:A company manufactures and sells custom furniture. The cost to produce each piece of furniture is between $120 and $150, inclusive. The company has a minimum production requirement of 30 pieces but cannot produce more than 50 pieces for a particular order due to resource constraints. Write a compound inequality representing the possible total cost for the company from this order.
Break down the word problem into smaller information:
1. Our goal is to find the possible total cost for the company from this order.
2. The cost to produce each piece of furniture is between $120 and $150, inclusive.
3. The company has a minimum production requirement of 30 pieces but cannot produce more than 50 pieces for a particular order.
Identify problem type: The cost to produce each piece of furniture is between $120 and $150, inclusive sets the range of acceptable costs for the company. This implies the use of compound inequalities to solve the problem.
Define the variables and formulate the compound inequality:
Let x be the total cost for the company from this order and the total cost can be calculated as the product of the cost per piece and the number of pieces produced.
The cost to produce each piece of furniture is between $120 and $150, inclusive so the cost per piece is between 120 and 150 inclusive of the values so = sign is used in the inequality then 120 <= Cost per piece <= 150
The company has a minimum production requirement of 30 pieces but cannot produce more than 50 pieces for a particular order so the number of pieces produced is between 30 and 50 inclusive of the values so = sign is used in the inequality then 30 <= Number of pieces <= 50
Total cost = Cost per piece * Number of pieces
Combining the inequalities: Cost per piece * Number of pieces is between 120*30 and 150*50 inclusive of the values so = sign is used in the inequality then Compound Inequality: 120*30 <= x <= 150*50
Symbolic Form: [[120*30 <= x, x <= 150*50, x, solve]]

Word Problem:A local farmer sells organic produce at a farmers' market. The price per pound of their vegetables ranges between $2 and $5, inclusive. They sell between 100 and 200 pounds of vegetables each week. Additionally, the farmer incurs a weekly stall fee of $50. Write a compound inequality representing the possible total revenue for the farmer from selling the vegetables in one week.
Break down the word problem into smaller information:
1. Our goal is to find the possible total revenue for the farmer from selling the vegetables in one week.
2. The price per pound of their vegetables ranges between $2 and $5, inclusive.
3. They sell between 100 and 200 pounds of vegetables each week.
4. The farmer incurs a weekly stall fee of $50.
Identify problem type: The price per pound of their vegetables ranges between $2 and $5, inclusive sets the range of acceptable prices for the vegetables. This implies the use of compound inequalities to solve the problem.
Define the variables and formulate the compound inequality:
Let x be the total revenue for the farmer from selling the vegetables in one week and the total revenue can be calculated as the product of the price per pound and the number of pounds sold.
The price per pound of their vegetables ranges between $2 and $5, inclusive so the price per pound is between 2 and 5 inclusive of the values so = sign is used in the inequality then 2 <= Price per pound <= 5
They sell between 100 and 200 pounds of vegetables each week so the number of pounds sold is between 100 and 200 inclusive of the values so = sign is used in the inequality then 100 <= Number of pounds <= 200
Total revenue = Price per pound * Number of pounds
Combining the inequalities: Price per pound * Number of pounds is between 2*100 and 5*200 inclusive of the values so = sign is used in the inequality and the weekly stall fee is minus from the total revenue then Compound Inequality: 2*100 -50 <= x <= 5*200 - 50
Symbolic Form: [[2*100 - 50 <= x, x <= 5*200 - 50, x, solve]]

Word Problem:A freelance graphic designer charges an hourly rate between $50 and $75, inclusive. They are working on a project that requires a minimum of 15 hours but no more than 25 hours. The designer also charges a fixed project setup fee of $200. Write a compound inequality representing the possible total earnings for the freelance graphic designer from this project.
Break down the word problem into smaller information:
1. Our goal is to find the possible total earnings for the freelance graphic designer from this project.
2. The hourly rate of the designer ranges between $50 and $75, inclusive.
3. The project requires a minimum of 15 hours but no more than 25 hours.
4. The designer also charges a fixed project setup fee of $200.
Identify problem type: The hourly rate of the designer ranges between $50 and $75, inclusive sets the range of acceptable hourly rates for the designer. This implies the use of compound inequalities to solve the problem.
Define the variables and formulate the compound inequality:
Let x be the total earnings for the freelance graphic designer from this project and the total earnings can be calculated as the product of the hourly rate and the number of hours worked plus the fixed project setup fee.
The hourly rate of the designer ranges between $50 and $75, inclusive so the hourly rate is between 50 and 75 inclusive of the values so = sign is used in the inequality then 50 <= Hourly rate <= 75
The project requires a minimum of 15 hours but no more than 25 hours so the number of hours worked is between 15 and 25 inclusive of the values so = sign is used in the inequality then 15 <= Number of hours <= 25
Total earnings = Hourly rate * Number of hours + Fixed project setup fee
Combining the inequalities: Hourly rate * Number of hours + Fixed project setup fee is between 50*15 + 200 and 75*25 + 200 inclusive of the values so = sign is used in the inequality and the fixed project setup fee is added to the total earnings then Compound Inequality: 50*15 + 200 <= x <= 75*25 + 200
Symbolic Form: [[50*15 + 200 <= x, x <= 75*25 + 200, x, solve]]
"""


Second_Temp = """

Word Problem:A software company is planning a marketing campaign and will distribute promotional USB drives. The cost of producing each USB drive is $3, and the company plans to give away between 100 and 500 USB drives. Additionally, there is a setup fee of $150 for the production. The company's budget for the campaign is between $600 and $1800. What is the possible range of the number of USB drives the company can produce while meeting both the cost constraints and the distribution limits?
Break down the word problem into smaller information:
1. Our goal is to find the possible range of the number of USB drives the company can produce while meeting both the cost constraints and the distribution limits.
2. The cost of producing each USB drive is $3.
3. The company plans to give away between 100 and 500 USB drives.
4. There is a setup fee of $150 for the production.
5. The company's budget for the campaign is between $600 and $1800.
Identify problem type: The company plans to give away between 100 and 500 USB drives and the company's budget for the campaign is between $600 and $1800 sets the range of acceptable numbers of USB drives and costs for the company. This implies the use of compound inequalities to solve the problem.
Define the variables and formulate the compound inequality:
Let x be the number of USB drives the company can produce.
between $600 and $1800 so the total cost is between 600 and 1800 inclusive of the values so = sign is used in the inequality then 600 <= Total cost <= 1800
The cost of producing each USB drive is $3 so the cost per USB drive is 3
The company plans to give away between 100 and 500 USB drives so the number of USB drives produced is between 100 and 500 inclusive of the values so = sign is used in the inequality then 100 <= Number of USB drives <= 500
Total cost = Cost per USB drive * Number of USB drives + Setup fee
Combining the inequalities: 600 <= 3*x + 150 <= 1800 and 100 <= x <= 500
Symbolic Form: [[600 <= 3*x + 150, 3*x + 150 <= 1800, 100 <= x, x <= 500, x, solve]]

Word Problem:A city is planning to install solar-powered streetlights along its main roads. The cost of each streetlight is $500, and the city plans to install between 20 and 100 streetlights. Additionally, there is an installation fee of $5,000. The city's budget for the project is between $25,000 and $60,000. If x represents the number of streetlights the city can install, write a compound inequality representing the possible range of the number of streetlights the city can install while meeting both the cost constraints and the installation limits.
Break down the word problem into smaller information:
1. Our goal is to find the possible range of the number of streetlights the city can install while meeting both the cost constraints and the installation limits.
2. The cost of each streetlight is $500.
3. The city plans to install between 20 and 100 streetlights.
4. There is an installation fee of $5,000.
5. The city's budget for the project is between $25,000 and $60,000.
Identify problem type: The city plans to install between 20 and 100 streetlights and the city's budget for the project is between $25,000 and $60,000 sets the range of acceptable numbers of streetlights and costs for the city. This implies the use of compound inequalities to solve the problem.
Define the variables and formulate the compound inequality:
Let x be the number of streetlights the city can install.
between $25,000 and $60,000 so the total cost is between 25000 and 60000 inclusive of the values so = sign is used in the inequality then 25000 <= Total cost <= 60000
The cost of each streetlight is $500 so the cost per streetlight is 500
The city plans to install between 20 and 100 streetlights so the number of streetlights installed is between 20 and 100 inclusive of the values so = sign is used in the inequality then 20 <= Number of streetlights <= 100
Total cost = Cost per streetlight * Number of streetlights + Installation fee
Combining the inequalities: 25000 <= 500*x + 5000 <= 60000 and 20 <= x <= 100
Symbolic Form: [[25000 <= 500*x + 5000, 500*x + 5000 <= 60000, 20 <= x, x <= 100, x, solve]]

Word Problem:A conservation organization is planning to plant trees in a reforestation project. The cost of planting each tree is $7, and the organization plans to plant between 200 and 1,000 trees. Additionally, there is a setup fee of $500 for the project. The organization's budget for the project is between $2,000 and $10,000. What is the possible range of the number of trees the organization can plant while meeting both the cost constraints and the planting limits?

Break down the word problem into smaller information:
1. Our goal is to find the possible range of the number of trees the organization can plant while meeting both the cost constraints and the planting limits.
2. The cost of planting each tree is $7.
3. The organization plans to plant between 200 and 1,000 trees.
4. There is a setup fee of $500 for the project.
5. The organization's budget for the project is between $2,000 and $10,000.
Identify problem type: The organization plans to plant between 200 and 1,000 trees and the organization's budget for the project is between $2,000 and $10,000 sets the range of acceptable numbers of trees and costs for the organization. This implies the use of compound inequalities to solve the problem.
Define the variables and formulate the compound inequality:
Let x be the number of trees the organization can plant.
between $2,000 and $10,000 so the total cost is between 2000 and 10000 inclusive of the values so = sign is used in the inequality then 2000 <= Total cost <= 10000
The cost of planting each tree is $7 so the cost per tree is 7
The organization plans to plant between 200 and 1,000 trees so the number of trees planted is between 200 and 1000 inclusive of the values so = sign is used in the inequality then 200 <= Number of trees <= 1000
Total cost = Cost per tree * Number of trees + Setup fee
Combining the inequalities: 2000 <= 7*x + 500 <= 10000 and 200 <= x <= 1000
Symbolic Form: [[2000 <= 7*x + 500, 7*x + 500 <= 10000, 200 <= x, x <= 1000, x, solve]]

Word Problem:A tech startup is organizing a virtual conference and will distribute customized T-shirts to participants. The cost of producing each T-shirt is $8, and the startup plans to give away between 200 and 800 T-shirts. Additionally, there is a setup fee of $300 for the production. The startup's budget for the campaign is between $2200 and $6500. What is the possible range of the number of T-shirts the startup can produce while meeting both the cost constraints and the distribution limits?
Break down the word problem into smaller information:
1. Our goal is to find the possible range of the number of T-shirts the startup can produce while meeting both the cost constraints and the distribution limits.
2. The cost of producing each T-shirt is $8.
3. The startup plans to give away between 200 and 800 T-shirts.
4. There is a setup fee of $300 for the production.
5. The startup's budget for the campaign is between $2200 and $6500.
Identify problem type: The startup plans to give away between 200 and 800 T-shirts and the startup's budget for the campaign is between $2200 and $6500 sets the range of acceptable numbers of T-shirts and costs for the startup. This implies the use of compound inequalities to solve the problem.
Define the variables and formulate the compound inequality:
Let x be the number of T-shirts the startup can produce.
between $2200 and $6500 so the total cost is between 2200 and 6500 inclusive of the values so = sign is used in the inequality then 2200 <= Total cost <= 6500
The cost of producing each T-shirt is $8 so the cost per T-shirt is 8
The startup plans to give away between 200 and 800 T-shirts so the number of T-shirts produced is between 200 and 800 inclusive of the values so = sign is used in the inequality then 200 <= Number of T-shirts <= 800
Total cost = Cost per T-shirt * Number of T-shirts + Setup fee
Combining the inequalities: 2200 <= 8*x + 300 <= 6500 and 200 <= x <= 800
Symbolic Form: [[2200 <= 8*x + 300, 8*x + 300 <= 6500, 200 <= x, x <= 800, x, solve]]

"""

Third = """
Word Problem:Tom has been saving money for a new bike and has a budget of $240 to $320. He wants to buy a bike that costs 15% to 25% more than his budget for accessories and maintenance. If he receives a $20 discount coupon for the bike, how much can he expect to spend on the bike after the discount?
Break down the word problem into smaller information:
1. Our goal is to find the possible range of prices Tom can expect to spend on the bike after the discount.
2. Tom has a budget of $240 to $320.
3. He wants to buy a bike that costs 15% to 25% more than his budget for accessories and maintenance.
4. He receives a $20 discount coupon for the bike. 

Identify problem type: Tom has a budget of $240 to $320 sets the range of acceptable budgets for the bike. This implies the use of compound inequalities to solve the problem.
Define the variables and formulate the compound inequality:
Let x be the price of the bike after the discount.
He wants to buy a bike that costs 15% to 25% more than his budget for accessories and maintenance so the price of the bike is between 1.15*240 and 1.25*320
He receives a $20 discount coupon for the bike so the price after the discount is x - 20
Combining the inequalities and the discount: 1.15*240 - 20 <= x <= 1.25*320 - 20
Symbolic Form: [[1.15*240 - 20 <= x, x <= 1.25*320 - 20, x, solve]]

Word Problem:A local electronics store is offering a promotional discount of $50 on all high-definition televisions (HDTVs). Karen is considering purchasing an HDTV from the store, and the prices of the HDTVs range from $450 to $1200. What is the range of prices Karen can expect to pay after the promotional discount?
Break down the word problem into smaller information:
1. Our goal is to find the range of prices Karen can expect to pay after the promotional discount.
2. The prices of the HDTVs range from $450 to $1200.
3. The store is offering a promotional discount of $50 on all HDTVs.
Identify problem type: The prices of the HDTVs range from $450 to $1200 sets the range of acceptable prices for the HDTVs. This implies the use of compound inequalities to solve the problem.
Define the variables and formulate the compound inequality:
Let x be the price of the HDTV after the promotional discount.
The store is offering a promotional discount of $50 on all HDTVs so the price after the discount is x
The prices of the HDTVs range from $450 to $1200 so the lower bound of the price after the discount is 450 - 50 and the upper bound is 1200 - 50
Combining the inequalities and the discount: 450 - 50 <= x <= 1200 - 50
Symbolic Form: [[450 - 50 <= x, x <= 1200 - 50, x, solve]]

Word Problem:Sarah is planning a weekend getaway and wants to book a hotel room. Her budget for accommodation is between $180 and $250 per night. She's looking for a room that includes additional amenities, which typically cost 10% to 20% more than the base room rate. If she finds a promotional code that offers a $30 discount on the total price, what range of prices can Sarah expect to pay for the room per night after applying the discount?
Break down the word problem into smaller information:
1. Our goal is to find the range of prices Sarah can expect to pay for the room per night after applying the discount.
2. Sarah's budget for accommodation is between $180 and $250 per night.
3. She's looking for a room that includes additional amenities, which typically cost 10% to 20% more than the base room rate.
4. She finds a promotional code that offers a $30 discount on the total price.

Identify problem type: Sarah's budget for accommodation is between $180 and $250 per night sets the range of acceptable budgets for the room. This implies the use of compound inequalities to solve the problem.
Define the variables and formulate the compound inequality:
Let x be the price of the room per night after the promotional discount.
She's looking for a room that includes additional amenities, which typically cost 10% to 20% more than the base room rate so the price of the room is between 1.10*180 and 1.20*250
She finds a promotional code that offers a $30 discount on the total price so the price after the discount is x - 30
Combining the inequalities and the discount: 1.10*180 - 30 <= x <= 1.20*250 - 30
Symbolic Form: [[1.10*180 - 30 <= x, x <= 1.20*250 - 30, x, solve]]

Word Problem:A local recycling center wants to increase its plastic bottle collection. They currently collect between 1,200 and 1,500 bottles per week. The center aims to improve their collection by 10% to 20% in the coming months. If they implement a new program that adds an additional 100 bottles per week to their collection, how many plastic bottles can they expect to collect weekly after the improvement?
Break down the word problem into smaller information:
1. Our goal is to find the number of plastic bottles the recycling center can expect to collect weekly after the improvement.
2. The center currently collects between 1,200 and 1,500 bottles per week.
3. The center aims to improve their collection by 10% to 20%.
4. They implement a new program that adds an additional 100 bottles per week to their collection.

Identify problem type: The center currently collects between 1,200 and 1,500 bottles per week sets the range of acceptable collections for the recycling center. This implies the use of compound inequalities to solve the problem.
Define the variables and formulate the compound inequality:
Let x be the number of plastic bottles the recycling center can expect to collect weekly after the improvement.
The center currently collects between 1,200 and 1,500 bottles per week so the lower bound of the collection after the improvement is 1.10*1200 + 100 and the upper bound is 1.20*1500 + 100
Combining the inequalities and the additional bottles: 1.10*1200 + 100 <= x <= 1.20*1500 + 100
Symbolic Form: [[1.10*1200 + 100 <= x, x <= 1.20*1500 + 100, x, solve]]

"""
