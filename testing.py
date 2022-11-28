# this is a testing file that contains all the tests for the calculator
# tests that the calculator works for every possible input
# and for every possible mistake scenario or invalid input
# Path: testing.py
# Author: @Eldar Aslanbeily


# import all from the functions file for testing
from functions import *


# import pytest to test the code
import pytest


def test_syntax_errors():
    """
    checks that all the syntax errors are caught
    and that the program exits
    """
    with pytest.raises(SystemExit) as e:
        calculate("2^*3")
        calculate("2-+3")
        calculate("2+3-")
        calculate("2+*3")
        calculate("2+/3")
        calculate("!2+3/")
        calculate("~2~3!")
    assert e.type == SystemExit


def test_garbage_input():
    """
    checks that the program exits when the input is wrong
    """
    with pytest.raises(SystemExit) as e:
        calculate("omega is not the best")
        calculate("calculator is easy")
        calculate("calculator is not working")
    assert e.type == SystemExit


def test_empty_white_space_input():
    """
    checks that the program exits when the input is empty
    or contains extra white spaces with nothing else
    """
    with pytest.raises(SystemExit) as e:
        calculate("")
        calculate(" ")
        calculate("\t")
        calculate("\n")
        calculate("\t   \t\t      \n\n    \n")
    # we check that the program exits with the correct error code
    # which is 0 - meaning that the program exited normally
    # and not with an error
    assert e.value.code == 0


def test_operator_valid():
    """
    checks that the program will return the correct result
    for all the possible operators
    """
    assert calculate("2+3") == "5"
    assert calculate("2-3") == "-1"
    assert calculate("2*3") == "6"
    assert calculate("2/3") == str(2/3)
    assert calculate("2^3") == "8"
    assert calculate("2%3") == "2"
    assert calculate("2$3") == "3"
    assert calculate("2&3") == "2"
    assert calculate("2@3") == str((2+3)/2)
    assert calculate("~3") == "-3"
    assert calculate("3!") == "6"


