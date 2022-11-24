# This is a file that contains the global variables for the calculator
# the reason this file exists is to make it easier to change the variables,
# and to make it easier to import the variables into other files
# in theory, this file should not be changed at all unless you want to
# add extra operators or operands
# Path: globals.py
# Author: @Eldar Aslanbeily


from operators import *

# TODO: when adding a new operator, add it to all of the sets and dictionaries below
# sets of possible math operators and operands
# those sets also act as a list of possible tokens for the equation
operators = ('+', '-', '*', '/', '^', '%', '$', '&', '@', '~', '!', '(', ')')
operands = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ' ')

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

# dictionary of functions for the operators
funcs_per_operator = {'+': addition,
                      '-': subtraction,
                      '*': multiplication,
                      '/': division,
                      '^': power,
                      '%': modulo,
                      '$': maximum,
                      '&': minimum,
                      '@': factorial,
                      '~': tilde,
                      '!': factorial}
