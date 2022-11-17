# This is a file that contains the functions for the calculator
# Path: mathFunctions.py
# Author: @Eldar Aslanbeily

from math import factorial


# adds a and b
def addition(a, b):
    return a + b


# subtracts b from a
def subtraction(a, b):
    return a - b


# multiplies a and b
def multiplication(a, b):
    return a * b


# divides a by b
def division(a, b):
    return a / b


# returns the modulo of a and b
def modulo(a, b):
    return a % b


# returns a to the power of b
def power(a, b):
    return pow(a, b)


# returns the maximum of a and b
def maximum(a, b):
    if a > b:
        return a
    else:
        return b


# returns the minimum of a and b
def minimum(a, b):
    if a < b:
        return a
    else:
        return b


# return the average of a and b
def average(a, b):
    return (a + b) / 2


# returns the negation of a
# for example, -5 is the tilde of 5
def tilde(a):
    return -a


# returns the factorial of a
# factorial of 0 is 1
# factorial of 1 is 1
# factorial of negative numbers is not defined
def factorial(a):
    if a < 0:
        raise ValueError('Invalid input for factorial: {},'
                         ' factorial() not defined for negative values'.format(a))
    if a == 0:
        return 1
    else:
        return a * factorial(a - 1)
