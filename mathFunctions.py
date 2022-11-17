# This is a file that contains the functions for the calculator
# Path: mathFunctions.py
# Author: @Eldar Aslanbeily

from math import pow


# adds a and b from string
def addition(a, b):
    return float(a) + float(b)


# subtracts b from a
def subtraction(a, b):
    return float(a) - float(b)


# multiplies a and b
def multiplication(a, b):
    return float(a) * float(b)


# divides a by b
def division(a, b):
    return float(a) / float(b)


# returns the modulo of a and b
def modulo(a, b):
    return float(a) % float(b)


# returns a to the power of b
def power(a, b):
    return pow(float(a), float(b))


# returns the maximum of a and b
def maximum(a, b):
    if float(a) > float(b):
        return float(a)
    else:
        return float(b)


# returns the minimum of a and b
def minimum(a, b):
    if float(a) < float(b):
        return float(a)
    else:
        return float(b)


# return the average of a and b
def average(a, b):
    return (float(a) + float(b)) / 2


# returns the negation of a
# for example, -5 is the tilde of 5
def tilde(a):
    return -float(a)


# returns the factorial of a
# factorial of 0 is 1
# factorial of 1 is 1
# factorial of negative numbers is not defined
# factorial of non-integer numbers is not defined
def factorial(a):
    if float(a) < 0:
        raise ValueError('Invalid input for factorial: {},'
                         ' factorial() not defined for negative values'.format(a))
    elif not float(a).is_integer():
        raise ValueError('Invalid input for factorial: {},'
                         ' factorial() not defined for non-integer values'.format(a))
    elif float(a) == 0 or float(a) == 1:
        return str(1)
    else:
        return str(int(float(a)) * int(float(factorial(float(a) - 1))))

print((factorial('87.0')))
