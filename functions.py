# This is a file that contains general functions for the equation
# Path: functions.py
# Author: @Eldar Aslanbeily

from helper_functions import *


def parentheses_surrounding_validity(equation="") -> str:
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

        # check the validly of the right parentheses
        if equation[x] == ')' and x != len(equation) - 1:
            check_right_parentheses_validity(equation,x)

        # if there is closing parentheses at the end of the equation
        # then we don't need to check if there is invalid character
        # after the closing parentheses
        elif equation[x] == ')' and x == len(equation) - 1:
            pass

        # check the validly of the right parentheses
        elif equation[x] == '(' and x != 0:
            check_left_parentheses_validity(equation,x)
        # if there is closing parentheses at the end of the equation
        # then we don't need to check if there is invalid character
        # after the closing parentheses
        elif equation[x] == '(' and x == 0:
            pass

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
                # add 0 according to the situation
                equation =handle_dot_in_the_middle_of_equation(equation,x)
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
        raise SyntaxError('Invalid syntax - number of opening and closing'
              ' parentheses is not the same \n'
              f'equation is: {equation}')

    # check if a closing parentheses is before an opening parentheses
    if equation.find(')') < equation.find('('):
        raise SyntaxError('Invalid syntax - closing parentheses'
              ' is before an opening'
              f'parentheses in equation: {equation}')

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
            raise SyntaxError('Invalid syntax - closing parentheses is'
                  ' before an opening'
                  f' parentheses in equation: {equation}')

    # at the end of the loop, if the counter is not zero,
    # it means that there is an opening parentheses
    # without a closing parentheses
    if counter_opening_parentheses != 0:
        raise SyntaxError('Invalid syntax - number of opening and closing'
              ' parentheses \n is not the'
              f' same in equation {equation}')

    # if we got here, the equation is balanced
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
            raise SyntaxError('Invalid syntax - binary operator at the beginning'
                  ' of the equation, \n'
                  f'at index {0}, equation is: {equation}')

    # check if there is a binary operator at the end of the equation
    if equation[-1] in binary_operators:
        raise SyntaxError('Invalid syntax - binary operator at the end'
              ' of the equation \n'
              f'at index {len(equation) - 1}, equation is: {equation}')

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
                    raise SyntaxError('Invalid syntax - binary operator after'
                          ' another binary operator \n'
                          f'at index {x}, equation is: {equation}')
            # check if the operator is after an opening parentheses
            if equation[x - 1] == '(':
                # check if the operator is not a minus operator
                if equation[x] != '-':
                    raise SyntaxError('Invalid syntax - binary operator after'
                          ' an opening parentheses \n'
                          f'at index {x}, equation is: {equation}')

            # checks for after the operator

            # check if the operator is a minus operator
            if equation[x] == '-':
                # check if the minus is before an operator
                if equation[x + 1] in binary_operators:
                    raise SyntaxError('Invalid syntax - binary operator after a'
                          ' binary operator \n'
                          f'at index {x}, equation is: {equation}')
                # check if the minus is before a closing parentheses
                elif equation[x + 1] == ')':
                    raise SyntaxError('Invalid syntax - closing parentheses after'
                          ' a binary operator \n'
                          f'at index {x}, equation is: {equation}')
            # if the operator is not a minus operator
            else:
                # check if the operator is before an operator
                if equation[x + 1] in binary_operators:
                    # if the operator is not be
                    if equation[x + 1] != '-':
                        raise SyntaxError('Invalid syntax - binary operator after a'
                              ' binary operator \n'
                              f'at index {x}, equation is: {equation}')
                # check if the minus is before a closing parentheses
                elif equation[x + 1] == ')':
                    raise SyntaxError('Invalid syntax - closing parentheses after'
                          ' a binary operator \n'
                          f'at index {x}, equation is: {equation}')

    # return the equation if it is valid
    return equation


def check_validity_of_equation_by_unary_operators(equation="",
                                                  right_unary_operators=RIGHT_ASSOCIATIVE_UNARY_OPERATORS,
                                                  left_unary_operators=LEFT_ASSOCIATIVE_UNARY_OPERATORS) -> str:
    """
    returns the function if all the unary operands
    are valid in it, if not prints error message
    :param left_unary_operators:
    :param right_unary_operators:
    :param equation:
    :return: equation
    """

    # check if the function starts with a right unary operator
    if equation[0] in right_unary_operators:
        raise SyntaxError('Invalid syntax - equation starts with a right unary operator \n'
              f'at index {0}, equation is: {equation}')

    # check if the function ends with a left unary operator
    if equation[-1] in left_unary_operators:
        raise SyntaxError('Invalid syntax - equation ends with a left unary operator \n'
              f'at index {len(equation) - 1}, equation is: {equation}')
    # check the validity of unary operators in the equation

    for x in range(len(equation) - 1):

        # validate the right unary operators
        if equation[x] in right_unary_operators:
            right_unary_validation(equation, x)

        # check if there is a left unary operator that is
        # in front of something that is not a number or an opening parentheses
        if equation[x] in left_unary_operators:
            left_unary_validation(equation, x)

    # return the equation if it is valid
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
                raise SyntaxError('Invalid syntax - binary operator before a right'
                      ' unary operator \n'
                      f'at index {x}, equation is: {equation}')
            elif equation[x - 1] in left_unary_operators:
                # check if there is a left unary operator before a binary operator
                raise SyntaxError('Invalid syntax - binary operator after a left'
                      ' unary operator \n'
                      f'at index {x}, equation is: {equation}')

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
    :param right_unary_operators: the right unary operators
    :param left_unary_operators: the left unary operators
    :param unary_operators: the unary operators
    :param operands: the operands
    :param binary_operators: the binary operators
    :param equation: the equation
    :return: equation with no extra minus signs
    """

    # remove extra minus signs
    equation = remove_triple_minus_signs(equation)

    # if there are minus signs at the end of the equation
    # then return error message because it is invalid syntax
    if equation[-1] == '-':
        raise SyntaxError("Invalid syntax - extra minus sign at the end of the equation \n"
              f"equation is: {equation}")
    # go over the equation and check if there are two consecutive minus signs
    # if there are deal with them
    equation = handle_double_minus_signs(equation)

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


def get_rid_of_extra_white_spaces(equation="", ) -> str:
    """
    simply get rid of extra white spaces in the equation
    :param equation: the equation
    :return: equation with no extra white spaces
    """
    equation = equation.replace(' ', '')

    return equation


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
        # if it is, return the equation
        return add_zero_before_and_after_dot_integer(equation)

    # else: the equation is not a number:
    # continue with the program
    # try to run all the functions that check if the equation is valid,
    # if one of the functions fails, the equation is not valid
    # we need to catch the error and print the error message
    try:

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

        # TODO: fix problem with ~-~3
        # check validity of equation by both binary and unary operators
        equation = check_validity_of_equation_by_all_operators(equation)

    # except the error and print the error message
    except Exception as error:
        print(error)
        # exit the program with error code 1
        exit(1)

    # return the equation if it is valid
    return equation


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

    # first of all, the function will calculate the
    # sub equation in parentheses, and replace it with the result
    # the sub equation in parentheses will be done in the
    # calculate_sub_equation_in_parentheses function called recursively

    # first we find if there are any right unary operators in the equation
    # that follow a closing parentheses
    # if there are, we calculate the sub equation in parentheses and
    # then calculate the right unary operator on the result
    for x in range(len(equation)):
        # if the current character is a closing parentheses
        if equation[x] == ')' and x != len(equation) - 1:
            # if the next character is a right unary operator
            if equation[x + 1] in right_unary_operands:
                # we need to find the matching opening parentheses
                # to the closing parentheses we found
                opening_parentheses_index = find_opening_parentheses(equation, x)

                # we need to check if the character before the parentheses is a left unary operator
                # if it is, we need to calculate the left unary operator on the sub equation
                # in parentheses and then calculate the right unary operator on the result
                if opening_parentheses_index != 0 \
                        and equation[opening_parentheses_index - 1] in left_unary_operands:
                    # calculate the left unary operator on the sub equation in parentheses
                    # this is equivalent to calculating the equation with one index backwards
                    result_inside = calculate_equation(equation[opening_parentheses_index + 1:x])
                    # calculate the right unary operator on the result inside
                    # the parentheses
                    # now we apply the left unary operator on the result of the equation
                    # inside the parentheses
                    result_inside = \
                        calculate_unary_operator(equation[opening_parentheses_index - 1],
                                                 result_inside)
                    result = calculate_unary_operator(equation[x + 1], result_inside)
                    # replace the result and the left unary operator and the right unary operator
                    # with the result of the calculation
                    equation = equation[:opening_parentheses_index - 1] + result + \
                               equation[x + 2:]
                else:
                    result_inside = calculate_equation(equation[opening_parentheses_index + 1:x])
                    # calculate the right unary operator on the result inside
                    # the parentheses
                    result = calculate_unary_operator(equation[x + 1], result_inside)
                    # replace the parentheses and the right unary operator with
                    # the result
                    equation = equation[:opening_parentheses_index] + result + equation[x + 2:]

                # call the function recursively to calculate the equation
                # again
                # we need to check if the equation is valid again
                # after the change
                equation = check_if_function_is_valid(equation)
                return calculate_equation(equation)

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
                # we need to check if the equation is valid again
                # after the change
                equation = check_if_function_is_valid(equation)
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
                            # we need to check if the number to the left is a negative number
                            # if it is we need to calculate the equation without negative
                            # if the number to the left is negative
                            if num_to_the_left[0] == '-':
                                len_of_left = len(num_to_the_left)
                                # if the minus sign functions as a sign change
                                # then we need to calculate the equation with the minus sign
                                # if the minus sign functions as a binary operator
                                # then we need to calculate the equation without the minus sign

                                # first we check if the minus sign is at the beginning of the equation
                                # if it is we need to calculate the equation with the minus sign
                                if x - len_of_left - 1 < 0:
                                    pass
                                elif equation[x - len_of_left - 1] in binary_operators:
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
                            # get the number to the right of the operator
                            num_to_the_right = get_number_to_the_right_of_the_operator(equation, x)
                            # calculate the equation
                            # and replace it with the result
                            equation = equation.replace(num_to_the_left + equation[x] +
                                                        num_to_the_right,
                                                        calculate_binary_operator(equation[x],
                                                                                  num_to_the_left,
                                                                                  num_to_the_right))
                            # break out of inner and outer loop
                            # we need to check if the equation is valid again
                            # after the change
                            equation = check_if_function_is_valid(equation)
                            size_changed = True
                            break

                        # if the current operator is a right unary operator
                        elif equation[x] in right_unary_operands:
                            # get the number to the left of the operator
                            num_to_the_left = get_number_to_the_left_of_the_operator(equation, x)
                            # in the case that the operator is a right unary operator
                            # we need to check if the number to the left is a negative number
                            # if it is we need to calculate the equation without negative
                            # if the number to the left is negative
                            # we need to calculate the equation without the minus sign
                            if num_to_the_left[0] == '-':
                                len_of_left = len(num_to_the_left)
                                # if the minus sign functions as a sign change
                                # then we need to calculate the equation with the minus sign
                                # if the minus sign functions as a binary operator
                                # then we need to calculate the equation without the minus sign

                                # first we check if the minus sign is at the beginning of the equation
                                # if it is we need to calculate the equation with the minus sign
                                # we need to check if the negative number is before the operator #,
                                # if it is we need to calculate the equation without the minus sign
                                # and if the negative number is before any other operator, we need to
                                # calculate the equation with the minus sign
                                if x - len_of_left - 1 < 0 and equation[x] != '#':
                                    pass

                                # if the number to the left is negative and the right unary operator
                                # is a # sign, then we need to apply the unary operator to the number
                                # without the minus sign
                                elif equation[x] == '#' and (equation[x - len_of_left - 1] in binary_operators
                                                             or equation[x - len_of_left - 1] == '('
                                                             or x - len_of_left - 1 == 0):
                                    num_to_the_left = num_to_the_left[1:]
                                elif equation[x - len_of_left - 1] in binary_operators:
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
                            # we need to check if the equation is valid again
                            # after the change
                            equation = check_if_function_is_valid(equation)
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
                            # we need to check if the equation is valid again
                            # after the change
                            equation = check_if_function_is_valid(equation)
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

        # we need to check if the equation is valid again
        # after the change
        equation = check_if_function_is_valid(equation)
        # run the function again recursively
        return calculate_equation(equation)
    else:
        raise SyntaxError('Invalid equation - the equation doesnt have a result \n '
              'or the equation is invalid \n'
              f'equation calculated so far is: {equation}')


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
        print('The entered equation is blank')
        exit(0)

    # check if equation is valid
    equation = check_if_function_is_valid(equation)

    result_of_calc = ''
    # try and calculate the equation
    try:
        # calculate the result
        result_of_calc = calculate_equation(equation)

    # except the exception that is raised when the equation is invalid
    # and print a message to the user
    except Exception as error:
        print(error)
        exit(1)

    # print the result of the equation
    print('\nResult: {}\n'.format(result_of_calc))

    # ask the user if he wants to continue using the calculator
    continue_using_calculator()

    # if the user wants to continue using the calculator,
    # ask him to enter an equation
    calculate(get_equation_from_user(previous_result=result_of_calc,
                                     first_run=0))
