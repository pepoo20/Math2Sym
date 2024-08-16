Math_Teacher_Prompt = """I want you to act as Math Teacher. Your goal is to create high quality math problems to help students learn math.You will be given a math question. Please create a new question based on the Given Problems and following principles. Then transform the new question to Symbolic Form.

You must followed these principles:
1. Do not solve the problem.
2. Create only one new problem similar to the given problem.
3. Follow the same format as the given problem.
4. Do not explain the problem.
5. Transform the problem to Symbolic Form.

Your output should be in the following format:
Topic: <Topic>
Word Problem: <Your created word problem>
Break down the word problem into smaller information: <information>
Identify problem type: <Determining the type of problem>
Symbolic Form: <Symbolic Form>
"""
igcd =Math_Teacher_Prompt+ """
Task: Create a new word problem for greatest common divisor problem and Transform the problem to an Symbolic Form. Be as creative as possible try to use any kind of topics for variation.
You will get rewarded for reasonable and variety of the word problems.

Topic: Summer Camp
Word Problem: A summer camp has 24 boys and 36 girls enrolled. The camp organizers want to divide the campers into groups for various activities, with each group having an equal number of campers and an equal number of boys and girls. What is the greatest number of groups the organizers can form while satisfying these conditions?

Break down the word problem into smaller information:
1. Our goal is to find the greatest number of groups the organizers can form.
2. The summer camp has 24 boys and 36 girls enrolled.
3. The camp organizers want to divide the campers into groups for various activities.
4. Each group should have an equal number of boys and girls.
Identify problem type: The problem states that the camp organizers want to divide the campers into groups with an equal number of campers. This suggests that we need to find a number that divides both the number of boys - 24 and the number of girls - 36 evenly, the problem also specifies that each group should have an equal number of boys and girls so we need to equal division and distribution among the groups.Additionally, the problem asks for the greatest number of groups that can be formed, indicating that we should use the greatest common divisor to determine the maximum number of groups that can be created while maintaining equal distribution.
Find the greatest common factor of 24 and 36.
Symbolic Form: [[24, 36, igcd]]

Topic: Ratios and Numbers
Word Problem: Two numbers are in the ratio 2 : 3. If the second number is 27, find their greatest common factor.

Break down the word problem into smaller information:
1. Our goal is to find the greatest common factor of two numbers.
2. The numbers are in the ratio 2 : 3.
3. The second number is 27.
Identify problem type: The problem states that the two numbers are in the ratio 2 : 3 and provides the value of the second number as 27. This implies that we need to find the first number based on the given ratio and then determine the greatest common factor between the two numbers. The problem asks for the greatest common factor, indicating that we should use the greatest common divisor to find the largest number that divides both numbers evenly.
Given the second number is 27 and the ratio is 2:3. the first number is (2/3)*27 
Find the greatest common factor of (2/3)*27 and 27.
Symbolic Form: [[(2/3)*27, 27, igcd]]

Topic: Motorcycle Inventory
Word Problem: A motorcycle dealership has 30 Yamaha R1s and 42 Honda CBRs in their inventory. The dealership wants to arrange the motorcycles in rows so that each row contains the same number of motorcycles and an equal number of each motorcycle type. What is the greatest number of rows that can be formed under these conditions?

Break down the word problem into smaller information:
1. Our goal is to find the greatest number of rows that can be formed.
2. The motorcycle dealership has 30 Yamaha R1s and 42 Honda CBRs.
3. The dealership wants to arrange the motorcycles in rows.
4. Each row should contain the same number of motorcycles and an equal number of each motorcycle type.
Identify problem type: The problem states that the dealership wants to arrange the motorcycles in rows with an equal number of motorcycles and an equal number of each motorcycle type. This suggests that we need to find a number that divides both the number of Yamaha R1s - 30 and the number of Honda CBRs - 42 evenly. Additionally, the problem asks for the greatest number of rows that can be formed, indicating that we should use the greatest common divisor to determine the maximum number of rows that can be created while maintaining equal distribution among the motorcycles.
Find the greatest common factor of 30 and 42.
Symbolic Form: [[30, 42, igcd]]

Word Problem: Sara has 16 red flowers and 24 yellow flowers. She wants to make bouquets with the same number of each color flower in each bouquet. What is the greatest number of bouquets she can make?

Break down the word problem into smaller information:\newline 1. Our goal is to find the greatest number of bouquets Sara can make.\newline 2. Sara has 16 red flowers and 24 yellow flowers.\newline 3. She wants to make bouquets with the same number of each color flower.\newline Identify problem type: The problem involves making bouquets with an equal number of red and yellow flowers. The phrase same number of each color flower indicates equal distribution among the bouquets. The question asks for the greatest number of bouquets Sara can make, suggesting that we need to find the greatest common factor of the given quantities to determine the maximum number of bouquets that can be created while maintaining equal distribution among the flowers.\newline Find the greatest common factor of 16 and 24.\newline Symbolic Form: [[16, 24, igcd]]


Topic: Musical Instruments
Word Problem:Two friends, Alice and Bob, are practicing playing their musical instruments together. They start playing at the same time and play a synchronized note every 60 seconds. If Alice plays a solo note every 6 seconds, how often does Bob play a solo note?

Break down the word problem into smaller information:
1. Our goal is to find how often Bob plays a solo note.
2. Alice and Bob play synchronized notes every 60 seconds.
3. Alice plays a solo note every 6 seconds.
Identify problem type: The problem describes two friends, Alice and Bob, playing their musical instruments together. The phrase synchronized notes every 60 seconds indicates that both friends play together at regular intervals. The question asks how often Bob plays a solo note, suggesting that we need to find the least common multiple of the time intervals to determine the frequency of Bob's solo notes.
Find the least common multiple of 60 and 6.
Symbolic Form: [[60, 6, ilcm]]

Word Problem: 
""".strip()
ilcm = Math_Teacher_Prompt + """
Task: Create an new word problem for least common multiple problem and Transform the problem to an Symbolic Form. Be as creative as possible try to use any kind of topics for variation.
Create ONLY ONE Word Problem.You will get rewarded for reasonable and diverse of the word problems.

Topic: Finding number
Word Problem: Two numbers are in the ratio 4 : 7. If the second number is 35, find their least common multiple.

Break down the word problem into smaller information:
1. Our goal is to find the least common multiple of two numbers.
2. The numbers are in the ratio 4 : 7.
3. The second number is 35.
Identify problem type: The problem states that the two numbers are in the ratio 4 : 7 and provides the value of the second number as 35. This implies that we need to find the first number based on the given ratio and then determine the least common multiple between the two numbers. The problem asks for the least common multiple, indicating that we should use the least common multiple to find the smallest number that is a multiple of both numbers.
Given the second number is 35 and the ratio is 4:7. the first number is (4/7)*35
Find the least common multiple of (4/7)*35 and 35.
Symbolic Form: [[(4/7)*35, 35, ilcm]]

Topic: Bell Tolls Together
Word Problem: Six bells commence tolling together and toll at intervals of 2, 4, 6, 8 10 and 12 seconds respectively. In 30 minutes, how many times do they toll together ? (excluding the one at start)

Break down the word problem into smaller information:
1. Our goal is to find the number of times the bells toll together.
2. Six bells commence tolling together.
3. The bells toll at intervals of 2, 4, 6, 8, 10, and 12 seconds.
4. The problem asks for the number of times they toll together in 30 minutes.
Identify problem type: The problem describes six bells that commence tolling together and toll at different intervals. The question asks for the number of times they toll together in 30 minutes a common occurrence. As the bells toll at different intervals, we need to find the least common multiple of the given intervals to determine when they will toll together again.
Find the least common multiple of 2, 4, 6, 8, 10, and 12.
Symbolic Form: [[2, 4, 6, 8, 10, 12, ilcm]]

Topic: Boxes Stacking
Word Problem:Boxes that are 12 inches tall are being piled next to boxes that are 10 inches tall. What is the least height in feet at which the two piles will be the same height?

Break down the word problem into smaller information:
1. Our goal is to find the least height at which the two piles will be the same height.
2. The boxes are 12 inches tall and 10 inches tall.
Identify problem type: The problem involves stacking boxes of different heights - 12 inches and 10 inches. The question asks for the least height at which the two piles will be the same height, indicating that we need to find the least common multiple of the given heights to determine the minimum height at which the two piles will have the same height.
Find the least common multiple of 12 and 10.
Symbolic Form: [[12, 10, ilcm]]

Topic: Garden Lights
Word Problem:Imagine there are two sets of decorative lights in a garden, set to blink at different intervals. The first set of lights blinks every 15 seconds, while the second set blinks at a slower, unknown rate. Both sets of lights blink together for the first time 90 seconds after they are turned on.If the first set of lights blinks every 15 seconds, how often does the second set of lights blink?

Break down the word problem into smaller information:
1. Our goal is to find how often the second set of lights blinks.
2. The first set of lights blinks every 15 seconds.
3. Both sets of lights blink together for the first time 90 seconds after they are turned on.
Identify problem type: The problem involves two sets of decorative lights blinking at different intervals. The phrase both sets of lights blink together for the first time indicates that the lights will synchronize at a specific time. The question asks how often the second set of lights blinks, suggesting that we need to find the least common multiple of the time intervals to determine the frequency of the second set's blinks.
Find the least common multiple of 15 and 90.
Symbolic Form: [[15, 90, ilcm]]

Word Problem:Today, both the soccer team and the basketball team had games. The soccer team plays every three days, and the basketball team plays every five days. When will both teams have games on the same day again?

Break down the word problem into smaller information:\newline 1. Our goal is to find when both teams will have games on the same day again.\newline 2. The soccer team plays every three days.\newline 3. The basketball team plays every five days.\newline Identify problem type: The problem involves two teams, the soccer team, and the basketball team, playing games at different intervals. The question asks when both teams will have games on the same day again, indicating that we need to find the least common multiple of the time intervals to determine when the teams will play on the same day.\newline Find the least common multiple of 3 and 5.\newline Symbolic Form: [[3, 5, ilcm]]

Word Problem:
"""
