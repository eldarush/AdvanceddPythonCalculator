# This is a file that contains the functions for the calculator
# important note: any function within this file already takes into account
# that the input is valid, so there is no need to check for validity
# F.E the functions assume that there are no letters in the input,
# and that the input is not empty,
# or that there are no spaces in the input, etc.
# only exception is the factorial function,
# which checks for validity for its input
# Path: operators.py
# Author: @Eldar Aslanbeily

# imports the pow function from the math library
from math import pow


def addition(a: str, b: str) -> str:
    """
    adds a and b and returns the sum
    :param a:
    :param b:
    :return: a+b
    """
    # if both a and b are integers, return an integer
    if a.isdigit() and b.isdigit():
        return str(int(float(a)) + int(float(b)))

    # if either a or b is a float, return a float
    return str(float(a) + float(b))


def subtraction(a: str, b: str) -> str:
    """
    subtracts b from a and returns the difference
    :param a:
    :param b:
    :return: a-b
    """

    # if both a and b are integers, return an integer
    if a.isdigit() and b.isdigit():
        return str(int(float(a)) - int(float(b)))

    # if either a or b is a float, return a float
    return str(float(a) - float(b))


def multiplication(a: str, b: str) -> str:
    """
    multiplies a and b and returns the product
    :param a:
    :param b:
    :return: a*b
    """
    # if both a and b are integers, return an integer
    if a.isdigit() and b.isdigit():
        return str(int(float(a)) * int(float(b)))

    # if either a or b is a float, return a float
    return str(float(a) * float(b))


def division(a: str, b: str) -> str:
    """
    divides a by b and returns the quotient
    :param a:
    :param b:
    :return: a/b
    """
    return str(float(a) / float(b))


def modulo(a: str, b: str) -> str:
    """
    returns the modulo of a and b
    :param a:
    :param b:
    :return: a%b
    """

    # if both a and b are integers, return an integer
    if a.isdigit() and b.isdigit():
        return str(int(float(a)) % int(float(b)))

    # if either a or b is a float, return a float
    return str(float(a) % float(b))


def power(a: str, b: str) -> str:
    """
    returns a to the power of b
    :param a:
    :param b:
    :return: a^b (a**b)
    """
    # if both a and b are integers, return an integer
    if a.isdigit() and b.isdigit():
        return str(int(pow(float(a), float(b))))

    # if either a or b is a float, return a float
    return str(pow(float(a), float(b)))


def maximum(a: str, b: str) -> str:
    """
    returns the maximum of a and b
    :param a:
    :param b:
    :return: if a > b, return a, else return b
    """
    # if both a and b are integers, return an integer
    if a.isdigit() and b.isdigit():
        return str(int(float(a)) if float(a) > float(b) else int(float(b)))

    # if either a or b is a float, return a float
    return str(float(a) if float(a) > float(b) else float(b))


def minimum(a: str, b: str) -> str:
    """
    returns the minimum of a and b
    :param a:
    :param b:
    :return: if a < b, return a, else return b
    """
    # if both a and b are integers, return an integer
    if a.isdigit() and b.isdigit():
        return str(int(float(a)) if float(a) < float(b) else int(float(b)))

    # if either a or b is a float, return a float
    return str(float(a) if float(a) < float(b) else float(b))


def average(a: str, b: str) -> str:
    """
    returns the average of a and b
    :param a:
    :param b:
    :return: a+b/2
    """
    # if both a and b are even or odd, return an integer
    if (float(a) % 2 == 0 and float(b) % 2 == 0) or \
            (float(a) % 2 != 0 and float(b) % 2 != 0):
        return str(int((float(a) + float(b)) / 2))

    # if a is even and b is odd, or a is odd and b is even, return a float
    return str((float(a) + float(b)) / 2)


def tilde(a: str) -> str:
    """
    returns the negative of a
    for example, if a = 5, returns -5
    :param a:
    :return: -a
    """

    # if a is an integer, return an integer
    if a.isdigit():
        return str(-int(float(a)))

    # if a is a float, return a float
    return str(-float(a))


def factorial(a: str) -> str:
    """
    returns the factorial of a
    factorial of 0 is 1
    factorial of 1 is 1
    factorial of negative numbers is not defined
    factorial of non-integer numbers is not defined
    :param a:
    :return: a! (a*...*1)
    """

    # if a is smaller than 0, return an error
    if float(a) < 0:
        raise ValueError('Invalid input for factorial: {},'
                         ' factorial() not defined for negative values'.format(a))

    # if a is not an integer, return an error
    elif not float(a).is_integer():
        raise ValueError('Invalid input for factorial: {},'
                         ' factorial() not defined for non-integer values'.format(a))

    # if a is 0 or 1, return 1
    elif float(a) == 0 or float(a) == 1:
        return str(1)

    # if a is greater than 1, return a!
    # calling factorial recursively until a = 1
    else:
        return str(int(float(a)) * int(float(factorial(str(float(a) - 1)))))
