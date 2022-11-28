# This is a file that contains general functions for the equation
# Path: functions.py
# Author: @Eldar Aslanbeily

from globals import *


def is_number(s="") -> bool:
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


def doesnt_contain_numbers(equation="") -> bool:
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


def function_doesnt_contain_numbers(equation="") -> str:
    """
    function that checks if a function doesn't contain numbers
    simply by running the function doesnt_contain_numbers
    :param equation:
    :return: equation if the function doesn't contain numbers
    """
    # check if the equation doesn't contain numbers
    if doesnt_contain_numbers(equation):
        print('Invalid syntax - equation does not contain numbers')
        exit(1)

    # if the equation contains numbers, then return the equation
    return equation


def parentheses_surrounding_validity(equation="",
                                     right_unary_operators=RIGHT_ASSOCIATIVE_UNARY_OPERATORS,
                                     left_unary_operators=LEFT_ASSOCIATIVE_UNARY_OPERATORS) -> str:
    """
    function that checks if the surrounding of parentheses
    are valid, meaning that there are no numbers or closing parentheses
    before an opening parentheses and there are no opening parentheses
    or numbers after a closing parentheses, in a regular equation
    5(3+4) is valid and would be 5*(3+4), but in this calculator
    5(3+4) is invalid and would print an error message
    For example: 2(3) is not valid
    or 2(3+4)5 is not valid but 2*(3+4)-5 is valid
    :param right_unary_operators:
    :param left_unary_operators:
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
            if is_number(equation[x + 1]) or equation[x + 1] == '(' \
                    or equation[x + 1] in left_unary_operators:
                print("Invalid syntax - number or opening parentheses "
                      "or left unary operator after closing parentheses")
                exit(1)
        # if there is closing parentheses at the end of the equation
        # then we don't need to check if there is invalid character
        # after the closing parentheses
        elif equation[x] == ')' and x == len(equation) - 1:
            pass
        elif equation[x] == '(' and x != 0:
            if is_number(equation[x - 1]) or equation[x - 1] == ')' \
                    or equation[x - 1] in right_unary_operators:
                print("Invalid syntax - number or closing parentheses "
                      "or right unary operator before opening parentheses")
                exit(1)
        # if there is closing parentheses at the end of the equation
        # then we don't need to check if there is invalid character
        # after the closing parentheses
        elif equation[x] == '(' and x == 0:
            pass

    return equation


def check_for_double_dots(equation="") -> str:
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
            exit(1)
    return equation


def check_for_number_with_too_many_dots_in_them(equation="") -> str:
    """
    function that checks if there are numbers with too many dots in them
    :param equation:
    :return: equation if there are no numbers with too many dots in them
    and prints an error message otherwise
    """
    # go over equation and check if there are numbers with too many dots in them
    # set a flag to check if we already have a dot in the current number
    flag = False

    # go over the equation and every time we see a dot, we set the flag to true
    # and if we see another dot, we print an error message if the flag is true
    # the flag is set to false after we exit the current number
    # meaning that the character is not a digit
    for x in equation:
        if x == '.':
            if flag:
                print('Invalid syntax - number with too'
                      ' many decimal points in it')
                exit(1)
            else:
                flag = True
        elif not is_number(x):
            flag = False
    return equation


def add_zero_before_and_after_dot_integer(equation="") -> str:
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


def check_balanced_equation(equation="") -> str:
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
        exit(1)

    # check if a closing parentheses is before an opening parentheses
    if equation.find(')') < equation.find('('):
        print('Invalid syntax - closing parentheses'
              ' is before an opening'
              f' parentheses on token {equation}')
        exit(1)

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
                  f' parentheses on token {equation}')
            exit(1)

    # at the end of the loop, if the counter is not zero,
    # it means that there is an opening parentheses
    # without a closing parentheses
    if counter_opening_parentheses != 0:
        print('Invalid syntax - number of opening and closing'
              ' parentheses is not the'
              f' same on token {equation}')
        exit(1)

    # if we got here, the equation is balanced
    return equation


def contains_invalid_characters(equation="", operators=OPERATORS,
                                operands=OPERANDS) -> str:
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
            exit(1)
    return equation


def check_validity_of_equation_by_binary_operators(equation="",
                                                   binary_operators=BINARY_OPERATORS) -> str:
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
            exit(1)

    # check if there is a binary operator at the end of the equation
    if equation[-1] in binary_operators:
        print('Invalid syntax - binary operator at the end'
              ' of the equation')
        exit(1)

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
                    exit(1)
            # check if the operator is after an opening parentheses
            if equation[x - 1] == '(':
                # check if the operator is not a minus operator
                if equation[x] != '-':
                    print('Invalid syntax - binary operator after'
                          ' an opening parentheses')
                    exit(1)

            # checks for after the operator

            # check if the operator is a minus operator
            if equation[x] == '-':
                # check if the minus is before an operator
                if equation[x + 1] in binary_operators:
                    print('Invalid syntax - binary operator after a'
                          ' binary operator')
                    exit(1)
                # check if the minus is before a closing parentheses
                elif equation[x + 1] == ')':
                    print('Invalid syntax - closing parentheses after'
                          ' a binary operator')
                    exit(1)
            # if the operator is not a minus operator
            else:
                # check if the operator is before an operator
                if equation[x + 1] in binary_operators:
                    # if the operator is not be
                    if equation[x + 1] != '-':
                        print('Invalid syntax - binary operator after a'
                              ' binary operator')
                        exit(1)
                # check if the minus is before a closing parentheses
                elif equation[x + 1] == ')':
                    print('Invalid syntax - closing parentheses after'
                          ' a binary operator')
                    exit(1)

    # return the equation if it is valid
    return equation


def check_validity_of_equation_by_unary_operators(equation="",
                                                  unary_operators=UNARY_OPERATORS,
                                                  right_unary_operators=RIGHT_ASSOCIATIVE_UNARY_OPERATORS,
                                                  left_unary_operators=LEFT_ASSOCIATIVE_UNARY_OPERATORS) -> str:
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
        exit(1)

    # check if the function ends with a left unary operator
    if equation[-1] in left_unary_operators:
        print('Invalid syntax - equation ends with a left unary operator')
        exit(1)
    # check the validity of unary operators in the equation

    for x in range(len(equation) - 1):
        # check if there are two unary operators in a row
        if equation[x] in unary_operators and \
                equation[x + 1] in unary_operators:
            print('Invalid syntax - two unary operators in a row ')
            exit(1)

        # check if there is a right unary operator is
        # after something that is not a number or a closing parentheses
        if equation[x] in right_unary_operators:
            if not is_number(equation[x - 1]) and equation[x - 1] != ')':
                print('Invalid syntax - right unary operator after something'
                      ' that is not a number or a closing parentheses')
                exit(1)
            # check if the next character is a number or an opening parentheses
            # this check prevents the user from writing something like 5!5
            if x != len(equation) - 1:
                # if the right unary operator is not the last character
                # in the equation, check if the next character is a number
                # or an opening parentheses
                if is_number(equation[x + 1]) or equation[x + 1] == '(':
                    print('Invalid syntax - right unary followed by'
                          ' a number or an opening parentheses')
                    exit(1)

        # check if there is a left unary operator that is
        # in front of something that is not a number or an opening parentheses
        if equation[x] in left_unary_operators:
            if not is_number(equation[x + 1]) and equation[x + 1] != '(' \
                    and equation[x + 1] != '-':
                print('Invalid syntax - left unary operator in front of'
                      ' something that is not a number or an opening parentheses')
                exit(1)
            # check if the last character is a number or a closing parentheses
            # this check prevents the user from writing something like 5~5
            if x != 0:
                # if the left unary operator is not the first character
                # in the equation, check if the character before it is a number
                # or a closing parentheses
                if is_number(equation[x - 1]) or equation[x - 1] == ')':
                    print('Invalid syntax - left unary operator following'
                          ' a number or a closing parentheses')
                    exit(1)

    return equation


def check_validity_of_equation_by_all_operators(equation="", binary_operators=BINARY_OPERATORS,
                                                right_unary_operators=RIGHT_ASSOCIATIVE_UNARY_OPERATORS,
                                                left_unary_operators=LEFT_ASSOCIATIVE_UNARY_OPERATORS) -> str:
    """
    returns the function if all the binary and unary operands
    are valid in it, if not prints error message
    :param left_unary_operators:
    :param right_unary_operators:
    :param equation:
    :param binary_operators:
    :return: equation
    """

    # go over the function and check if there is a binary operator
    # and if there is a unary operator next to each other
    # in a way that is not valid
    # for example: 5*!5 or 5~*5
    # if there is such a case print an error message and exit
    for x in range(len(equation) - 1):
        if equation[x] in binary_operators and \
                equation[x] != '-':
            if equation[x + 1] in right_unary_operators:
                # check if there is a right unary operator after a binary operator
                print('Invalid syntax - binary operator before a right'
                      ' unary operator')
                exit(1)
            elif equation[x - 1] in left_unary_operators:
                # check if there is a left unary operator before a binary operator
                print('Invalid syntax - binary operator after a left'
                      ' unary operator')
                exit(1)

    return equation


def check_for_extra_parentheses(equation="") -> str:
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
        exit(1)

    # if there are no extra parentheses, return the equation
    return equation


def get_rid_of_extra_minus_signs(equation="", operands=OPERANDS,
                                 binary_operators=BINARY_OPERATORS,
                                 unary_operators=UNARY_OPERATORS,
                                 right_unary_operators=RIGHT_ASSOCIATIVE_UNARY_OPERATORS,
                                 left_unary_operators=LEFT_ASSOCIATIVE_UNARY_OPERATORS) -> str:
    """
    function that gets rid of extra minus signs
    F.E 2---3 is just 2-3
    or 2--3 is just 2-3
    or 2----3 is 2+3
    :param right_unary_operators:
    :param left_unary_operators:
    :param unary_operators:
    :param operands:
    :param binary_operators:
    :param equation:
    :return: equation with no extra minus signs
    """

    # if the equation is not None, continue with the program

    # replace all triple minus signs with -
    while '---' in equation:
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
            continue
        # go over the equation and check if there is a minus sign
        # until the first left unary operator, number or opening parentheses
        elif is_number(equation[1]) or equation[1] == '(' \
                or equation[1] in left_unary_operators:
            break

    # if there are minus signs at the end of the equation
    # then return error message because it is invalid syntax
    if equation[-1] == '-':
        print("Invalid syntax, extra minus sign at the end of the equation")
        exit(1)

    # now that there are no extra minus signs at the beginning
    # of the equation, check if there are extra minus signs
    # in the middle of the equation

    # go over equation and get rid of extra minus signs
    # this is done by replacing -- with +
    for x in range(len(equation) - 1):
        # if there are two minus signs in a row
        if equation[x] == '-' and equation[x + 1] == '-':
            # if the double minus sign is before a number
            # or an opening parentheses or a left unary operator
            if is_number(equation[x + 2]) or equation[x + 2] == '(' or \
                    equation[x + 2] in left_unary_operators:
                # if the double minus sign is after a binary operator
                if equation[x - 1] in binary_operators or equation[x - 1] \
                        in left_unary_operators or equation[x-1] == '(':
                    # remove the double minus sign
                    equation = equation[:x] + equation[x + 2:]
                    break
                # if the double minus sign is after an operand
                # or a closing parentheses or a right unary operator
                elif equation[x - 1] in operands or equation[x - 1] == ')' \
                        or equation[x - 1] in right_unary_operators:
                    # then replace the double minus sign with a plus sign
                    equation = equation[:x] + '+' + equation[x + 2:]
                    break
            # if the double minus sign is before a closing parentheses
            elif equation[x + 2] == ')':
                # print error message and exit
                print("Invalid syntax, extra minus sign before a closing "
                      "parentheses")
                exit(1)
            # if the double minus sign is before a unary operator
            elif equation[x + 2] in right_unary_operators:
                # print error message and exit
                print("Invalid syntax, extra minus sign before a right "
                      "unary operator")
                exit(1)
            # if the double minus sign is before a binary operator
            elif equation[x + 2] in binary_operators:
                # print error message and exit
                print("Invalid syntax, extra minus sign before a binary "
                      "operator")
                exit(1)

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
                                            unary_operators,
                                            right_unary_operators, left_unary_operators)


def get_rid_of_extra_white_spaces(equation="") -> str:
    """
    function that gets rid of extra white spaces
    and also checks if there are illegal white spaces
    between two operands
    :param equation:
    :return: equation with no extra white spaces
    """

    # convert all double spaces and tabs
    # and next lines to single spaces
    while '  ' in equation or '\t' in equation or '\n' in equation:
        equation = equation.replace('  ', ' ')
        equation = equation.replace('\t', ' ')
        equation = equation.replace('\n', ' ')

    # remove all leading and trailing white spaces
    if ' ' in equation:
        if equation[0] == ' ':
            equation = equation[1:]

        # if the equation ends with white spaces, remove them
        elif equation[-1] == ' ':
            equation = equation[:-1]

    # if there are no white spaces in the equation,
    else:
        return equation

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
                exit(1)

    # when there are no illegal white spaces, return the equation
    # with no extra white spaces
    equation = equation.replace(' ', '')

    return equation


def find_closing_parentheses(equation="", index=0) -> int:
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
        exit(1)

    # check if the index is in the equation
    if index >= len(equation):
        print('Invalid syntax - the index is out of range')
        exit(1)

    # check if the index is not negative
    if index < 0:
        print('Invalid syntax - the index is negative')
        exit(1)

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

    # if we reach end and counter is not 0, print error message
    # technically this should never happen because the function
    # is run after the equation is checked for parentheses errors
    # but just in case we will print an error message
    if counter_opening_parentheses != 0:
        print('Invalid syntax - no closing parentheses'
              ' for the opening parentheses at the index')
        exit(1)


def check_if_function_is_valid(equation="") -> str:
    """
    This function checks if the equation is valid,
    the function receives the equation, the tuples of operators and operands,
    and the dictionary of priorities for the operators and checks,
    if the equation is not valid, if the equation is not valid,
    the program prints an error message, if the equation is valid,
    the function returns the equation
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
    equation = contains_invalid_characters(equation)

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

    # remove the extra minus signs from the equation
    equation = get_rid_of_extra_minus_signs(equation)

    # check the validity of the equation by binary operators
    equation = check_validity_of_equation_by_binary_operators(equation)

    # check the validity of the equation by unary operators
    equation = check_validity_of_equation_by_unary_operators(equation)

    # check validity of equation by both binary and unary operators
    equation = check_validity_of_equation_by_all_operators(equation)

    return equation


def get_number_to_the_right_of_the_operator(equation="", index=0) -> str:
    """
    this function gets an equation and an index of an operator,
    and returns the number to the right of the operator
    :param equation: the equation
    :param index: the index of the operator
    :return: the number to the right of the operator
    """

    # check if the index is in the equation
    if index >= len(equation):
        print('Invalid syntax - the index is out of range')
        exit(1)

    # check if the index is not negative
    if index < 0:
        print('Invalid syntax - the index is negative')
        exit(1)

    # if the index is at the end of the equation
    if index == len(equation) - 1:
        print('Invalid syntax - the operator is at the end of the equation')
        exit(1)

    # if the index is at the second to last character of the equation
    if index == len(equation) - 2:
        # return the last character of the equation
        return equation[index + 1]

    # initialize the number to the right of the operator
    num_to_return = ''

    # initialize the max sum of minus signs acceptable
    # if we don't set this, the function will return
    # a number with an infinite number of minus signs
    # for example: 5*-3-3, the function will return
    # -3-3 instead of -3, because it will keep adding
    # minus signs to the number
    # so the max sum of minus signs acceptable is 1
    max_num_of_minus_signs = 1

    # current number of minus signs in the number
    current_num_of_minus_signs = 0

    # go over the equation from the index
    for x in range(index + 1, len(equation)):
        # if the current character is an operand
        if equation[x] in OPERANDS:
            # add the current character to the number
            num_to_return += equation[x]
        # if the current character is a minus sign
        elif equation[x] == '-':
            # if the current number of minus signs is less than
            # the max number of minus signs acceptable
            # add the minus sign to the number
            # also check if we haven't added any numbers to the number
            # we return yet because if we did, we can't add a minus sign
            # to the number
            if current_num_of_minus_signs < max_num_of_minus_signs \
                    and num_to_return == '':
                num_to_return += equation[x]
                current_num_of_minus_signs += 1
            # if the current number of minus signs is equal to
            # the max number of minus signs acceptable
            # return the number we added so far
            else:
                break
        # if the current character is not an operand
        else:
            # return the number
            return num_to_return

    # return the number we added so far
    return num_to_return


def get_number_to_the_left_of_the_operator(equation="", index=0) -> str:
    """
    this function gets an equation and an index of an operator,
    and returns the number to the left of the operator
    :param equation: the equation
    :param index: the index of the operator
    :return: the number to the left of the operator
    """

    # check if the index is in the equation
    if index >= len(equation):
        print('Invalid syntax - the index is out of range')
        exit(1)

    # check if the index is not negative
    if index < 0:
        print('Invalid syntax - the index is negative')
        exit(1)

    # if the index is at the start of the equation,
    # but the operator is not a minus sign (that will stand
    # for a negative number)
    if index == 0:
        if equation[index] != '-':
            print('Invalid syntax - the operator is at the start of the equation')
            exit(1)
        elif equation[index] == '-':
            # returning 0 minus something is the same as returning
            # the negative of the number
            return '0'

    # if the index is at the second character of the equation
    if index == 1:
        # return the first character of the equation
        return equation[0]

    # initialize the number to the left of the operator
    num_to_return = ''

    # go over the equation from the index backwards
    for x in range(index - 1, -1, -1):
        # if the current character is an operand
        if equation[x] in OPERANDS:
            # add the current character to the number
            num_to_return = equation[x] + num_to_return
        # if the current character is a minus sign
        elif equation[x] == '-':
            return '-' + num_to_return
        # if the current character is not an operand
        else:
            # return the number
            return num_to_return

    # return the number we added so far
    return num_to_return


def is_negative_number(equation="") -> bool:
    """
    this function gets an equation and returns whether
    the equation contains only a minus sign and numbers
    after the minus sign to indicate a negative number
    :param equation: the equation
    :return: whether the equation contains only a minus sign
     and valid operands
    """
    # go over the equation
    return equation[0] == '-' and is_number(equation[1:]) \
           and equation[1:].count('-') == 0


def count_amount_operators_in_equation(equation="", binary_operators=BINARY_OPERATORS,
                                       unary_operators=UNARY_OPERATORS) -> int:
    """
    this function gets an equation and returns the amount of
    operators in the equation
    :param equation: the equation
    :param binary_operators: the binary operators
    :param unary_operators: the unary operators
    :return: the amount of operators in the equation
    """

    # initialize the amount of operators in the equation
    amount_operators = 0

    # go over the equation
    for x in equation:
        # if the current character is an operator
        if x in binary_operators or x in unary_operators:
            # add 1 to the amount of operators
            amount_operators += 1

    # return the amount of operators
    return amount_operators


def calculate_binary_operator(operator="", left_operand="",
                              right_operand="") -> str:
    """
    this function gets an operator and two operands and returns
    the result of the calculation
    :param operator: the operator
    :param left_operand: the left operand
    :param right_operand: the right operand
    :return: the result of the calculation
    """
    return FUNCTIONS_PER_OPERATOR[operator](left_operand, right_operand)


def calculate_unary_operator(operator="", operand="") -> str:
    """
    this function gets an operator and an operand and returns
    the result of the calculation
    :param operator: the operator
    :param operand: the operand
    :return: the result of the calculation
    """
    return FUNCTIONS_PER_OPERATOR[operator](operand)


def calculate_equation(equation="", binary_operators=BINARY_OPERATORS,
                       unary_operators=UNARY_OPERATORS, priority=PRIORITY,
                       right_unary_operands=RIGHT_ASSOCIATIVE_UNARY_OPERATORS,
                       left_unary_operands=LEFT_ASSOCIATIVE_UNARY_OPERATORS) -> str:
    """
    general function that calculates the equation, this function
    will be run recursively until the equation is solved
    :param left_unary_operands:
    :param right_unary_operands:
    :param equation:
    :param binary_operators:
    :param unary_operators:
    :param priority:
    :return: the result of the equation
    """
    # go over the equation and do the math for each operator
    # by the priority that each operator has
    # the operators with the highest priority will be calculated first
    # and the operators with the lowest priority will be calculated last
    # for example: 2+2*2, the function will first calculate 2*2
    # and then calculate 2+4
    # if there are operators with the same priority, the function will
    # calculate the operators from left to right
    # for example: 2+2*2-2, the function will first calculate 2*2
    # and then calculate 2+4 and then calculate 6-2

    # important - first of all, the function will calculate the
    # sub equation in parentheses, and replace it with the result
    # to avoid problems with the operands that try to calculate
    # something like (2+2)*2, make sure to first calculate (2+2) and
    # replace it with 4, and then calculate 4*2, the calculation of
    # the sub equation in parentheses will be done in the
    # calculate_sub_equation_in_parentheses function called recursively

    # while there are still parentheses in the equation
    # calculate the sub equation in parentheses
    # and replace it with the result
    while '(' in equation:
        for x in range(len(equation)):
            if equation[x] == '(':
                closing_parentheses_index = find_closing_parentheses(equation, x)
                # get the equation inside the parentheses
                equation_inside_parentheses = equation[x + 1:closing_parentheses_index]

                # save the equation before calculating the equation inside the parentheses
                saved_equation_inside_parentheses = equation_inside_parentheses

                # calculate the equation inside the parentheses
                equation_inside_parentheses = calculate_equation(equation_inside_parentheses)
                # replace the equation inside the parentheses with the result
                equation = equation.replace('(' + saved_equation_inside_parentheses + ')',
                                            equation_inside_parentheses)
                # we need to break out of the loop because the equation changed
                # and the loop is still going over the equation as it was before
                # the change, so it will go over indexes that don't exist
                # and cause an error
                break
    # if there are no parentheses in the equation
    # calculate the equation by the priority of the operators
    else:
        # define flag for when size of equation was changed
        size_changed = False

        # define current priority that will go from 6 to 1
        current_priority = 6
        # go over the operators by the priority
        while current_priority > 0 and not size_changed:
            # if the equation is number - return the number
            # this check is needed for when we reach this place
            # while calculating the insider equation in parentheses

            # go over the equation
            if is_number(equation):
                return equation
            for x in range(len(equation)):
                # if the current character is an operator
                if equation[x] in unary_operators or \
                        equation[x] in binary_operators:
                    # if the current operator has the current priority
                    if priority[equation[x]] == current_priority:
                        # if the current operator is a binary operator
                        if equation[x] in binary_operators:
                            # if the case is that we are at the first index
                            # and the operator is a minus sign
                            # then we continue to the next iteration
                            # because that means that the minus sign is
                            # a sign of a negative number
                            if x == 0 and equation[x] == '-':
                                continue
                            # get the number to the left of the operator
                            num_to_the_left = get_number_to_the_left_of_the_operator(equation, x)
                            # get the number to the right of the operator
                            num_to_the_right = get_number_to_the_right_of_the_operator(equation, x)
                            # calculate the equation
                            equation = equation.replace(num_to_the_left + equation[x] +
                                                        num_to_the_right,
                                                        calculate_binary_operator(equation[x],
                                                                                  num_to_the_left,
                                                                                  num_to_the_right))
                            # break out of inner and outer loop
                            size_changed = True
                            break

                        # if the current operator is a right unary operator
                        elif equation[x] in right_unary_operands:
                            # get the number to the left of the operator
                            num_to_the_left = get_number_to_the_left_of_the_operator(equation, x)
                            # if the right unary operator is a factorial
                            # we need to check if the number to the left is a negative number
                            # if it is we need to calculate the equation without negative
                            if equation[x] == '!':
                                # if the number to the left is negative
                                if num_to_the_left[0] == '-':
                                    len_of_left = len(num_to_the_left)
                                    # if the minus sign functions as a sign change
                                    # then we need to calculate the equation with the minus sign
                                    # if the minus sign functions as a binary operator
                                    # then we need to calculate the equation without the minus sign
                                    if equation[x - len_of_left - 1] in binary_operators:
                                        # in this scenario the minus sign functions as
                                        # a sign change
                                        # calculate the equation with the minus sign
                                        pass
                                    elif not equation[x - len_of_left - 1] in binary_operators:
                                        # in this scenario the minus sign functions as
                                        # a binary operator
                                        # we need to calculate the
                                        # equation without the minus sign
                                        num_to_the_left = num_to_the_left[1:]
                            # calculate the equation and replace it with the result
                            equation = equation.replace(num_to_the_left + equation[x],
                                                        calculate_unary_operator(equation[x],
                                                                                 num_to_the_left))
                            # break out of inner and outer loop
                            size_changed = True
                            break
                        # if the current operator is a left unary operator
                        elif equation[x] in left_unary_operands:
                            # get the number to the right of the operator
                            num_to_the_right = get_number_to_the_right_of_the_operator(equation, x)
                            # calculate the equation
                            equation = equation.replace(equation[x] + num_to_the_right,
                                                        calculate_unary_operator(equation[x],
                                                                                 num_to_the_right))
                            # break out of inner and outer loop
                            size_changed = True
                            break
            # decrease the priority
            current_priority -= 1
    # final check to see if the equation is a number
    # if it is a number, return it
    if is_number(equation) or is_negative_number(equation):
        return equation
    # check if there are still operators in the equation
    # if there are still operators in the equation
    # run the function recursively
    elif count_amount_operators_in_equation(equation) > 0:

        # remove extra minus signs
        equation = get_rid_of_extra_minus_signs(equation)
        # run the function again recursively
        return calculate_equation(equation)
    else:
        print('Invalid equation - the equation doesnt have a result')
        exit(1)


def print_operators(binary_operators=BINARY_OPERATORS,
                    unary_operators=UNARY_OPERATORS) -> None:
    """
    print the operators
    :param binary_operators: the binary operators
    :param unary_operators: the unary operators
    :return: None
    """
    # initialize the strings that will contain the operators
    binary = ""
    unary = ""
    for i in binary_operators:
        binary += i + ' '
    for i in unary_operators:
        unary += i + ' '
    print(f'Binary operators: {binary}')
    print(f'Unary operators: {unary} \n')


def print_welcome_message() -> None:
    """
    print welcome message and instructions
    to the user
    :return: None
    """
    print('Welcome to the calculator! ',
          'This is a smart calculator made by @Eldar Aslanbeily \n'
          'You can use the calculator to calculate equations with '
          'the following operators:\n')
    print_operators()
    print('For more information about the calculator, \n'
          'please read the README.md file in the repository \n'
          'at: https://github.com/eldarush/AdvanceddPythonCalculator.git \n'
          'This calculator supports parentheses,'
          'and extra spaces between the operators and operands, \n'
          'but not between the operators themselves.\n'
          'type "exit" or "quit" to exit the program')


def check_for_exit_quit(equation="") -> None:
    """
    check if the user typed 'exit' or 'quit'
    if he did, exit the program
    :param equation: the equation
    :return: None
    """

    # create equation copy, so we can change it
    # without changing the original equation
    equation_copy = equation

    # remove all spaces before and after the equation
    equation_copy = equation_copy.strip()

    # if the user typed 'exit' or 'quit'
    if equation_copy.lower() == 'exit' or equation_copy.lower() == 'quit':
        print('Exiting the program...')
        raise SystemExit


def check_for_continue_c(equation="") -> bool:
    """
    check if the user typed 'continue' or 'c'
    if he did, return True
    :param equation: the equation
    :return: True if the user typed 'continue' or 'c'
    """
    # create copy of the equation, so we can remove spaces
    # without changing the original equation
    equation_copy = equation

    # remove all spaces before and after the equation
    equation_copy = equation_copy.strip()

    # if the user typed 'continue' or 'c'
    if equation_copy.lower() == 'continue' or \
            equation_copy.lower() == 'c':
        return True
    return False


def is_blank(equation="") -> bool:
    """
    check if the equation is blank
    :param equation: the equation
    :return: True if the equation is blank
    """
    # create copy of the equation, so we can remove spaces
    # without changing the original equation
    equation_copy = equation

    # remove all spaces before and after the equation
    equation_copy = equation_copy.strip()

    # if the equation is blank
    if equation_copy == '':
        return True
    return False


def get_equation_from_user(first_run=1, previous_result='') -> str:
    """
    function that gets an equation from the user
    and if the user stops the program,
    print a message and exit the program
    :return:
    """
    # initialize the equation
    input_equation = ""

    # check if the function is called for the first time
    # if it is, print the welcome message
    if first_run == 1:
        print_welcome_message()
        try:
            input_equation = \
                input('Please enter the equation you want to calculate:')
            # if the user entered an empty string
            # ask him to enter an equation
            while is_blank(input_equation):
                input_equation = \
                    input('Seems that you entered a blank equation, '
                          'Please enter the equation you want to calculate:')

            # if the user typed 'exit' or 'quit'
            # exit the program
            check_for_exit_quit(input_equation)
        # if the user stops the program via ctrl + c,
        # print a message and exit the program
        except KeyboardInterrupt:
            print("\n"
                  "Program was interrupted by user")
            exit(1)

    # if the function is not called for the first time
    else:
        print('\nWelcome back to the calculator!\n'
              'type "exit" or "quit" to exit the program\n'
              f'your previous result is: {previous_result}, \n'
              'if you want to use the previous result as an operand,\n'
              'then type your equation with the operand "p" that will be replaced\n'
              'with the previous result\n')
        try:
            input_equation = \
                input('Please enter the equation you want to calculate:')
            # if the user entered an empty string
            # ask him to enter an equation
            while is_blank(input_equation):
                input_equation = \
                    input('Seems that you entered a blank equation, '
                          'Please enter the equation you want to calculate:')

            # if the user typed 'exit' or 'quit'
            # exit the program
            check_for_exit_quit(input_equation)

            # replace the 'p' operand with the previous result
            input_equation = input_equation.replace('p', previous_result)

        except KeyboardInterrupt:
            print('\nProgram was interrupted by user')
            exit(1)

    # return the equation that the user entered
    return input_equation


def calculate(equation="") -> None:
    """
    function that runs the checks and calculates the equation
    this is a function that is used by tne handler file which
    is accessed by the user
    :param equation:
    :return: result of the equation
    """

    # test if for some reason the equation is blank,
    # this should not happen because the equation is checked
    # before it is passed to this function by the get_equation_from_user
    # function in the handler file
    if is_blank(equation):
        print("The entered equation is blank")
        exit(0)

    # check if equation is valid
    equation = check_if_function_is_valid(equation)

    # calculate the result
    result_of_calc = calculate_equation(equation)

    # print the result of the equation
    print("\nResult: {}\n".format(result_of_calc))

    # ask the user if he wants to continue using the calculator
    # or exit the program
    print('If you want to continue using the calculator, '
          'type "continue" or "c"')

    # initialize user_input
    user_input = ''
    try:
        user_input = input('If you want to exit the program,'
                           ' type "exit" or "quit:')
    except KeyboardInterrupt:
        print("\nProgram was interrupted by user")
        exit(1)
    # go in a loop until the user types 'continue' or 'c'
    # or 'exit' or 'quit'
    while not check_for_continue_c(user_input):
        # if the user typed 'exit' or 'quit'
        # exit the program
        check_for_exit_quit(user_input)
        # if the user typed something else
        # ask him to enter 'continue' or 'c'
        user_input = input('Please type "continue" or "c" to continue '
                           'using the calculator or "exit"'
                           ' or "quit" to exit the program:')

    # if the user wants to continue using the calculator,
    # ask him to enter an equation
    calculate(get_equation_from_user(previous_result=result_of_calc,
                                     first_run=0))
