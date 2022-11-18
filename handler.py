# This is the main program for getting the equation from the user and printing the result
# This is a runner program that runs the calculator using the functions from the other files
# Path: handler.py
# Author: @Eldar Aslanbeily

# imports the functions from the other files
from operators import *
from functions import *

# TODO: when adding a new operator, add it to all of the sets and dictionaries below
# sets of possible math operators and operands
# those sets also act as a list of possible tokens for the equation
operators = ('+', '-', '*', '/', '^', '%', '$', '&', '@', '~', '!')
operands = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '(', ')', ' ')

# set of binary operators
# meaning that they take two operands in order to work
binary_operators = ('+', '-', '*', '/', '^', '%', '$', '&', '@')

# set of unary operators
# meaning that they take one operand in order to work
unary_operators = ('~', '!')

# dictionary of priorities for the operators
priority = {'+': 1, '-': 1,
            '*': 2, '/': 2,
            '^': 3,
            '%': 4,
            '$': 5, '&': 5, '@': 5,
            '~': 6, '!': 6}

# define the equation
input_equation = ""

# try and get equation from user and catch any exceptions
# try:
#     input_equation = input("Enter Equation:")
# except KeyboardInterrupt:
#     print("\n program was interrupted by user")


# check if equation is valid
input_equation = check_if_function_is_valid(input_equation, operators,
                                            operands, binary_operators,
                                            unary_operators, priority)

# simplify equation
input_equation = simplify_equation(input_equation)

# calculate the result
result = calculate_equation(input_equation, binary_operators, unary_operators, priority)

# print the result of the equation
# print("Result: {}".format(result))
