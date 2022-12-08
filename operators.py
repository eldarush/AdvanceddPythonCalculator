# This is a file that contains the functions for the calculator
# important note: any function within this file already takes into account
# that the input is valid, so there is no need to check for validity
# F.E the functions assume that there are no letters in the input,
# and that the input is not empty,
# or that there are no spaces in the input, etc.
# so we don't need to check value exceptions,
# or type exceptions, or index exceptions, etc.
# the only exceptions that we need to check for are
# math exceptions, like division by zero, or overflow errors
# if the number is too big for the calculator to handle
# also we don't want to get nan as a result, so we need to check for that
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
    # if both a and b are infinite,
    # but have different signs, print error message
    if a == "inf" and b == "-inf" or \
            a == "-inf" and b == "inf":
        raise ValueError("Invalid input: Cannot add"
              " infinity and negative infinity.")

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

    # if both a and b are infinite, print error message
    if a == "inf" and b == "inf" or a == "-inf" and b == "-inf":
        raise ValueError("Invalid input: Cannot subtract infinity from infinity.")

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

    # if one of the numbers is infinity,
    # and the other is zero, print error message
    if (a == "inf" or a == "-inf") and b == "0" or \
            (b == "inf" or b == "-inf") and a == "0":
        raise ValueError("Invalid input: Cannot multiply infinity by zero.")

    # try and multiply a and b
    try:
        # if both a and b are integers, return an integer
        if a.isdigit() and b.isdigit():
            return str(int(float(a)) * int(float(b)))

        # if either a or b is a float, return a float
        return str(float(a) * float(b))
    # if the result is too big, return an error message
    except OverflowError:
        raise ValueError("Error: Overflow - number too large for multiplication.")


def division(a: str, b: str) -> str:
    """
    divides a by b and returns the quotient
    only works if b is not 0
    :param a:
    :param b:
    :return: a/b
    """
    # check if b is zero
    if b == '0':
        raise ValueError("Math Error: Division by zero is "
              f"not allowed at Token: {a}/{b}.")

    # if both a and b are infinite, print error message
    if a == "inf" and b == "inf":
        raise ValueError("Invalid input: Cannot divide infinity by infinity.")

    # if both a and b are negative infinite, print error message
    if a == "-inf" and b == "-inf":
        raise ValueError("Invalid input: Cannot divide negative"
              " infinity by negative infinity.")

    # if a is infinite and b is negative infinite, print error message
    if a == "inf" and b == "-inf":
        raise ValueError("Invalid input: Cannot divide infinity by negative infinity.")

    # if a is negative infinite and b is infinite, print error message
    if a == "-inf" and b == "inf":
        raise ValueError("Invalid input: Cannot divide negative infinity by infinity.")

    return str(float(a) / float(b))


def modulo(a: str, b: str) -> str:
    """
    returns the modulo of a and b
    :param a:
    :param b:
    :return: a%b
    """

    # check if b is zero
    if b == 0:
        raise ValueError("Invalid input: Modulo by zero is not allowed."
              f" Cannot do {a}%{b}.")

    # check if a is infinite
    if a == "inf" or a == "-inf":
        raise ValueError("Invalid input: Modulo of infinity is not allowed.")

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
    :return: a^b (a to the power of b)
    """
    # if b is 0, return 1
    # this check already covers the case where a is 0
    # because 0^0 is agreed to be 1 (at lease according to wiki)
    # source: https://en.wikipedia.org/wiki/Zero_to_the_power_of_zero
    if b == '0':
        return "1"

    # if b is 1, return a
    if b == '1':
        return a

    # if a is 0, return 0
    if a == '0':
        return "0"

    # check if the user is trying to do power function
    # where the base is negative and the exponent is not an integer
    if float(a) < 0 and float(b) % 1 != 0:
        raise ValueError('Invalid input: Cannot do negative base to non-integer power. \n'
              'power is not defined for negative base and non-integer power. \n'
              f'Cannot do {a}^{b}.')
    try:
        # if both a and b are integers, return an integer
        if a.isdigit() and b.isdigit():
            return str(int(pow(float(a), float(b))))

        # if either a or b is a float, return a float
        return str(pow(float(a), float(b)))
    # if the result is too big, return an error message
    except OverflowError:
        raise ValueError('Math Error: Overflow - number too large for power'
              f' Cannot do {a}^{b}.')
    # if the result raises a type error, return an error message
    except TypeError:
        raise ValueError('TypeError: unsupported operand type(s) for power: \n'
              f'{type(a)} and {type(b)}. Cannot do {a}^{b}.')
    # if the result raises a value error, return an error message
    except ValueError as e:
        raise ValueError(f'ValueError: {e}. Cannot do {a}^{b}.')


def maximum(a: str, b: str) -> str:
    """
    returns the maximum of a and b
    :param a:
    :param b:
    :return: if a > b, return a, else return b
    """

    # check if one of the numbers is infinity
    if a == "inf" or b == "inf":
        return "inf"

    # check if one of the numbers is negative infinity
    if a == "-inf" or b == "-inf":
        return "-inf"

    # check if one of the numbers is not a number
    if a == "nan" or b == "nan":
        # print error message if one of the numbers
        # is not a number
        raise ValueError("Invalid input: Cannot find maximum of nan"
              " (Not A number).")

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

    # check if one of the numbers is infinity
    if a == "inf" and b != "inf":
        return b
    elif b == "inf" and a != "inf":
        return a

    # check if one of the numbers is negative infinity
    if a == "-inf" or b == "-inf":
        return "-inf"

    # check if one of the numbers is not a number
    if a == "nan" or b == "nan":
        # print error message if one of the numbers
        # is not a number
        raise ValueError("Invalid input: Cannot find minimum of nan"
              " (Not A number).")

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
    # try and divide a+b by 2
    try:
        # if both a and b are even or odd, return an integer
        if (float(a) % 2 == 0 and float(b) % 2 == 0) or \
                (float(a) % 2 != 0 and float(b) % 2 != 0):
            return str(int((float(a) + float(b)) / 2))

        # if a is even and b is odd, or a is odd and b is even, return a float
        return str((float(a) + float(b)) / 2)
    # if the result is too big, return an error message
    # if we reach this point, it means that the input is probably
    # too big for the computer to handle, for example "inf" that stands
    # for infinity
    except OverflowError:
        raise ValueError("Math Error: Overflow - number too large for average."
              f" Cannot do average of {a} and {b}.")


def tilde(a: str) -> str:
    """
    returns the negative of a
    for example, if a = 5, returns -5
    :param a:
    :return: -a
    """
    # check if a is infinity
    if a == "inf":
        return "-inf"

    # check if a is negative infinity
    if a == "-inf":
        return "inf"

    # check if a is not a number
    if a == "nan":
        # print error message if a is not a number
        raise ValueError("Invalid input: Cannot find negative of nan"
              " (Not A number).")

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
        raise ValueError(f'Invalid input for factorial: {a},'
              ' factorial() not defined for negative values')

    # if a is not an integer or infinity, return an error
    # if a is infinity, the check for infinity is done in the
    # second next if statement (check if bigger than 171)
    elif not float(a).is_integer() and a != "inf":
        raise ValueError(f'Invalid input for factorial: {a},'
              ' factorial() not defined for non-integer values')

    # if a is 0 or 1, return 1
    elif float(a) == 0 or float(a) == 1:
        return str(1)

    # the max value of a is 171, otherwise the result will be too big
    elif float(a) > 171:
        raise ValueError(f'Invalid input for factorial: {a},'
              ' factorial() not defined for values larger than 171')

    # if a is greater than 1, return a!
    # calling factorial recursively until a = 1
    else:
        return str(int(float(a)) *
                   int(float(factorial(str(float(a) - 1)))))


def sum_digits(equation: str) -> str:
    """
    returns the sum of the digits of the input
    this operation is only defined for positive numbers
    123# = 1+2+3 = 6
    123.456# = 1+2+3+4+5+6 = 21
    -3.14# = -(3+1+4) = -8
    :param equation:
    :return: the sum of the digits of the input
    """

    # check if the input is infinity
    if equation == "inf":
        return "inf"

    # check if the input is negative infinity
    if equation == "-inf":
        return "-inf"

    # check if the input is not a number
    if equation == "nan":
        # print error message if the input is not a number
        raise ValueError("Invalid input: Cannot find sum of digits of nan"
              " (Not A number).")

    # if input is 0, return 0
    if equation == "0":
        return "0"

    # if the input is positive, return the sum of the digits
    if float(equation) >= 0:
        # if the input is an integer, return the sum of the digits
        if float(equation).is_integer():
            return str(sum(int(digit) for digit in equation if digit.isdigit()))
        # if the input is a float, return the sum of the digits of the
        # integer part and the sum of the digits of the decimal part
        elif not float(equation).is_integer():
            return str(sum(int(digit) for digit in equation.split('.')[0]
                           if digit.isdigit()) +
                       sum(int(digit) for digit in equation.split('.')[1]
                           if digit.isdigit()))

    # if the input is negative, print an error message
    elif float(equation) < 0:
        raise ValueError(f'Invalid input for sum_digits: {equation},'
              ' sum_digits() not defined for negative values')
