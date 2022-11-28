# this is a testing file that contains all the tests for the calculator
# tests that the calculator works for every possible input
# and for every possible mistake scenario or invalid input
# Path: testing.py
# Author: @Eldar Aslanbeily


# import all from the functions file for testing
from functions import *

# import all the config for testing purposes
from globals import *

# import pytest to test the code
import pytest


def test_operators():
    """
    tests that the operators are valid and working
    for every possible input
    :return:
    """
    assert calculate_equation("3!*((2^6)$7!)", BINARY_OPERATORS, UNARY_OPERATORS,
                              PRIORITY, OPERANDS, OPERATORS, RIGHT_ASSOCIATIVE_UNARY_OPERATORS,
                              LEFT_ASSOCIATIVE_UNARY_OPERATORS) == "30240"


def test_exit():
    """
    checks that all the exit commands work
    and all the validity checks work
    :return:
    """
    with pytest.raises(SystemExit) as e:
        check_if_function_is_valid("5 5+6", OPERATORS, OPERANDS, BINARY_OPERATORS,
                                          UNARY_OPERATORS, RIGHT_ASSOCIATIVE_UNARY_OPERATORS,
                                          LEFT_ASSOCIATIVE_UNARY_OPERATORS)
    assert e.value.code == 1
    # assert e.type == SystemExit
