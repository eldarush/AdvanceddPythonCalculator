# This is a file that contains the functions for the calculator
# important note: any function within this file already takes into account
# that the input is valid, so there is no need to check for validity
# F.E the functions assume that there are no letters in the input,
# and that the input is not empty, or that there are no spaces in the input, etc.
# only exception is the factorial function, which checks for validity for its input
# Path: mathFunctions.py
# Author: @Eldar Aslanbeily

# imports the pow function from the math library
from math import pow


# adds a and b together and returns the sum
def addition(a: str, b: str) -> str:

    # if both a and b are integers, return an integer
    if a.isdigit() and b.isdigit():
        return str(int(float(a)) + int(float(b)))

    # if either a or b is a float, return a float
    return str(float(a) + float(b))


# subtracts b from a and returns the difference
def subtraction(a: str, b: str) -> str:

    # if both a and b are integers, return an integer
    if a.isdigit() and b.isdigit():
        return str(int(float(a)) - int(float(b)))

    # if either a or b is a float, return a float
    return str(float(a) - float(b))


# multiplies a by b and returns the product
def multiplication(a: str, b: str) -> str:

    # if both a and b are integers, return an integer
    if a.isdigit() and b.isdigit():
        return str(int(float(a)) * int(float(b)))

    # if either a or b is a float, return a float
    return str(float(a) * float(b))


# divides a by b and returns the quotient
def division(a: str, b: str) -> str:
    return str(float(a) / float(b))


# returns the modulo of a and b
def modulo(a: str, b: str) -> str:

    # if both a and b are integers, return an integer
    if a.isdigit() and b.isdigit():
        return str(int(float(a)) % int(float(b)))

    # if either a or b is a float, return a float
    return str(float(a) % float(b))


# returns a to the power of b
def power(a: str, b: str) -> str:

    # if both a and b are integers, return an integer
    if a.isdigit() and b.isdigit():
        return str(int(pow(float(a), float(b))))

    # if either a or b is a float, return a float
    return str(pow(float(a), float(b)))


# returns the maximum of a and b
def maximum(a: str, b: str) -> str:

    # if both a and b are integers, return an integer
    if a.isdigit() and b.isdigit():
        return str(int(float(a)) if float(a) > float(b) else int(float(b)))

    # if either a or b is a float, return a float
    return str(float(a) if float(a) > float(b) else float(b))


# returns the minimum of a and b
def minimum(a: str, b: str) -> str:
    # if both a and b are integers, return an integer
    if a.isdigit() and b.isdigit():
        return str(int(float(a)) if float(a) < float(b) else int(float(b)))

    # if either a or b is a float, return a float
    return str(float(a) if float(a) < float(b) else float(b))


# return the average of a and b
def average(a: str, b: str) -> str:

    # if both a and b are even or odd, return an integer
    if (float(a) % 2 == 0 and float(b) % 2 == 0) or (float(a) % 2 != 0 and float(b) % 2 != 0):
        return str(int((float(a) + float(b)) / 2))

    # if a is even and b is odd, or a is odd and b is even, return a float
    return str((float(a) + float(b)) / 2)


# returns the negation of a
# for example, -5 is the tilde of 5
def tilde(a: str) -> str:

    # if a is an integer, return an integer
    if a.isdigit():
        return str(-int(float(a)))

    # if a is a float, return a float
    return str(-float(a))


# returns the factorial of a
# factorial of 0 is 1
# factorial of 1 is 1
# factorial of negative numbers is not defined
# factorial of non-integer numbers is not defined
def factorial(a: str) -> str:
    if float(a) < 0:
        raise ValueError('Invalid input for factorial: {},'
                         ' factorial() not defined for negative values'.format(a))
    elif not float(a).is_integer():
        raise ValueError('Invalid input for factorial: {},'
                         ' factorial() not defined for non-integer values'.format(a))
    elif float(a) == 0 or float(a) == 1:
        return str(1)
    else:
        return str(int(float(a)) * int(float(factorial(str(float(a) - 1)))))
