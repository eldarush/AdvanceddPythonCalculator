# This is the main program for getting the equation from the user and printing the result
# Path: main.py
# Author: @Eldar Aslanbeily

from mathFunctions import *
from generalEquationFunctions import *

# sets of possible math operators and operands
operators = ('+', '-', '*', '/', '^', '%', '$', '&', '@', '~', '!')
operands = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '(', ')', ' ')

# dictionary of priorities for the operators
priority = {'+': 1, '-': 1,
            '*': 2, '/': 2,
            '^': 3,
            '%': 4,
            '$': 5, '&': 5, '@': 5,
            '~': 6, '!': 6}

input_equation = input("Enter Equation:")

# check if equation is valid
check_if_function_is_valid(input_equation, operators, operands)

# get rid of extra parentheses
get_rid_of_extra_parentheses(input_equation)

# convert equation to list of tokens (operators and operands) and remove spaces
equation = input_equation.replace(' ', '')
equation = list(equation)
print(equation)
