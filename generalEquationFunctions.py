# This is a file that contains general functions for the equation
# Path: qualityOfLifeFunctions.py
# Author: @Eldar Aslanbeily


# check if equation is valid
def check_if_function_is_valid(equation: str, operators: set, operands: set,
                               binary_operators: set, unary_operators: set, priority: dict) -> str:
    # check if equation only contains operators and operands
    for x in equation:
        if x not in operators and x not in operands:
            raise Exception('Invalid token: {}'.format(x))

    # check if equation is balanced
    # meaning that there are the same number of opening and closing parentheses
    if equation.count('(') != equation.count(')'):
        raise Exception('Invalid syntax - number of opening and closing'
                        ' parentheses is not the same on token {}'.format(equation))

    # check if a closing parentheses is before an opening parentheses
    if equation.find(')') < equation.find('('):
        raise Exception('Invalid syntax - closing parentheses is before an opening'
                        ' parentheses on token {}'.format(equation))

    # check if every opening parentheses has a closing parentheses
    counter_opening_parentheses = 0
    for x in equation:
        if x == '(':
            counter_opening_parentheses += 1
        elif x == ')':
            counter_opening_parentheses -= 1
        if counter_opening_parentheses < 0:
            raise Exception('Invalid syntax - closing parentheses is before an opening'
                            ' parentheses on token {}'.format(equation))

    if counter_opening_parentheses != 0:
        raise Exception('Invalid syntax - number of opening and closing'
                        ' parentheses is not the same on token {}'.format(equation))

    # check if there are two operators in a row
    for x in range(len(equation) - 1):

        # go over equation and check if there are two binary operators in a row
        # only exceptions when there is a unary operator in front of a binary operator
        # or when there is a closing parentheses in front of a binary operator
        # or if there is a minus sign in front of a binary operator (- as in sign change not subtraction)
        if equation[x] in binary_operators and \
                equation[x + 1] in binary_operators and equation[x + 1] != '-':
            raise Exception('Invalid syntax - two operators in a row on token {}'.format(equation))
    return equation


# simple function that checks if a string is a number
def is_number(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False


# function that gets an equation and
# gets rid of extra parentheses in the equation
def get_rid_of_extra_parentheses(equation: str) -> str:
    # go over equation and get rid of extra parentheses
    equation = equation.replace('()', '')

    # return the equation with no extra parentheses
    return equation


# function that gets rid of extra minus signs
# TODO: implement this function
def get_rid_of_extra_minus_signs(equation: str) -> str:
    # go over equation and get rid of extra minus signs
    # this is done by replacing -- with +
    equation = equation.replace('--', '+')
    return equation


# function that gets rid of extra white spaces
# TODO: implement this function
def get_rid_of_extra_white_spaces(equation: str) -> str:
    # # Removing any unwanted white spaces, tabs, or new lines from the equation string:
    #     equation = re.sub(r"[\n\t\s]*", "", equation)
    #     # Creating a list based on the equation string:
    #     result_list = re.split(r'([-+*/^~%!@$&()])|\s+', equation)
    #     # Filtering the list - Removing all the unwanted "spaces" from the list:
    #     result_list = [value for value in result_list if value not in ['', ' ', '\t']]

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


# function that simplifies the equation
def simplify_equation(equation: str) -> str:
    # get rid of extra parentheses
    equation = get_rid_of_extra_parentheses(equation)

    # get rid of extra minus signs
    equation = get_rid_of_extra_minus_signs(equation)

    # get rid of extra white spaces
    equation = get_rid_of_extra_white_spaces(equation)

    # return the simplified equation
    return equation


# general function that calculates the equation
# TODO: implement this function
def calculate_equation(equation: str, binary_operators: set,
                       unary_operators: set, priority: dict) -> str:

    # do the math functions based on the priority the highest priority first
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
    #             # by getting the last number on the left side and first number on the right side
    #             # this is done by going over the left and right side of the operator
    #             # and getting the last and first number
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
    #             # by replacing the left and right side of the operator with the result
    #             equation = equation.replace(left_side_number + equation[y] + right_side_number,
    #                                         str(binary_operators[x][equation[y]](left_side_number,
    #                                                                              right_side_number)))
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
    #             # by getting the last number on the left side and first number on the right side
    #             # this is done by going over the left and right side of the operator
    #             # and getting the last and first number
    #             left_side_number = ''
    #             right_side_number = ''
    #             for z in range(len(left_side) - 1, -1, -1):
    #                 if is_number(left_side[z]):
    #                     left_side_number = left_side[z] + left_side_number
    #                 else:
    #                     break

    return equation
