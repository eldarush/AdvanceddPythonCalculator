# this is a file that contains all the functions that are used in the functions file
# the functions in this file are used inside the more general functions
# Path: helper_functions.py
# Author: @Eldar Aslanbeily

from globals import *

def is_number(equation="") -> bool:
    """
    simple function that checks if a string is a number
    this function receives a string and returns
    true if the string is a number and false otherwise
    :param equation: the string
    :return: true if the string is a number and false otherwise
    """

    # try to convert the string to a float, if it works then it is a number
    try:
        float(equation)
        return True

    # if the string is not a number, then return false
    except ValueError:
        return False


def contains_invalid_characters(equation="", operators=OPERATORS,
                                operands=OPERANDS) -> str:
    """
    This function checks if the equation contains invalid characters
    :param equation: the equation
    :param operators: the operators
    :param operands: the operands
    :return: True if the equation contains invalid characters, False otherwise
    """
    for x in equation:
        if x not in operators and x not in operands:
            raise SyntaxError("Invalid syntax - The equation contains invalid characters \n"
                  f"at index {x}, equation is: {equation}")
    return equation


def is_negative_number(equation="") -> bool:
    """
    this function gets an equation and returns whether
    the equation contains only a minus sign and numbers
    after the minus sign to indicate a negative number
    :param equation: the equation
    :return: whether the equation contains only a minus sign
     and valid operands
    """
    # go over the equation and check if there is a minus sign
    # and if there are only numbers after the minus sign

    # if the equation is empty or its just 1 character long
    # return false
    if len(equation) <= 1:
        return False

    return equation[0] == '-' and is_number(equation[1:]) \
           and equation[1:].count('-') == 0


def doesnt_contain_numbers(equation="") -> bool:
    """
    This function checks if an equation contains numbers
    :param equation: the equation
    :return: True if the equation doesn't contain numbers, False otherwise
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
    :param equation: the equation
    :return: equation if the function doesn't contain numbers,
    and raises a syntax error otherwise
    """
    # check if the equation doesn't contain numbers
    if doesnt_contain_numbers(equation):
        raise SyntaxError('Invalid syntax - equation does not contain numbers, \n'
              f'equation is: {equation}')

    # if the equation contains numbers, then return the equation
    return equation


def check_right_parentheses_validity(equation="", index=0,
                                     left_unary_operators=
                                     LEFT_ASSOCIATIVE_UNARY_OPERATORS) -> None:
    """
    function that checks if the right parentheses is valid
    :param equation: the equation
    :param index: the index of the right parentheses
    :param left_unary_operators: the left unary operators
    :return: None if the right parentheses is valid
    and raises a syntax error otherwise
    """
    if is_number(equation[index + 1]) or equation[index + 1] == '(' \
            or equation[index + 1] in left_unary_operators:
        # raise syntax exception
        raise SyntaxError("Invalid syntax - number or opening parentheses "
                          "or left unary operator after closing parentheses \n"
                          f"at index {index}, equation is: {equation}")


def check_left_parentheses_validity(equation="", index=0,
                                    right_unary_operators=
                                    RIGHT_ASSOCIATIVE_UNARY_OPERATORS) -> None:
    """
    function that checks if the left parentheses is valid
    :param equation: the equation
    :param index: the index of the left parentheses
    :param right_unary_operators: the right unary operators
    :return: None if the left parentheses is valid
    and raises a syntax error otherwise
    """
    if is_number(equation[index - 1]) or equation[index - 1] == ')' \
            or equation[index - 1] in right_unary_operators:
        # raise syntax exception
        raise SyntaxError("Invalid syntax - number or closing parentheses "
                          "or right unary operator before opening parentheses \n"
                          f"at index {index}, equation is: {equation}")


def check_for_double_dots(equation="") -> str:
    """
    function that checks if there are two dots in a row
    :param equation: the equation
    :return: equation if there are no two dots in a row
    and prints an error message otherwise
    """
    # go over equation and check if there are two dots in a row
    for x in range(len(equation) - 1):
        if equation[x] == '.' and equation[x + 1] == '.':
            raise SyntaxError('Invalid syntax - two dots in a row \n'
                  f'at index {x}, equation is: {equation}')
    return equation


def check_for_number_with_too_many_dots_in_them(equation="") -> str:
    """
    function that checks if there are numbers with too many dots in them
    :param equation: the equation
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
            # if we encounter a dot and the flag is true
            # then we have a number with too many dots in it
            if flag:
                raise SyntaxError('Invalid syntax - number with too'
                      ' many decimal points in it \n'
                      f'at index {x}, equation is: {equation}')
            # if we encounter a dot and the flag is false
            # then we set the flag to true
            else:
                flag = True
        elif not is_number(x):
            flag = False
    return equation


def handle_dot_in_the_middle_of_equation(equation="", index =0) -> str:
    """
    function that handles the dot in the middle of the equation
    :param equation: the equation
    :param index: the index of the dot
    :return: the equation with extra 0 where needed
    """
    # if there is no number before the dot
    # then we add a 0 before the dot
    if not is_number(equation[index - 1]):
        equation = equation[:index] + '0' + equation[index:]

    # if there is no number after the dot
    # then we add a 0 after the dot
    elif not is_number(equation[index + 1]):
        equation = equation[:index + 1] + '0' + equation[index + 1:]

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
        raise SyntaxError('Invalid syntax - the index is out of range \n'
              f'at index {index}, equation is: {equation}')

    # check if the index is not negative
    if index < 0:
        raise SyntaxError('Invalid syntax - the index is negative \n'
              f'at index {index}, equation is: {equation}')

    # if the index is at the end of the equation
    if index == len(equation) - 1:
        raise SyntaxError('Invalid syntax - the operator is at the end of the equation \n'
              f'at index {index}, equation is: {equation}')

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
        raise SyntaxError('Invalid syntax - the index is out of range \n'
              f'at index {index}, equation is: {equation}')

    # check if the index is not negative
    if index < 0:
        raise SyntaxError('Invalid syntax - the index is negative \n'
              f'at index {index}, equation is: {equation}')

    # if the index is at the start of the equation,
    # but the operator is not a minus sign (that will stand
    # for a negative number)
    if index == 0:
        if equation[index] != '-':
            raise SyntaxError('Invalid syntax - the operator is at the start of the equation \n'
                  f'at index {index}, equation is: {equation}')
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


def right_unary_validation(equation="", index=0,
                           right_unary_operators=RIGHT_ASSOCIATIVE_UNARY_OPERATORS) -> None:
    """
    this function gets an equation and an index of an operator,
    and checks if the operator is a right unary operator is valid or not
    this is done by checking the surrounding characters of the operator
    :param equation: the equation
    :param index: the index of the operator
    :param right_unary_operators: the right unary operators
    :return: None if the operator is valid, otherwise raises an error
    """
    # check if the right unary operator is after a number
    previous_number = get_number_to_the_left_of_the_operator(equation, index)
    if not is_number(equation[index - 1]) and equation[index - 1] != ')' and equation[index - 1] not \
            in right_unary_operators and not is_number(previous_number):
        raise SyntaxError('Invalid syntax - right unary operator after something'
                          ' that is not a number or a closing parentheses \n'
                          f'at index {index}, equation is: {equation}')
    # check if the next character is a number or an opening parentheses
    # this check prevents the user from writing something like 5!5
    if index != len(equation) - 1:
        # if the right unary operator is not the last character
        # in the equation, check if the next character is a number
        # or an opening parentheses
        if is_number(equation[index + 1]) or equation[index + 1] == '(':
            raise SyntaxError('Invalid syntax - right unary followed by'
                              ' a number or an opening parentheses \n'
                              f'at index {index}, equation is: {equation}')


def left_unary_validation(equation="", index=0) -> None:
    """
    this function gets an equation and an index of an operator,
    and checks if the operator is a left unary operator is valid or not
    this is done by checking the surrounding characters of the operator
    :param equation: the equation
    :param index: the index of the operator
    :return: None if the operator is valid, otherwise raises an error
    """
    # get the next number after the left unary operator
    next_number = get_number_to_the_right_of_the_operator(equation, index)
    if not is_number(equation[index + 1]) and equation[index + 1] != '(' \
            and not is_negative_number(next_number):
        raise SyntaxError('Invalid syntax - left unary operator in front of'
                          ' something that is not a number or an opening parentheses \n'
                          f'at index {index}, equation is: {equation}')

    # check if the last character is a number or a closing parentheses
    # this check prevents the user from writing something like 5~5
    if index != 0:
        # if the left unary operator is not the first character
        # in the equation, check if the character before it is a number
        # or a closing parentheses
        if is_number(equation[index - 1]) or equation[index - 1] == ')':
            raise SyntaxError('Invalid syntax - left unary operator following'
                              ' a number or a closing parentheses \n'
                              f'at index {index}, equation is: {equation}')


def check_for_extra_parentheses(equation="") -> str:
    """
    function that checks if there are extra parentheses
    in the equation that don't do anything
    and if there are, prints error message
    and ends the program
    :param equation: the equation
    :return: same equation if there are no extra parentheses
    """

    # check if there are extra parentheses
    if '()' in equation:
        raise SyntaxError("Invalid syntax, extra parentheses in the equation")

    # if there are no extra parentheses, return the equation
    return equation


def get_number_after_minus_signs(equation="", index=0) -> str:
    """
    function that gets an equation and an index of the first minus
    sign and returns the whole number after all the minus signs
    :param equation: the equation
    :param index: the index of the first minus sign
    :return: the number after the minus signs
    """
    # get the index of the first number after all the minus signs
    # and return the number
    # min index is the index of the first minus sign
    # after the first minus sign
    min_index = index + 1
    # initialize the number to be returned
    number = ""
    while equation[min_index] == '-':
        number += equation[min_index]
        min_index += 1

    # now minIndex is the index of the first number after all the minus signs
    # we get the complete number after all the minus signs
    # and return it
    while min_index < len(equation) and \
            (is_number(equation[min_index]) or equation[min_index] == '.'):
        number += equation[min_index]
        min_index += 1

    # return the number
    return number


def remove_triple_minus_signs(equation="")-> str:
    """
    function that removes all the triple minus signs
    from the equation, and replaces them with a single minus sign
    :param equation: the equation
    :return: the equation without triple minus signs
    """
    # replace all triple minus signs with -
    while '---' in equation:
        equation = equation.replace('---', '-')

    # return the equation
    return equation


def is_stronger_than_minus_sign(equation="", index=0) -> bool:
    """
    function that gets an equation and an index of the operator
    and checks if the operator is stronger than the minus sign
    :param equation: the equation
    :param index: the index of the operator
    :return: True if the operator is stronger than the minus sign
    """
    return STRONGER_THAN_UNARY_MINUS[equation[index]]


def handle_double_minus_signs(equation="", operands=OPERANDS,
                                 binary_operators=BINARY_OPERATORS,
                                 right_unary_operators=RIGHT_ASSOCIATIVE_UNARY_OPERATORS,
                                 left_unary_operators=LEFT_ASSOCIATIVE_UNARY_OPERATORS) -> str:

    """
    function that handles the double minus signs in the equation
    :param equation: the equation
    :param operands: the operands
    :param binary_operators: the binary operators
    :param right_unary_operators: the right unary operators
    :param left_unary_operators: the left unary operators
    :return: the equation without double minus signs
    """
    # go over the equation and check if there are double minus signs
    # if there are, replace them with +  or delete them, or replace with -(-
    # depending on the situation
    for x in range(len(equation) - 1):
        # if there are two minus signs in a row
        if equation[x] == '-' and equation[x + 1] == '-':
            # if the double minus sign is at the beginning of the equation
            if x == 0:
                # if after the double minus signs there is a number
                # we need to check if the next operator is stronger than the minus
                # if it is, then we need to remove the double minus sign
                num_right_of_first_minus_sign = get_number_after_minus_signs(equation, x)
                if is_stronger_than_minus_sign(equation,x + len(num_right_of_first_minus_sign) + 1):
                    # remove the double minus sign
                    equation = equation[x + 2:]
                    # break the loop and start over
                    break

            # if the double minus sign is before a number
            # or an opening parentheses or a left unary operator
            if is_number(equation[x + 2]) or equation[x + 2] == '(' or \
                    equation[x + 2] in left_unary_operators:
                # if the double minus sign is after a binary operator
                if equation[x - 1] in binary_operators or equation[x - 1] \
                        in left_unary_operators or equation[x - 1] == '(':
                    # remove the double minus sign
                    equation = equation[:x] + equation[x + 2:]
                    break
                # if the double minus sign is after an operand
                # or a closing parentheses or a right unary operator
                elif equation[x - 1] in operands or equation[x - 1] == ')' \
                        or equation[x - 1] in right_unary_operators:

                    # the cases where -- immediately becomes + are:
                    # 1. -- is before an opening parentheses
                    # 2. -- is before a left unary operator
                    if equation[x + 2] == '(' or equation[x + 2] in left_unary_operators:
                        # replace the double minus sign with +
                        equation = equation[:x] + '+' + equation[x + 2:]
                        break

                    # then replace the double minus sign with a plus sign
                    # change the double minus sign to a minus sign,
                    # and add parentheses around the number after the second minus sign
                    num_right_of_first_minus_sign = get_number_after_minus_signs(equation, x)


                    # if the next character after the number is stronger than minus, then we can just replace
                    # the double minus sign with a plus sign, and not add parentheses
                    # but if the next character is not stronger than minus, then we need to add parentheses
                    # to the number after the first minus sign to indicate to the operator that
                    # the number after the first minus sign is negative
                    if x + 1 + len(num_right_of_first_minus_sign) < len(equation) and \
                            is_stronger_than_minus_sign(equation,x + 1 + len(num_right_of_first_minus_sign)):
                        # replace the double minus sign with a plus sign
                        equation = equation[:x] + '+' + equation[x + 2:]
                        break
                    # if the next character after the number is not a #, then we need to add
                    # parentheses around the number
                    elif x + 1 + len(num_right_of_first_minus_sign) < len(equation) and not\
                             is_stronger_than_minus_sign(equation,x + 1 + len(num_right_of_first_minus_sign)):
                        equation = equation[:x + 1] + '(' + num_right_of_first_minus_sign + ')' \
                                   + equation[x + 1 + len(num_right_of_first_minus_sign):]
                        break
                    # if we reached here then we need to replace the double minus sign with
                    # a plus sign, because the number is at the end of the equation
                    else:
                        # replace the double minus sign with a plus sign
                        equation = equation[:x] + '+' + equation[x + 2:]
                        break

            # if the double minus sign is before a closing parentheses
            elif equation[x + 2] == ')':
                # print error message and exit
                raise SyntaxError("Invalid syntax - extra minus sign before a closing "
                      "parentheses \n"
                      f"at index {x}, equation is: {equation}")
            # if the double minus sign is before a unary operator
            elif equation[x + 2] in right_unary_operators:
                # print error message and exit
                raise SyntaxError("Invalid syntax - extra minus sign before a right "
                      "unary operator \n"
                      f"at index {x}, equation is: {equation}")
            # if the double minus sign is before a binary operator
            elif equation[x + 2] in binary_operators:
                # print error message and exit
                raise SyntaxError("Invalid syntax - extra minus sign before a binary "
                      "operator \n"
                      f"at index {x}, equation is: {equation}")

    # if we reached here then we need to return the equation
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
        raise SyntaxError('Invalid syntax - the character at the index'
              ' is not an opening parentheses \n'
              f'at index {index}, equation is: {equation}')

    # check if the index is in the equation
    if index >= len(equation):
        raise SyntaxError('Invalid syntax - the index is out of range \n'
              f'at index {index}, equation is: {equation}')

    # check if the index is not negative
    if index < 0:
        raise SyntaxError('Invalid syntax - the index is negative \n'
              f'at index {index}, equation is: {equation}')

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
        raise SyntaxError('Invalid syntax - no closing parentheses'
              ' for the opening parentheses  \n'
              f'at index {index}, equation is: {equation}')


def find_opening_parentheses(equation="", index=0) -> int:
    """
    this function gets an equation, and a starting index
    of the closing parentheses and returns the index of the
    opening parentheses
    :param equation: the equation
    :param index: the index of the closing parentheses
    :return: the index of the opening parentheses
    """
    # check if the character at the index is a closing parentheses
    if equation[index] != ')':
        raise SyntaxError('Invalid syntax - the character at the index'
              ' is not a closing parentheses \n'
              f'at index {index}, equation is: {equation}')

    # check if the index is in the equation
    if index >= len(equation):
        raise SyntaxError('Invalid syntax - the index is out of range \n'
              f'at index {index}, equation is: {equation}')

    # check if the index is not negative
    if index < 0:
        raise SyntaxError('Invalid syntax - the index is negative \n'
              f'at index {index}, equation is: {equation}')

    # counter for the number of closing parentheses
    counter_closing_parentheses = 0

    # go over the equation from the index
    for x in range(index, -1, -1):

        # if the current character is a closing parentheses
        if equation[x] == ')':
            # increase the counter
            counter_closing_parentheses += 1

        # if the current character is an opening parentheses
        if equation[x] == '(':
            # decrease the counter
            counter_closing_parentheses -= 1

        # if the counter is 0
        if counter_closing_parentheses == 0:
            # return the index of the opening parentheses
            return x

    # if we reach end and counter is not 0, print error message
    # technically this should never happen because the function
    # is run after the equation is checked for parentheses errors
    # but just in case we will print an error message
    if counter_closing_parentheses != 0:
        raise SyntaxError('Invalid syntax - no opening parentheses'
              ' for the closing parentheses  \n'
              f'at index {index}, equation is: {equation}')


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


def print_operators(binary_operators=BINARY_OPERATORS,
                    unary_operators=UNARY_OPERATORS) -> None:
    """
    print the operators
    :param binary_operators: the binary operators
    :param unary_operators: the unary operators
    :return: the function prints the operators
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
    :return: the function prints the welcome message
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
    :return: exit the program if the user typed 'exit' or 'quit'
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
    :return: the equation that the user typed
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
            print('\nProgram was interrupted by user')
            exit(1)
        # if the input is an EOF, exit the program
        except EOFError:
            print('\nProgram was interrupted by user - input contains EOF')
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
        # if the user stops the program via ctrl + c,
        # print a message and exit the program
        except KeyboardInterrupt:
            print('\nProgram was interrupted by user')
            exit(1)
        # if the input is an EOF, exit the program
        except EOFError:
            print('\nProgram was interrupted by user - input contains EOF')
            exit(1)

    # return the equation that the user entered
    return input_equation


def continue_using_calculator() -> None:
    """
    function that asks the user if he wants to continue using the calculator
    if he does, call the main function again
    if he doesn't, exit the program
    :return: the function calls the main function again if the user wants to
    """
    print('If you want to continue using the calculator, '
          'type "continue" or "c"')

    # initialize user_input
    user_input = ''
    try:
        user_input = input('If you want to exit the program,'
                           ' type "exit" or "quit:')
    except KeyboardInterrupt:
        print('\nProgram was interrupted by user')
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