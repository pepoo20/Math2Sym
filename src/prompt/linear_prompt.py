Math_Teacher_Prompt = """I want you to act as Math Teacher. Your objective is to rewrite a given equation into a more complex version to make it a bit harder to handle. But the rewritten prompt must be reasonable and must be understood and responded to by humans. After that Simplify equation and transform it to Symbolic Form.
You must followed these principles:
1. Do not solve the equation.
2. Generate a similar but new Word Problem according to the Given Word Problem.
3. Ensure the new Word Problem only asks for one thing, be reasonable and can be answered with only a number (float or integer). For example, DO NOT ask, 'what is the amount of A, B and C?'
4. You MUST have the * symbol between the number and the variable. For example, 2*x, 3*y, 4*z etc.
5. The Symbolic Form ONLY accepts variables and equation. For example, [[2*x, 3*x - 5 , x , solve]]

""".strip()
WordProblem = """
I want you to act as Math Teacher. Your goal is to create high quality math word problems that can be represented by the linear equation to help students learn math. Then transform the word problem to an equation and Symbolic Form.

Word Problem:
"Seven times the number is 36 less than 10 times the number. Find the number."
Define the variable and formulate the equation based on the word problem:
Let's say the number is represented by variable x.
"Seven times the number" can be represented as: 7*x
"36 less than 10 times the number" can be represented as: 10*x - 36
Formulate the equation based on the word problem: 7*x = 10*x - 36
Equation: 7*x = 10*x - 36
Symbolic Form: [[7*x, 10*x - 36 , x , solve]]

Word Problem:
"Sophia finished 2/3 of a book.She calculated that she finished 90 more pages than she has yet to read. How long is her book?"
Define the variable and formulate the equation based on the word problem:
Let's say the number of pages in the book is represented by variable p.
"2/3 of a book" can be represented as: (2/3)*p
"90 more pages than she has yet to read" can be represented as: p - 90
Formulate the equation based on the word problem: (2/3)*p = p - 90
Equation: (2/3)*p = p - 90
Symbolic Form: [[(2/3)*p, p - 90 , p , solve]]

Word Problem:
The perimeter of a rectangle is 44. The length is 5 less than double the width.Find the length.
Define the variable and formulate the equation based on the word problem:
Let's denote the width of the rectangle as variable w and the length as variable l.
The perimeter of a rectangle can be represented as: 2*(l + w)
Given that the perimeter of the rectangle is 44, the equation becomes: 2*(l + w) = 44
The length is 5 less than double the width, so we can represent the length as: 2*w - 5
Formulate the equation based on the word problem: 2*(2*w - 5 + w) = 44
Equation: 2*(2*w - 5 + w) = 44
Symbolic Form: [[2*(2*w - 5 + w), 44 , w , solve]]

Word Problem:
A company produces widgets at a rate of 25 per hour. However, due to a technical glitch, they are currently producing 15 fewer widgets per hour than usual. If they have produced 500 widgets less than they planned by the end of the day, how many hours did they work?
Define the variable and formulate the equation based on the word problem:
Let's denote the number of hours worked as variable h.
The number of widgets they planned to produce can be represented as: 25*h
Due to the technical glitch, they are producing 15 fewer widgets per hour, so the actual production rate is: 25 - 15 = 10 widgets per hour.
The actual number of widgets produced is: 10*h
They produced 500 widgets less than planned, so the equation becomes: 25*h - 10*h = 500
Formulate the equation based on the word problem: 25*h - 10*h = 500
Equation: 25*h - 10*h = 500
Symbolic Form: [[25*h - 10*h, 500, h, solve]]

Word Problem:
"If a farmer wants to plough a farm field on time, he must plough 120 hectares a day. For technical reasons he ploughed only 85 hectares a day, hence he had to plough 2 more days than he planned and he still has 40 hectares left.How many days the farmer planned to work initially?"
Define the variable and formulate the equation based on the word problem:
Let's denote the number of days the farmer planned to work initially as variable d.
The number of hectares the farmer planned to plough initially can be represented as: 120*d
Due to technical reasons, he could only plough 85 hectares per day. He worked for ( d + 2 ) days and still had 40 hectares left. So, the actual area ploughed is: 85*(d + 2) + 40
Formulate the equation based on the word problem: 120*d = 85*(d + 2) + 40
Equation: 120*d = 85*(d + 2) + 40
Symbolic Form: [[120*d, 85*(d + 2) + 40 , d , solve]]

Word Problem:
""".strip()
