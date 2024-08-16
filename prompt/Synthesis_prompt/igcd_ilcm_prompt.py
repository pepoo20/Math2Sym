Math_Teacher_Prompt = """I want you to act as Math Teacher. Your goal is to create high quality math problems to help students learn math.You will be given a math question. Please create a new question based on the Given Problems and following principles. Then transform the new question to Symbolic Form.

You must followed these principles:
1. Do not solve the problem.
2. Create only one new problem similar to the given problem.
3. Follow the same format as the given problem.
4. Do not explain the problem.
5. Transform the problem to Symbolic Form.

""".strip()

IGCD_Word_Prompt = Math_Teacher_Prompt + """
Task: Create a new word problem for greatest common divisor problem and Transform the problem to an Symbolic Form. Be as creative as possible try to use any kind of topics for variation.
You will get rewarded for reasonable and variety of the word problems.

Your output must be in the following format:
Word Problem: [Your Word Problem]
Find the greatest common factor of [Numbers].
Symbolic Form: [[Numbers, igcd]]

Word Problem:Find the greatest possible length that can be used to measure exactly the lengths 84 feet, 98 feet and 126 feet.
Find the greatest common factor of 84, 98 and 126.
Symbolic Form: [[84, 98, 126, igcd]]

Word Problem: A warehouse has three shelves that can hold 8, 12, or 16 skateboards. Each shelf has sections holding the same number of skateboards. What is the greatest number of skateboards that can be put in a section?
Find the greatest common factor of 8, 12 and 16.
Symbolic Form: [[8, 12, 16, igcd]]

Word Problem: A summer camp has 24 boys and 36 girls enrolled. The camp organizers want to divide the campers into groups for various activities, with each group having an equal number of campers and an equal number of boys and girls. What is the greatest number of groups the organizers can form while satisfying these conditions?
Find the greatest common factor of 24 and 36.
Symbolic Form: [[24, 36, igcd]]

Word Problem: Two numbers are in the ratio 2 : 3. If the second number is 27, find their greatest common factor.
Given the second number is 27 and the ratio is 2:3. the first number is 2/3*27 = 18
Find the greatest common factor of 18 and 27.
Symbolic Form: [[18, 27, igcd]]

Word Problem: Kiara baked 30 oatmeal cookies and 48 chocolate chip cookies to package in plastic containers for her friends at school. She wants to divide the cookies into identical containers so that each container has the same number of each kind of cookie. If she wants each container to have the greatest number of cookies possible, how many plastic containers does she need?
Find the greatest common factor of 30 and 48.
Symbolic Form: [[30, 48, igcd]]

Word Problem: A motorcycle dealership has 30 Yamaha R1s and 42 Honda CBRs in their inventory. The dealership wants to arrange the motorcycles in rows so that each row contains the same number of motorcycles and an equal number of each motorcycle type. What is the greatest number of rows that can be formed under these conditions?
Find the greatest common factor of 30 and 42.
Symbolic Form: [[30, 42, igcd]]

Word Problem: Sara has 16 red flowers and 24 yellow flowers. She wants to make bouquets with the same number of each color flower in each bouquet. What is the greatest number of bouquets she can make?
Find the greatest common factor of 16 and 24.
Symbolic Form: [[16, 24, igcd]]

Word Problem:
"""

ILCM_Word_Prompt = Math_Teacher_Prompt + """
Task: Create an new word problem for least common multiple problem and Transform the problem to an Symbolic Form. Be as creative as possible try to use any kind of topics for variation.
Create ONLY ONE Word Problem.You will get rewarded for reasonable and diverse of the word problems. 

Word Problem: Omar is planting trees. He has enough trees to plant 6, 7, or 14 trees in each row. What is the least number of trees Omar could have ?
Find the least common multiple of 6, 7 and 14.
Symbolic Form: [[6, 7, 14, ilcm]]

Word Problem: Two numbers are in the ratio 4 : 7. If the second number is 35, find their least common multiple.
Given the second number is 35 and the ratio is 4:7. the first number is 4/7*35 = 20
Find the least common multiple of 20 and 35.
Symbolic Form: [[20, 35, ilcm]]

Word Problem: Six bells commence tolling together and toll at intervals of 2, 4, 6, 8 10 and 12 seconds respectively. In 30 minutes, how many times do they toll together ? (excluding the one at start)
Find the least common multiple of 2, 4, 6, 8, 10 and 12.
Symbolic Form: [[2, 4, 6, 8, 10, 12, ilcm]]

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

Word Problem:Today, both the soccer team and the basketball team had games. The soccer team plays every three days, and the basketball team plays every five days. When will both teams have games on the same day again?
Find the least common multiple of 3 and 5.
Symbolic Form: [[3, 5, ilcm]]


Word Problem:
"""

temp = """
Word Problem: The Line A bus arrives at the bus stop every 25 minutes, and the Line B bus arrives every 15 minutes. They are both at the bus stop right now. In how many minutes will they both be at the bus stop again ?
Find the least common multiple of 25 and 15.
Symbolic Form: [[25, 15, ilcm]]
"""