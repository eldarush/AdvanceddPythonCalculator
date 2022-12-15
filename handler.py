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


