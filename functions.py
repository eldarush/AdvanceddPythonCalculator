# This is a file that contains general functions for the equation
# Path: functions.py
# Author: @Eldar Aslanbeily


def is_number(s: str) -> bool:
    """
    simple function that checks if a string is a number
    this function receives a string and returns
    true if the string is a number and false otherwise
    :param s:
    :return:
    """
    try:
        float(s)
        return True
    except ValueError:
        return False


def doesnt_contain_numbers(equation: str) -> bool:
    """
    This function checks if an equation contains numbers
    :param equation:
    :return:
    """
    for x in equation:
        if x.isdigit():
            return False
    return True


def contains_number_after_closing_parentheses(equation: str) -> bool:
    """
    function that checks if an equation contains a number
    after a closing parentheses
    For example: 2(3)4 is not valid
    or 2(3+4)5 is not valid but 2(3+4) is valid
    :param equation:
    :return: true if there is a number after a closing parentheses
    and false otherwise
    """
    # go over equation and check if there is a number
    # after a closing parentheses
    for x in range(len(equation) - 1):
        if equation[x] == ')' and equation[x + 1].isdigit():
            return True
    return False


def check_for_double_dots(equation: str) -> str:
    """
    function that checks if there are two dots in a row
    :param equation:
    :return: equation if there are no two dots in a row
    and throws an exception otherwise
    """
    # go over equation and check if there are two dots in a row
    for x in range(len(equation) - 1):
        if equation[x] == '.' and equation[x + 1] == '.':
            raise Exception('Invalid syntax - two dots in a row ')
    return equation


def check_for_number_with_too_many_dots_in_them(equation: str) -> str:
    """
    function that checks if there are numbers with too many dots in them
    :param equation:
    :return: equation if there are no numbers with too many dots in them
    and throws an exception otherwise
    """
    # go over equation and check if there are numbers with too many dots in them
    for x in range(len(equation) - 1):
        if equation[x].isdigit() and equation[x + 1] == '.' and equation[x + 2].isdigit()\
                and equation[x + 3] == '.':
            raise Exception('Invalid syntax - number with too many dots in it')
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
                if not equation[x-1].isdigit():
                    equation = equation[:x] + '0' + equation[x:]
                elif not equation[x+1].isdigit():
                    equation = equation[:x+1] + '0' + equation[x+1:]
        x += 1
    # return the equation with a zero before and after a dot
    return equation


def check_if_function_is_valid(equation: str, operators: set, operands: set,
                               binary_operators: set, unary_operators: set,
                               priority: dict) -> str:
    """
    This function checks if the equation is valid,
    the function receives the equation, the sets of operators and operands,
    and the dictionary of priorities for the operators and checks,
    if the equation is not valid, if the equation is not valid,
    the program throws an exception, if the equation is valid,
    the function returns the equation
    :param equation:
    :param operators:
    :param operands:
    :param binary_operators:
    :param unary_operators:
    :param priority:
    :return: equation if it is valid and throws an exception otherwise
    """

    # check if the equation is just a number
    if is_number(equation):
        return equation

    # else: the equation is not a number:
    # continue with the program

    # check if the equation doesn't contain numbers
    if doesnt_contain_numbers(equation):
        raise Exception("The equation doesn't contain numbers")

    # check if equation only contains operators and operands
    for x in equation:
        if x not in operators and x not in operands:
            raise Exception('Invalid token: {}'.format(x))

    # check if the equation contains two consecutive dots
    check_for_double_dots(equation)

    # add a zero before and after a dot if needed
    equation = add_zero_before_and_after_dot_integer(equation)

    # check if there is a number with too many dots in it
    check_for_number_with_too_many_dots_in_them(equation)

    # check if equation is balanced
    # meaning that there are the same
    # number of opening and closing parentheses
    if equation.count('(') != equation.count(')'):
        raise Exception('Invalid syntax - number of opening and closing'
                        ' parentheses is not the same on token'
                        ' {}'.format(equation))

    # check if a closing parentheses is before an opening parentheses
    if equation.find(')') < equation.find('('):
        raise Exception('Invalid syntax - closing parentheses'
                        ' is before an opening'
                        ' parentheses on token {}'.format(equation))

    # check if every opening parentheses has a closing parentheses
    counter_opening_parentheses = 0
    for x in equation:
        if x == '(':
            counter_opening_parentheses += 1
        elif x == ')':
            counter_opening_parentheses -= 1
        if counter_opening_parentheses < 0:
            raise Exception('Invalid syntax - closing parentheses is'
                            ' before an opening'
                            ' parentheses on token {}'.format(equation))

    if counter_opening_parentheses != 0:
        raise Exception('Invalid syntax - number of opening and closing'
                        ' parentheses is not the'
                        ' same on token {}'.format(equation))

    # check if equation contains a number after a closing parentheses
    if contains_number_after_closing_parentheses(equation):
        raise Exception("There is a number after a closing parentheses "
                        "at the equation, Syntax Error")

    # TODO: confirm if this check is needed, if it is, fix it
    # # check if there are two operators in a row
    # for x in range(len(equation) - 1):
    # # check if there are two binary operators in a row
    # # only exceptions when there is a unary operator
    # # in front of a binary operator or when
    # # there is a closing parentheses
    # # in front of a binary operator
    # # or if there is a minus sign in front of a binary operator
    # # (- as in sign change not subtraction)
    # if equation[x] in binary_operators and \
    #         equation[x + 1] in binary_operators and equation[x + 1] != '-':
    #     raise Exception('Invalid syntax - two operators in a row '
    #                     'on token {}'.format(equation))
    return equation


def get_rid_of_extra_parentheses(equation: str) -> str:
    """
    function that gets an equation and
    gets rid of extra parentheses in the equation
    F.E 2()()() is just 2
    or 2(3)() is just 2(3) and so on
    :param equation:
    :return: equation with no extra parentheses
    """
    # go over equation and get rid of extra parentheses
    equation = equation.replace('()', '')

    # return the equation with no extra parentheses
    return equation


# TODO: implement this function
def get_rid_of_extra_minus_signs(equation: str) -> str:
    """
    function that gets rid of extra minus signs
    F.E 2---3 is just 2-3
    or 2-(-3) is just 2+3
    :param equation:
    :return: equation with no extra minus signs
    """
    # go over equation and get rid of extra minus signs
    # this is done by replacing -- with +
    equation = equation.replace('--', '+')
    return equation


# TODO: implement this function
def get_rid_of_extra_white_spaces(equation: str) -> str:
    """
    function that gets rid of extra white spaces
    and also checks if there are illegal white spaces
    between two operands
    :param equation:
    :return: equation with no extra white spaces
    """
    # # Removing any unwanted white spaces,
    # tabs, or new lines from the equation string:
    #     equation = re.sub(r"[\n\t\s]*", "", equation)
    #     # Creating a list based on the equation string:
    #     result_list = re.split(r'([-+*/^~%!@$&()])|\s+', equation)
    #     # Filtering the list - Removing all the unwanted
    #     "spaces" from the list:
    #     result_list = [value for value in result_list if
    #     value not in ['', ' ', '\t']]

    # # s = "((8   1 *     6) /  42  + (3-1))"
    # s= "5  2        + 4.0  "
    # r = [""]
    #
    # for i in s.replace(" ", ""):
    #     if i.isdigit() and r[-1].isdigit():
    #         r[-1] = r[-1] + i
    #     else:
    #         r.append(i)
    #
    # print(r[1:])
    return equation


def put_multiplication_in_front_of_opening_parentheses(equation : str) -> str:
    """
    function that gets an equation and puts a multiplication sign
    in front of opening parentheses where needed
    f.e. 2(3+4) -> 2*(3+4)
    or 2(3+4)(5+6) -> 2*(3+4)*(5+6)
    but 2(3+4)5 -> 2*(3+4)5 and not 2*(3+4)*5
    also 2(3+4)(5+6)5 -> 2*(3+4)*(5+6)5 and not 2*(3+4)*(5+6)*5
    and 5((3+4)(5+6)) -> 5*((3+4)*(5+6))
    :param equation:
    :return: corrected equation
    """
    for x in range(len(equation)):
        # if the current character is an opening parentheses
        if equation[x] == '(':
            # if the character before the current character
            # is a digit, or a closing parentheses
            if equation[x - 1].isdigit() or \
                    equation[x - 1] == ')':
                # put a multiplication sign in front of the parentheses
                equation = equation[:x] + '*' + equation[x:]
    return equation


def find_closing_parentheses(equation: str, index: int) -> int:
    """
    this function gets an euqation, and a strting index
    of the opening parantheses and returns the index of the
    closing parentheses
    :param equation: the equation
    :param index: the index of the opening parentheses
    :return: the index of the closing parentheses
    """
    # check if the character at the index is an opening parentheses
    if equation[index] != '(':
        raise Exception('Invalid syntax - the character at the index'
                        ' is not an opening parentheses')

    # check if the index is in the equation
    if index >= len(equation):
        raise Exception('Invalid syntax - the index is out of range')

    # check if the index is not negative
    if index < 0:
        raise Exception('Invalid syntax - the index is negative')

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
            raise Exception('Invalid syntax - no closing parentheses'
                            ' for the opening parentheses at the index')

    # if we reach end and counter is not 0, raise exception
    # technically this should never happen because the function
    # is run after the equation is checked for parentheses errors
    # but just in case we will raise an exception
    if counter_opening_parentheses != 0:
        raise Exception('Invalid syntax - no closing parentheses'
                        ' for the opening parentheses at the index')

def simplify_equation(equation: str) -> str:
    """
    function that simplifies the equation
    :param equation:
    :return: simplified equation
    """
    # get rid of extra parentheses
    equation = get_rid_of_extra_parentheses(equation)

    # get rid of extra minus signs
    equation = get_rid_of_extra_minus_signs(equation)

    # get rid of extra white spaces
    equation = get_rid_of_extra_white_spaces(equation)

    # put * in front of opening parentheses where needed
    equation = put_multiplication_in_front_of_opening_parentheses(equation)

    # return the simplified equation
    return equation


# TODO: implement this function
def calculate_equation(equation: str, binary_operators: set,
                       unary_operators: set, priority: dict) -> str:
    """
    general function that calculates the equation, this function
    will be run recursively until the equation is solved
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
