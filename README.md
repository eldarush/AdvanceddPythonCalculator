# AdvanceddPythonCalculator
This is an advanced calculator repository for a project for omega
Author: @Eldar Aslanbeily (username on GitHub: eldarush)
Language: Python
Interpritor: Python-3.7

This calculator while run through the "main.py" file will
ask the user to input a function, then the program will calculate the 
result of the equation that the user inputted, this result can be saved and used again
for further equations as 'ans'.
both input and output of an equation are in str type.

This calculator has unique custom operators.
list of all operators:
  addition (a+b)
  subtraction (a-b)
  multiplication (a*b)
  division (a/b)
  power (a^b) a.k.a (a**b)
  modulo (a%b)
  maximum (a$b) - returns the maximunm between a and b
  minimum (a%b) - returns the minimum between a and b
  avarage (a@b) - returns the avarage between a and b
  tilde (~a) - returns the negative value of a
  factorial (a!)
  
priorotiy list for the operators: 
// higher proiroty mreans that its done first in the calculation.
// if two operators have the same prioroty the one that comes first will be calculated first.
  1:
    addition (a+b)
    subtraction (a-b)
  2:
    multiplication (a*b)
    division (a/b)
  3:
    power (a^b)
  4:
    modulo (a%b)
  5:
    maximum (a$b) 
    minimum (a%b) 
    avarage (a@b) 
  6:
    tilde (~a)
    factorial (a!)
  
This calculator only accepts digits (0-9) not variables (a-z) etc.
This calculator only accepts round parentheses (), not any other kind - [] {}.
