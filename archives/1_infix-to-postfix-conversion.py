# Stack 
# infix to postfix conversion using Stack

'''
Algorithm:
1. Scan the infix expression from left to right.
2. If the scanned character is an operand, output it.
3. Else,
…..3.1 If the precedence of the scanned operator is greater than the precedence of the operator in the stack(or the stack is empty or the stack contains a ‘(‘ ), push it.
…..3.2 Else, Pop all the operators from the stack which are greater than or equal to in precedence than that of the scanned operator. After doing that Push the scanned operator to the stack. (If you encounter parenthesis while popping then stop there and push the scanned operator in the stack.)
4. If the scanned character is an ‘(‘, push it to the stack.
5. If the scanned character is an ‘)’, pop the stack and and output it until a ‘(‘ is encountered, and discard both the parenthesis.
6. Repeat steps 2-6 until infix expression is scanned.
7. Print the output
8. Pop and output from the stack until it is not empty.
'''

# Class to convert the expression
class Conversion:

    # Construction to initialize the class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        # This array is used a stack
        self.array = []
        # Precedence setting
        self.output = []
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}

    # check if the stack is empty
    def isEmpty(self):
        return True if self.top == -1 else False

    # Return the value of the top of the stack
    def peek(self):
        return self.array[-1]

    # Pop the element from the stack
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"

    # Push the element to the stack 
    def push(self, op): 
        self.top += 1
        self.array.append(op) 

    # utility function to check if the given character is operand
    def isOperand(self, ch):
        return ch.isalpha()

    # Check if the precedence of the operator is strictly less than top of the stack or not
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False

    # The main function that converts given infix expression to postfix expression
    def infixToPostfix(self, exp):

        # Iterate over the expression for conversion
        for i in exp:
            # If the character is an operand, add it to output
            if self.isOperand(i):
                self.output.append(i)
                #print(i)
            # If the character is an '(', push it to stack
            elif i == '(':
                self.push(i)

            # If the scanned character is an ')', pop and out from the stack until '(' is found
            elif i == ')':
                while( (not self.isEmpty()) and self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()

            # An operator is encountered
            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)

        # pop all the operator from the stack
        while not self.isEmpty():
            self.output.append(self.pop())

        print ("".join(self.output))

# Driver program to test above functin
exp = "a+b*(c^d-e)^(f+g*h)-i"
obj = Conversion(len(exp))
obj.infixToPostfix(exp)


'''# Python program to convert infix expression to postfix 

# Class to convert the expression 
class Conversion: 
	
	# Constructor to initialize the class variables 
	def __init__(self, capacity): 
		self.top = -1
		self.capacity = capacity 
		# This array is used a stack 
		self.array = [] 
		# Precedence setting 
		self.output = [] 
		self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3} 
	
	# check if the stack is empty 
	def isEmpty(self): 
		return True if self.top == -1 else False
	
	# Return the value of the top of the stack 
	def peek(self): 
		return self.array[-1] 
	
	# Pop the element from the stack 
	def pop(self): 
		if not self.isEmpty(): 
			self.top -= 1
			return self.array.pop() 
		else: 
			return "$"
	
	# Push the element to the stack 
	def push(self, op): 
		self.top += 1
		self.array.append(op) 

	# A utility function to check is the given character 
	# is operand 
	def isOperand(self, ch): 
		return ch.isalpha() 

	# Check if the precedence of operator is strictly 
	# less than top of stack or not 
	def notGreater(self, i): 
		try: 
			a = self.precedence[i] 
			b = self.precedence[self.peek()] 
			return True if a <= b else False
		except KeyError: 
			return False
			
	# The main function that converts given infix expression 
	# to postfix expression 
	def infixToPostfix(self, exp): 
		
		# Iterate over the expression for conversion 
		for i in exp: 
			# If the character is an operand, 
			# add it to output 
			if self.isOperand(i): 
				self.output.append(i) 
			
			# If the character is an '(', push it to stack 
			elif i == '(': 
				self.push(i) 

			# If the scanned character is an ')', pop and 
			# output from the stack until and '(' is found 
			elif i == ')': 
				while( (not self.isEmpty()) and self.peek() != '('): 
					a = self.pop() 
					self.output.append(a) 
				if (not self.isEmpty() and self.peek() != '('): 
					return -1
				else: 
					self.pop() 

			# An operator is encountered 
			else: 
				while(not self.isEmpty() and self.notGreater(i)): 
					self.output.append(self.pop()) 
				self.push(i) 

		# pop all the operator from the stack 
		while not self.isEmpty(): 
			self.output.append(self.pop()) 

		print ("".join(self.output))

# Driver program to test above function 
exp = "a+b*(c^d-e)^(f+g*h)-i"
obj = Conversion(len(exp)) 
obj.infixToPostfix(exp) 

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) '''
