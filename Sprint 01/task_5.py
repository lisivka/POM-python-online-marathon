# TODO: task_5
"""
Convert a certain expression like 2+3 to expression in a postfix notation.
The given expression can have one of the following tokens:

a number;
a parenthesis;
arithmetic operator:
subtraction (-);
addition (+);
multiplication (*);
devision (/);
modulo operation (%).
Example:

For expression = ["2","+","3"] the output should be ["2","3","+"].
[execution time limit] 4 seconds (py)
[input] array.string expression
An array of tokes of a valid expression in the standard notation.
[output] array.string
Tokens of the expression in the postfix notation.
"""

# https://www.collegenote.net/curriculum/data-structures-and-algorithms/36/181/
# https://www.techiedelight.com/ru/convert-infix-to-postfix-expression/

def toPostFixExpression(e):

    result = [each for each in e if each.isdigit()] + [each for each in e if each in ["/","*","+","-"]]

    return result

e=(["(","(","(","1","+","2",")","*","3",")","+","6",")","/","(","2","+","3",")"])
answr = ['1', '2', '+', '3', '*', '6', '+', '2', '3', '+', '/']
print(toPostFixExpression(e))