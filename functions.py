# This is a file that contains general functions for the equation
# Path: functions.py
# Author: @Eldar Aslanbeily

from globals import *


def get_equation_from_user() -> str:
    """
    function that gets an equation from the user
    and if the user stops the program,
    print a message and exit the program
    :return:
    """
    input_equation = ""
    try:
        input_equation = input("Enter Equation:")
        # if the user stops the program
    except KeyboardInterrupt:
        print("\n Program was interrupted by user")
        exit()

    return input_equation


def calculate(equation: str) -> None:
    """
    function that runs the checks and calculates the equation
    this is a function that is used by tne handler file which
    is accessed by the user
    :param equation:
    :return: result of the equation
    """

    # check if equation is valid
    equation = check_if_function_is_valid(equation, OPERATORS,
                                          OPERANDS, BINARY_OPERATORS,
                                          UNARY_OPERATORS, RIGHT_ASSOCIATIVE_UNARY_OPERATORS,
                                          LEFT_ASSOCIATIVE_UNARY_OPERATORS)

    # calculate the result
    result_of_calc = calculate_equation(equation, BINARY_OPERATORS,
                                        UNARY_OPERATORS, PRIORITY,
                                        OPERANDS, OPERATORS, RIGHT_ASSOCIATIVE_UNARY_OPERATORS,
                                        LEFT_ASSOCIATIVE_UNARY_OPERATORS)

    # print the result of the equation
    print("Result: {}".format(result_of_calc))


def is_number(s: str) -> bool:
    """
    simple function that checks if a string is a number
    this function receives a string and returns
    true if the string is a number and false otherwise
    :param s:
    :return:
    """

    # try to convert the string to a float, if it works then it is a number
    try:
        float(s)
        return True

    # if the string is not a number, then return false
    except ValueError:
        return False


def doesnt_contain_numbers(equation: str) -> bool:
    """
    This function checks if an equation contains numbers
    :param equation:
    :return:
    """
    for x in equation:

        # if the equation contains a number than return false
        if is_number(x):
            return False

    # if the equation doesn't contain a number than return true
    return True


def function_doesnt_contain_numbers(equation: str) -> str:
    """
    function that checks if a function doesn't contain numbers
    simply by running the function doesnt_contain_numbers
    :param equation:
    :return: equation if the function doesn't contain numbers
    """
    # check if the equation doesn't contain numbers
    if doesnt_contain_numbers(equation):
        print('Invalid syntax - equation does not contain numbers')
        exit()

    # if the equation contains numbers, then return the equation
    return equation


def parentheses_surrounding_validity(equation: str) -> str:
    """
    function that checks if the surrounding of parentheses
    are valid, meaning that there are no numbers or closing parentheses
    before an opening parentheses and there are no opening parentheses
    or numbers after a closing parentheses, in a regular equation
    5(3+4) is valid and would be 5*(3+4), but in this calculator
    5(3+4) is invalid and would print an error message
    For example: 2(3) is not valid
    or 2(3+4)5 is not valid but 2*(3+4)-5 is valid
    :param equation:
    :return: true if there is a number after a closing parentheses
    and false otherwise
    """

    # go over equation and check if there is a number
    # after a closing parentheses
    for x in range(len(equation) - 1):
        # if there is a number or opening parentheses
        # after a closing parentheses in the middle of the equation
        if equation[x] == ')' and x != len(equation) - 1:
            if is_number(equation[x + 1]) or equation[x + 1] == '(':
                print("Invalid syntax - number or opening parentheses"
                      " after a closing parentheses")
                exit()
        # if there is closing parentheses at the end of the equation
        # then we don't need to check if there is invalid character
        # after the closing parentheses
        elif equation[x] == ')' and x == len(equation) - 1:
            pass
        elif equation[x] == '(' and x != 0:
            if is_number(equation[x - 1]) or equation[x + 1] == ')':
                print("Invalid syntax - number or closing parentheses"
                      " before an opening parentheses")
                exit()
        # if there is closing parentheses at the end of the equation
        # then we don't need to check if there is invalid character
        # after the closing parentheses
        elif equation[x] == '(' and x == 0:
            pass

    return equation


def check_for_double_dots(equation: str) -> str:
    """
    function that checks if there are two dots in a row
    :param equation:
    :return: equation if there are no two dots in a row
    and prints an error message otherwise
    """
    # go over equation and check if there are two dots in a row
    for x in range(len(equation) - 1):
        if equation[x] == '.' and equation[x + 1] == '.':
            print('Invalid syntax - two dots in a row')
            exit()
    return equation


def check_for_number_with_too_many_dots_in_them(equation: str) -> str:
    """
    function that checks if there are numbers with too many dots in them
    :param equation:
    :return: equation if there are no numbers with too many dots in them
    and prints an error message otherwise
    """
    # go over equation and check if there are numbers with too many dots in them
    for x in range(len(equation) - 1):
        if is_number(equation[x]) and equation[x + 1] == '.' \
                and is_number(equation[x + 2]) \
                and equation[x + 3] == '.':
            print('Invalid syntax -'
                  ' number with too many dots in it')
            exit()
    return equation


def add_zero_before_and_after_dot_integer(equation: str) -> str:
    """
    function that adds a zero before and after a dot
    F.E 2.(3) is 2.0(3)
    or .8 is 0.8
    or 2. is 2.0
    advanced example: 2.(.3+4.) is 2.0(0.3+4.0)
    :param equation:
    :return: equation with a zero before and after a dot
    """

    # if equation == '.' then add a 0 on both sides of the dot
    if equation == '.':
        equation = '0' + equation + '0'
        return equation

    # go over equation and add a zero before and after a dot
    x = 0
    while x <= len(equation) - 1:
        if equation[x] == '.':

            # if the dot is at the beginning of the equation
            if x == 0:
                equation = '0' + equation

            # if the dot is at the end of the equation
            elif x == len(equation) - 1:
                equation = equation + '0'

            # if the dot is in the middle of the equation
            elif not x == 0 and not x == len(equation) - 1:
                if not is_number(equation[x - 1]):
                    equation = equation[:x] + '0' + equation[x:]
                elif not is_number(equation[x + 1]):
                    equation = equation[:x + 1] + '0' + equation[x + 1:]
        x += 1
    # return the equation with a zero before and after a dot
    return equation


def check_if_function_is_valid(equation: str, operators: tuple, operands: tuple,
                               binary_operators: tuple,
                               unary_operators: tuple,
                               right_unary_operands: tuple,
                               left_unary_operands: tuple) -> str:
    """
    This function checks if the equation is valid,
    the function receives the equation, the tuples of operators and operands,
    and the dictionary of priorities for the operators and checks,
    if the equation is not valid, if the equation is not valid,
    the program prints an error message, if the equation is valid,
    the function returns the equation
    :param left_unary_operands:
    :param right_unary_operands:
    :param equation:
    :param operators:
    :param operands:
    :param binary_operators:
    :param unary_operators:
    :return: equation if it is valid and prints an error message otherwise
    """

    # check if the equation is just a number
    if is_number(equation):
        return equation

    # else: the equation is not a number:
    # continue with the program

    # check if the equation doesn't contain numbers
    equation = function_doesnt_contain_numbers(equation)

    # check if equation only contains operators and operands
    equation = contains_invalid_characters(equation, operators, operands)

    # remove all the spaces from the equation
    equation = get_rid_of_extra_white_spaces(equation)

    # check for parentheses errors
    equation = check_for_extra_parentheses(equation)

    # check if the equation contains two consecutive dots
    equation = check_for_double_dots(equation)

    # add a zero before and after a dot if needed
    equation = add_zero_before_and_after_dot_integer(equation)

    # check if there is a number with too many dots in it
    check_for_number_with_too_many_dots_in_them(equation)

    # check if equation is balanced
    equation = check_balanced_equation(equation)

    # check if there is an invalid character after a closing parentheses
    # or before an opening parentheses
    equation = parentheses_surrounding_validity(equation)

    # remove the extra white spaces from the equation
    equation = get_rid_of_extra_white_spaces(equation)

    # check the validity of the equation by binary operators
    equation = check_validity_of_equation_by_binary_operators(equation,
                                                              binary_operators)

    # check the validity of the equation by unary operators
    equation = check_validity_of_equation_by_unary_operators(equation,
                                                             unary_operators, RIGHT_ASSOCIATIVE_UNARY_OPERATORS,
                                                             LEFT_ASSOCIATIVE_UNARY_OPERATORS)

    # check validity of equation by both binary and unary operators
    equation = check_validity_of_equation_by_all_operators(equation, binary_operators,
                                                           unary_operators, RIGHT_ASSOCIATIVE_UNARY_OPERATORS,
                                                           LEFT_ASSOCIATIVE_UNARY_OPERATORS)

    return equation


test = '2.0-(3.0+4.0)'
print(check_if_function_is_valid(test, OPERATORS, OPERANDS, BINARY_OPERATORS,
                                 UNARY_OPERATORS, RIGHT_ASSOCIATIVE_UNARY_OPERATORS, LEFT_ASSOCIATIVE_UNARY_OPERATORS))


def check_balanced_equation(equation: str) -> str:
    """
    This function checks if the equation is balanced,
    the function receives the equation and checks,
    if the amount of opening parentheses is the
    same as the amount of closing parentheses
    and if all the parentheses are balanced
    meaning all the opening parentheses have a closing parentheses
    and all the closing parentheses have an opening parentheses
    :param equation:
    :return: equation
    """

    # meaning that there are the same
    # number of opening and closing parentheses
    if equation.count('(') != equation.count(')'):
        print('Invalid syntax - number of opening and closing'
              ' parentheses is not the same on token'
              ' {}'.format(equation))
        exit()

    # check if a closing parentheses is before an opening parentheses
    if equation.find(')') < equation.find('('):
        print('Invalid syntax - closing parentheses'
              ' is before an opening'
              ' parentheses on token {}'.format(equation))
        exit()

    # check if every opening parentheses has a closing parentheses
    counter_opening_parentheses = 0
    for x in equation:
        # every time we find an opening parentheses
        # we add 1 to the counter
        # every time we find a closing parentheses
        # we subtract 1 from the counter
        if x == '(':
            counter_opening_parentheses += 1
        elif x == ')':
            counter_opening_parentheses -= 1

        # check if there are too many closing parentheses
        # before an opening parentheses
        if counter_opening_parentheses < 0:
            print('Invalid syntax - closing parentheses is'
                  ' before an opening'
                  ' parentheses on token {}'.format(equation))
            exit()

    # at the end of the loop, if the counter is not zero,
    # it means that there is an opening parentheses
    # without a closing parentheses
    if counter_opening_parentheses != 0:
        print('Invalid syntax - number of opening and closing'
              ' parentheses is not the'
              ' same on token {}'.format(equation))
        exit()

    # if we got here, the equation is balanced
    return equation


def contains_invalid_characters(equation: str, operators: tuple, operands: tuple) -> str:
    """
    This function checks if the equation contains invalid characters
    :param equation:
    :param operators:
    :param operands:
    :return: True if the equation contains invalid characters, False otherwise
    """
    for x in equation:
        if x not in operators and x not in operands:
            print("Invalid syntax - The equation contains invalid characters")
            exit()
    return equation


def check_validity_of_equation_by_binary_operators(equation: str,
                                                   binary_operators: tuple) -> str:
    """
    returns the function if all the binary operands
    are valid in it, if not prints error message
    :param equation:
    :param binary_operators:
    :return: equation
    """

    # NOTE: the function is not implemented yet
    # and everything that is written here is just a draft

    # check if there is a binary operator at the beginning of the equation
    if equation[0] in binary_operators:
        # if the equation starts with a binary operator
        # then the equation is not valid
        # the exception is if the equation starts with a minus sign
        if equation[0] != '-':
            print('Invalid syntax - binary operator at the beginning'
                  ' of the equation')
            exit()

    # check if there is a binary operator at the end of the equation
    if equation[-1] in binary_operators:
        print('Invalid syntax - binary operator at the end'
              ' of the equation')
        exit()

    # it is important to note that this function is run
    # after the function that checks for extra minus signs
    # so there is no need to check for extra minus signs here

    # check if there is a binary operator after a binary operator
    # where the only exception is the minus operator
    # because the minus operator appear after a binary operator
    # when it is a negative number
    for x in range(len(equation) - 1):
        if equation[x] in binary_operators:

            # checks for before the operator

            # check if the operator is after another operator
            if equation[x - 1] in binary_operators:
                # check if the operator is not a minus operator
                if equation[x] != '-':
                    print('Invalid syntax - binary operator after'
                          ' another binary operator')
                    exit()
            # check if the operator is after an opening parentheses
            if equation[x - 1] == '(':
                # check if the operator is not a minus operator
                if equation[x] != '-':
                    print('Invalid syntax - binary operator after'
                          ' an opening parentheses')
                    exit()

            # checks for after the operator

            # check if the operator is a minus operator
            if equation[x] == '-':
                # check if the minus is before an operator
                if equation[x + 1] in binary_operators:
                    print('Invalid syntax - binary operator after a'
                          ' binary operator')
                    exit()
                # check if the minus is before a closing parentheses
                elif equation[x + 1] == ')':
                    print('Invalid syntax - closing parentheses after'
                          ' a binary operator')
                    exit()
            # if the operator is not a minus operator
            else:
                # check if the operator is before an operator
                if equation[x + 1] in binary_operators:
                    # if the operator is not be
                    if equation[x + 1] != '-':
                        print('Invalid syntax - binary operator after a'
                              ' binary operator')
                        exit()
                # check if the minus is before a closing parentheses
                elif equation[x + 1] == ')':
                    print('Invalid syntax - closing parentheses after'
                          ' a binary operator')
                    exit()

    # return the equation if it is valid
    return equation


def check_validity_of_equation_by_unary_operators(equation: str,
                                                  unary_operators: tuple,
                                                  right_unary_operators: tuple,
                                                  left_unary_operators: tuple) -> str:
    """
    returns the function if all the unary operands
    are valid in it, if not prints error message
    :param left_unary_operators:
    :param right_unary_operators:
    :param unary_operators:
    :param equation:
    :return: equation
    """

    # check if the function starts with a right unary operator
    if equation[0] in right_unary_operators:
        print('Invalid syntax - equation starts with a right unary operator')
        exit()

    # check if the function ends with a left unary operator
    if equation[-1] in left_unary_operators:
        print('Invalid syntax - equation ends with a left unary operator')
        exit()
    # check the validity of unary operators in the equation

    for x in range(len(equation) - 1):
        # check if there are two unary operators in a row
        if equation[x] in unary_operators and \
                equation[x + 1] in unary_operators:
            print('Invalid syntax - two unary operators in a row ')
            exit()

        # check if there is a right unary operator is
        # after something that is not a number or a closing parentheses
        if equation[x] in right_unary_operators:
            if not is_number(equation[x - 1]) and equation[x - 1] != ')':
                print('Invalid syntax - right unary operator after something'
                      ' that is not a number or a closing parentheses')
                exit()
            # check if the next character is a number or an opening parentheses
            # this check prevents the user from writing something like 5!5
            if x != len(equation) - 1:
                # if the right unary operator is not the last character
                # in the equation, check if the next character is a number
                # or an opening parentheses
                if is_number(equation[x + 1]) or equation[x + 1] == '(':
                    print('Invalid syntax - right unary followed by'
                          ' a number or an opening parentheses')
                    exit()

        # check if there is a left unary operator that is
        # in front of something that is not a number or an opening parentheses
        if equation[x] in left_unary_operators:
            if not is_number(equation[x + 1]) and equation[x + 1] != '(':
                print('Invalid syntax - left unary operator in front of'
                      ' something that is not a number or an opening parentheses')
                exit()
            # check if the last character is a number or a closing parentheses
            # this check prevents the user from writing something like 5~5
            if x != 0:
                # if the left unary operator is not the first character
                # in the equation, check if the character before it is a number
                # or a closing parentheses
                if is_number(equation[x - 1]) or equation[x - 1] == ')':
                    print('Invalid syntax - left unary operator following'
                          ' a number or a closing parentheses')
                    exit()

    return equation


def check_validity_of_equation_by_all_operators(equation: str, binary_operators: tuple,
                                                unary_operators: tuple,
                                                right_unary_operators: tuple,
                                                left_unary_operators: tuple) -> str:
    """
    returns the function if all the binary and unary operands
    are valid in it, if not prints error message
    :param left_unary_operators:
    :param right_unary_operators:
    :param equation:
    :param binary_operators:
    :param unary_operators:
    :return: equation
    """

    # go over the function and check if there is a binary operator
    # and if there is a unary operator next to each other
    # in a way that is not valid
    # for example: 5*!5 or 5~*5
    # if there is such a case print an error message and exit
    for x in range(len(equation) - 1):
        if equation[x] in binary_operators:
            if equation[x + 1] in right_unary_operators:
                # check if there is a right unary operator after a binary operator
                print('Invalid syntax - binary operator before a right'
                      ' unary operator')
                exit()
            elif equation[x - 1] in left_unary_operators:
                # check if there is a left unary operator before a binary operator
                print('Invalid syntax - binary operator after a left'
                      ' unary operator')
                exit()

    return equation


def check_for_extra_parentheses(equation: str) -> str:
    """
    function that checks if there are extra parentheses
    in the equation that don't do anything
    and if there are, prints error message
    and ends the program
    :param equation:
    :return: same equation if there are no extra parentheses
    """

    # check if there are extra parentheses
    if '()' in equation:
        print("Invalid syntax, extra parentheses in the equation")
        exit()

    # if there are no extra parentheses, return the equation
    return equation


def get_rid_of_extra_minus_signs(equation: str, operands: tuple,
                                 binary_operators: tuple,
                                 unary_operators: tuple) -> str:
    """
    function that gets rid of extra minus signs
    F.E 2---3 is just 2-3
    or 2--3 is just 2-3
    or 2----3 is 2+3
    :param unary_operators:
    :param operands:
    :param binary_operators:
    :param equation:
    :return: equation with no extra minus signs
    """

    # if the equation is not None, continue with the program

    # replace all triple minus signs with -
    equation = equation.replace('---', '-')

    # at this point, the equation can only contain
    # two consecutive minus signs or none

    # remove all extra minus signs at the
    # beginning of the equation
    while equation[0] == '-':
        # if the equation is just a minus sign
        # then return the equation
        if len(equation) == 1:
            return equation
        elif equation[1] == '-':
            equation = equation[2:]

    # if there are minus signs at the end of the equation
    # then return error message because it is invalid syntax
    if equation[-1] == '-':
        print("Invalid syntax, extra minus sign at the end of the equation")
        exit()

    # now that there are no extra minus signs at the beginning
    # of the equation, check if there are extra minus signs
    # in the middle of the equation

    # go over equation and get rid of extra minus signs
    # this is done by replacing -- with +
    for x in range(len(equation) - 1):
        # if there are two minus signs in a row
        if equation[x] == '-' and equation[x + 1] == '-':
            # if the double minus sign is before a number
            if is_number(equation[x + 2]):
                # replace the double minus sign with +
                equation = equation[:x] + '+' + equation[x + 2:]
                break
            # if the double minus sign is before a parentheses
            elif equation[x + 2] == '(':
                # replace the double minus sign with +
                equation = equation[:x] + '+' + equation[x + 2:]
                break
            # if the double minus sign is before a closing parentheses
            elif equation[x + 2] == ')':
                # print error message and exit
                print("Invalid syntax, extra minus sign before a closing "
                      "parentheses")
                exit()
            # if the double minus sign is before a unary operator
            elif equation[x + 2] in unary_operators:
                # print error message and exit
                print("Invalid syntax, extra minus sign before a unary "
                      "operator")
                exit()
            # if the double minus sign is before a binary operator
            elif equation[x + 2] in binary_operators:
                # print error message and exit
                print("Invalid syntax, extra minus sign before a binary "
                      "operator")
                exit()

    # if there are no extra minus signs, return the equation
    # we need this check because we break out of the for loop
    # when we replace a double minus, but we do that because
    # if we don't the equation will be changed and the for loop
    # will not work properly
    if '--' not in equation:
        return equation
    else:
        # if there are still extra minus signs, call the function again
        return get_rid_of_extra_minus_signs(equation, operands,
                                            binary_operators,
                                            unary_operators)


def get_rid_of_extra_white_spaces(equation: str) -> str:
    """
    function that gets rid of extra white spaces
    and also checks if there are illegal white spaces
    between two operands
    :param equation:
    :return: equation with no extra white spaces
    """

    # remove tabs from the equation
    # go over equation and get rid of extra white spaces
    # if the equation starts with white spaces, remove them
    if ' ' in equation or '\t' in equation:
        if equation[0] == ' ':
            counter = 0
            while equation[counter] == ' ' or equation[counter] == '\t':
                # while there are white spaces
                counter += 1
            equation = equation[counter:]  # remove the white spaces

        # if the equation ends with white spaces, remove them
        if equation[-1] == ' ':
            counter = -1
            while equation[counter] == ' ' or equation[counter] == '\t':
                counter -= 1
            equation = equation[:counter + 1]

    # if there are no white spaces in the equation,
    else:
        return equation

    # convert all double spaces to single spaces
    while '  ' in equation or '\t\t' in equation:
        equation = equation.replace('  ', ' ')
        equation = equation.replace('\t', ' ')

    # if there are white spaces in the equation, check if they
    # are legal white spaces
    # if there are illegal white spaces, print error message
    # if there are legal white spaces, remove them

    # go over equation and check if there are illegal white spaces
    # between two operands
    for x in range(len(equation) - 1):
        if equation[x] == ' ':

            # check if there is a white space between two digits
            if is_number(equation[x - 1]) and is_number(equation[x + 1]):
                print("Invalid syntax, illegal white space between two "
                      "digits")
                exit()

    # when there are no illegal white spaces, return the equation
    # with no extra white spaces
    equation = equation.replace(' ', '')

    return equation


def find_closing_parentheses(equation: str, index: int) -> int:
    """
    this function gets an equation, and a starting index
    of the opening parentheses and returns the index of the
    closing parentheses
    :param equation: the equation
    :param index: the index of the opening parentheses
    :return: the index of the closing parentheses
    """
    # check if the character at the index is an opening parentheses
    if equation[index] != '(':
        print('Invalid syntax - the character at the index'
              ' is not an opening parentheses')
        exit()

    # check if the index is in the equation
    if index >= len(equation):
        print('Invalid syntax - the index is out of range')
        exit()

    # check if the index is not negative
    if index < 0:
        print('Invalid syntax - the index is negative')
        exit()

    # counter for the number of opening parentheses
    counter_opening_parentheses = 0

    # go over the equation from the index
    for x in range(index, len(equation)):

        # if the current character is an opening parentheses
        if equation[x] == '(':
            # increase the counter
            counter_opening_parentheses += 1

        # if the current character is a closing parentheses
        if equation[x] == ')':
            # decrease the counter
            counter_opening_parentheses -= 1

        # if the counter is 0
        if counter_opening_parentheses == 0:
            # return the index of the closing parentheses
            return x

        # if the counter is not 0
        # it means that there is no closing parentheses
        # for the opening parentheses at the index
        if counter_opening_parentheses < 0:
            print('Invalid syntax - no closing parentheses'
                  ' for the opening parentheses at the index')
            exit()

    # if we reach end and counter is not 0, print error message
    # technically this should never happen because the function
    # is run after the equation is checked for parentheses errors
    # but just in case we will print an error message
    if counter_opening_parentheses != 0:
        print('Invalid syntax - no closing parentheses'
              ' for the opening parentheses at the index')
        exit()


# TODO: implement this function
# note: important - make sure that the function always calculates
# the sub equation in parentheses first, and replace it with the
# result, to avoid problems with the operands that try to calculate
# something like (2+2)*2, make sure to first calculate (2+2) and
# replace it with 4, and then calculate 4*2
def calculate_equation(equation: str, binary_operators: tuple,
                       unary_operators: tuple, priority: dict,
                       operands: tuple, operators: tuple,
                       right_unary_operands: tuple,
                       left_unary_operands: tuple) -> str:
    """
    general function that calculates the equation, this function
    will be run recursively until the equation is solved
    :param left_unary_operands:
    :param operators:
    :param operands:
    :param right_unary_operands:
    :param equation:
    :param binary_operators:
    :param unary_operators:
    :param priority:
    :return: the result of the equation
    """
    # do the math functions based on the priority,
    # the highest priority first
    # for x in range(priority, -1, -1):
    #     # go over equation and do the math functions
    #     for y in range(len(equation)):
    #         # if the equation is a number, return it
    #         if is_number(equation):
    #             return equation
    #
    #         # if the equation is a binary operator
    #         if equation[y] in binary_operators[x]:
    #             # get the left and right side of the operator
    #             left_side = equation[:y]
    #             right_side = equation[y + 1:]
    #
    #             # get the left and right side of the operator
    #             # by getting the last number on the left side and first
    #             # number on the right side
    #             # this is done by going over the left and right side of
    #             # the operator and getting the last and first number
    #             left_side_number = ''
    #             right_side_number = ''
    #             for z in range(len(left_side) - 1, -1, -1):
    #                 if is_number(left_side[z]):
    #                     left_side_number = left_side[z] + left_side_number
    #                 else:
    #                     break
    #             for z in range(len(right_side)):
    #                 if is_number(right_side[z]):
    #                     right_side_number += right_side[z]
    #                 else:
    #                     break
    #
    #             # calculate the equation
    #             # by replacing the left and right side
    #             # of the operator with the result
    #             equation = equation.replace(left_side_number + equation[y]
    #                                         + right_side_number,
    #                                         str(binary_operators[x][equation[y]]
    #                                         (left_side_number,right_side_number)))
    #
    #             # break out of the for loop
    #             break
    #
    #         # if the equation is a unary operator
    #         elif equation[y] in unary_operators[x]:
    #             # get the left and right side of the operator
    #             left_side = equation[:y]
    #             right_side = equation[y + 1:]
    #
    #             # get the left and right side of the operator
    #             # by getting the last number on the left
    #             # side and first number on the right side
    #             # this is done by going over the left and
    #             # right side of the operator
    #             # and getting the last and first number
    #             left_side_number = ''
    #             right_side_number = ''
    #             for z in range(len(left_side) - 1, -1, -1):
    #                 if is_number(left_side[z]):
    #                     left_side_number = left_side[z] + left_side_number
    #                 else:
    #                     break

    # TODO: implement the current parentheses handling somewhere here
    # if we have parentheses in the equation, we find the matching closing parentheses,
    # and we calculate the equation inside the parentheses, then we replace the parentheses
    # with the result of the equation inside the parentheses, the calculation is done
    # recursively until there are no parentheses left using the calculate_equation function
    # if equation[y] == '(':
    #     # get the index of the closing parentheses
    #     closing_parentheses_index = find_closing_parentheses(equation, y)
    #     # get the equation inside the parentheses
    #     equation_inside_parentheses = equation[y + 1:closing_parentheses_index]
    #
    #     # save the equation before calculating the equation inside the parentheses
    #     saved_equation_inside_parentheses = equation_inside_parentheses
    #
    #     # calculate the equation inside the parentheses
    #     equation_inside_parentheses = calculate_equation(equation_inside_parentheses,
    #                                                      binary_operators,
    #                                                      unary_operators,
    #                                                      priority)
    #     # replace the equation inside the parentheses with the result
    #     equation = equation.replace('(' + saved_equation_inside_parentheses + ')',
    #                                 equation_inside_parentheses)

    # final check to see if the equation is a number
    # if it is a number, return it
    if is_number(equation):
        return equation
    else:
        print('Invalid equation - the equation doesnt have a result')
        exit()
