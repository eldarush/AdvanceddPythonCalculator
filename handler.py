# This is the main program for getting the equation from the user and printing the result
# This is a runner program that runs the calculator using the functions from the other files
# Path: handler.py
# Author: @Eldar Aslanbeily

# only import the functions that are needed to run the calculator
from functions import get_equation_from_user, calculate


# get the equation from the user
input_equation = get_equation_from_user()

# run the calculator and print the result
calculate(input_equation)

# TODO: make (- 3) not valid because - is a part of the number and there
# TODO: is a space between the - and the 3 (do this in remove_spaces function)
