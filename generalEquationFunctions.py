# This is a file that contains general functions for the equation
# Path: qualityOfLifeFunctions.py
# Author: @Eldar Aslanbeily


# check if equation is valid
def check_if_function_is_valid(equation, operators, operands):

    # check if equation only contains operators and operands
    for x in equation:
        if x not in operators and x not in operands:
            raise Exception('Invalid token: {}'.format(x))

    # check if equation is balanced
    # meaning that there are the same number of opening and closing parentheses
    if equation.count('(') != equation.count(')'):
        raise Exception('Invalid syntax on token {}'.format(equation))

    # check if the order of parentheses is correct in the equation
    if equation.find(')') < equation.find('('):
        raise Exception('Invalid syntax on token {}'.format(equation))


# function that gets rid of extra parentheses
def get_rid_of_extra_parentheses(equation):
    # go over equation and get rid of extra parentheses
    while equation.find('()') != -1:
        equation = equation.replace('()', '')


# # Removing any unwanted white spaces, tabs, or new lines from the equation string:
#     equation = re.sub(r"[\n\t\s]*", "", equation)
#     # Creating a list based on the equation string:
#     result_list = re.split(r'([-+*/^~%!@$&()])|\s+', equation)
#     # Filtering the list - Removing all the unwanted "spaces" from the list:
#     result_list = [value for value in result_list if value not in ['', ' ', '\t']]

# s = "((8   1 *     6) /  42  + (3-1))"
s= "5     + 4  3    24"
r = [""]

for i in s.replace(" ", ""):
    if i.isdigit() and r[-1].isdigit():
        r[-1] = r[-1] + i
    else:
        r.append(i)

print(r[1:])
print(type(str(r[1:])))
