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
    checks that all the syntax errors are raised correctly
    when the input is invalid
    """
    assert pytest.raises(SyntaxError, calculate_equation, "2-+3")
    assert pytest.raises(SyntaxError, calculate_equation, "2^*3")
    assert pytest.raises(SyntaxError, calculate_equation, "2+3-")
    assert pytest.raises(SyntaxError, calculate_equation, "!2+3/")
    assert pytest.raises(SyntaxError, calculate_equation, "~2~3!")


def test_garbage_input():
    """
    checks that all the syntax errors are raised correctly
    when the input is gibberish
    """
    assert pytest.raises(SyntaxError, calculate_equation, "hello world")
    assert pytest.raises(SyntaxError, calculate_equation, "gibberish equation")
    assert pytest.raises(SyntaxError, calculate_equation, "this should not be possible")


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
    assert calculate_equation("2/3") == "0.6666666667"
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


def test_complicated_equations():
    """
    checks that the program will return the correct result
    for complicated equations
    """
    # this test function contains 20 very complicated equations, that
    # make use of all the operators and are at lest 20 characters long
    assert calculate_equation("(122+33*(   4^3! $ (9- 8@33 ) ) )& ( 9*  21! - 93218# )") == "135290.0"
    assert calculate_equation("(4! - (5.5^3)#)$ (1 231 23@6! )@(~5 43)") == "30689.25"
    assert calculate_equation("(~-23  4*5  43)#-(543  43^0.1)@69 420$(133 7)") == "-34693.4875938195"
    assert calculate_equation("((~(4^   3!$9-8 @33)  )&9*  21 #-   93218#)@42  069") == "-372162.25"
    assert calculate_equation("(420-69+1337)# -~((-2)^3)!$(2.5^2@3)  ----82366") == "42069.0"
    assert calculate_equation("731+~(31321)*2 *-321 --- (3!$89@321321$312^0.5)") == "20108412.1197186187"
    assert calculate_equation("(~-----(321312*32)%2^31)*76 -- (5---321 +(21)!)") == "51090942171709440000.0"
    assert calculate_equation("(24$3!)@   1.69+7!   *(0.01^2)#    /12*7  -(.1)") == "2952.745"
    assert calculate_equation("((~(4^   3!$9-8 @33)  )&9*  21 #-   93218#)@42  069") == "-372162.25"
    assert calculate_equation("--(54  3*0.69  )#/123--(9!-~3@  9$  2^  3) ---(365^(55-(32+23)))")  == "362852.2195121951"
    assert calculate_equation("((  (  123#)@6  7312  -381#-~-(5!))*0   .1+2^5@69420%2)")  == "3354.1142135624"
    assert calculate_equation("(8 *8 @  8%8#+8!  ^8/8+88)---   (77^0.77@ 77#-77* 7.7)")  == "873120530892689293402981834661298176.0"
    assert calculate_equation("(  324%3-  (31^2-19!%89-432+3@1)  *0.69420+  (5^435@1) )  ^0.00069420")  == "1.2757895631"
    assert calculate_equation("(1!  -2@3#   +4$- 5%6^ 7&8* 9) -- 10- ~(11!*-12) ") == "-478854135.5"
    assert calculate_equation("5318008 +(69 -42*10 )/1&7 ^5%42 @9%2  - (9-0 9090 909. 9 )^1") == "14408557.9000000004"
    assert calculate_equation("(458%34)-((65-(9!)^0.2)*7%2#-9/7^5)-------(2@2%2$2*2^2)") == "-36.0589183394"
    assert calculate_equation("54&2--(542*7^4%34#*2!$2-0.98/76%43)----- -- - (897-(4!)^0.69)") == "2603574.0095242294"
    assert calculate_equation("((--(-1-  (-2%6  ^7&6)- -0.89)+3  #/2)--1) @1@1@1@2--8$7") ==  "-246.413125"
    assert calculate_equation("1!+2!   -33#+4  4$55&77  ^0-88*9  9--~(1  @2@3#-4%3)^2") ==  "-8712.4375"
