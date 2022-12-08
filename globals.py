# This is a file that contains the global variables for the calculator
# the reason this file exists is to make it easier to change the variables,
# and to make it easier to import the variables into other files
# in theory, this file should not be changed at all unless you want to
# add extra operators or operands
# Path: globals.py
# Author: @Eldar Aslanbeily

# the list of operators that the calculator can use
from operators import *

# note: all the names of the operators are in uppercase
# because these are global variables, that do not change

# tuples of possible math operators and operands
# those tuples also act as a list of possible tokens for the equation
OPERATORS = ('+', '-', '*', '/', '^', '%', '$', '&', '@', '~', '!', '(', ')', '#')
OPERANDS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ' ', '\t', '\n')

# tuple of binary operators
# meaning that they take two operands in order to work
BINARY_OPERATORS = ('+', '-', '*', '/', '^', '%', '$', '&', '@')

# tuple of unary operators
# meaning that they take one operand in order to work
UNARY_OPERATORS = ('~', '!', '#')

# tuple of unary operators that are right associative
# meaning that they take one operand in order to work
# and that they work from right to left
RIGHT_ASSOCIATIVE_UNARY_OPERATORS = ('!', '#')

# tuple of unary operators that are left associative
# meaning that they take two operands in order to work
# and that they work from left to right
LEFT_ASSOCIATIVE_UNARY_OPERATORS = tuple('~')

# dictionary of priorities for the operators
PRIORITY = {'+': 1, '-': 1,
            '*': 2, '/': 2,
            '^': 3,
            '%': 4,
            '$': 5, '&': 5, '@': 5,
            '~': 6, '!': 6, '#': 6}

# dictionary of functions for the operators
FUNCTIONS_PER_OPERATOR = {'+': addition,
                          '-': subtraction,
                          '*': multiplication,
                          '/': division,
                          '^': power,
                          '%': modulo,
                          '$': maximum,
                          '&': minimum,
                          '@': average,
                          '~': tilde,
                          '!': factorial,
                          '#': sum_digits}
