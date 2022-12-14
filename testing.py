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
    # we check that the program exits with the correct error code
    # which is 1 - meaning that the program exited with an error
    # because the input was wrong
    assert e.value.code == 1


def test_garbage_input():
    """
    checks that the program exits when the input is wrong
    """
    with pytest.raises(SystemExit) as e:
        calculate("omega is not the best")
        calculate("calculator is easy")
        calculate("calculator is not working")
    # we check that the program exits with the correct error code
    # which is 1 - meaning that the program exited with an error
    # because the input was wrong
    assert e.value.code == 1


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
    assert calculate_equation("2+3") == "5"
    assert calculate_equation("2-3") == "-1"
    assert calculate_equation("2*3") == "6"
    assert calculate_equation("2/3") == str(2/3)
    assert calculate_equation("2^3") == "8"
    assert calculate_equation("2%3") == "2"
    assert calculate_equation("2$3") == "3"
    assert calculate_equation("2&3") == "2"
    assert calculate_equation("2@3") == str((2+3)/2)
    assert calculate_equation("~3") == "-3"
    assert calculate_equation("3!") == "6"
    assert calculate_equation("3!!") == "720"
    assert calculate_equation("99#") == "18"
    assert calculate_equation("99##") == "9"
    # assert calculate_equation("2^(3-2)") == "2"
    # assert calculate_equation("~5+5!") == "115.0"
    # assert calculate_equation("2^3!") == "64"
    # assert calculate_equation("~(~5)*(5)!") == "600.0"


def test_complicated_equations():
    """
    checks that the program will return the correct result
    for complicated equations
    """
    # this test function contains 20 very complicated equations, that
    # make use of all the operators and are at lest 20 characters long
    assert calculate_equation("(122+33*(   4^3! $ (9- 8@33 ) ) )& ( 9*  21! - 93218# )") == "135290.0"
    assert calculate_equation("(4! - (5.5^3)#)$ (123123@6!)@(~543)") == "30689"
    assert calculate_equation("(~-23  4*5  43)#-(543  43^0.1)@69 420$(133 7)") == "-34693.4875938195"
    assert calculate_equation("((~(4^   3!$9-8 @33)  )&9*  21 #-   93218#)@42  069") == "-372162"
    assert calculate_equation("(420-69+1337)# -~((-2)^3)!$(2.5^2@3)  ----82366") == "42069.0"
    assert calculate_equation("731+~(31321)*2 *-321 --- (3!$89@321321$312^0.5)") == "20108412.11971862"
    assert calculate_equation("(~-----(321312*32)%2^31)*76 -- (5---321 +(21)!)") == "5.109094217170944"
    assert calculate_equation("(24$3!)@   1.69+7!   *(0.01^2)#    /12*7  -(.1)") == "2952.745"
    # TODO: add more complicated equations and test them here


