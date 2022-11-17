# This is the main program for getting the equation from the user and printing the result
# Path: main.py
# Author: @Eldar Aslanbeily

# sets of possible math operators and operands
operators = set('+', '-', '*', '/', '^', '%', '$', '&', '@', '~', '!')
operants = set('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '(', ')')

# map of proirities for the operators
priority = {'+': 1, '-': 1,
            '*': 2, '/': 2,
            '^': 3,
            '%': 4,
            '$': 5, '&': 5, '@': 5,
            '~': 6, '!': 6}

input_equation = input("Enter Equation:")

# check if equation is valid
for x in input_equation:
    if x not in operators and x not in operants:
        raise Exception('Invalid token: {}'.format(x))

# check if equation is balanced
if input_equation.count('(') != input_equation.count(')'):
    raise Exception('Invalid syntax on token {}'.format(input_equation))

# check if ) appears  before ( 
if input_equation.find(')') < input_equation.find('('):
    raise Exception('Invalid syntax on token {}'.format(input_equation))

print(eval(input_equation))