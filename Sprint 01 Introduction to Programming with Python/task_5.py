# TODO: task_5 +

"""
Convert a certain expression like 2+3 to expression in a postfix notation.
The given expression can have one of the following tokens:

a number;
a parenthesis;
arithmetic operator:
subtraction (-);
addition (+);
multiplication (*);
division (/);
modulo operation (%).
Example:

For expression = ["2","+","3"] the output should be ["2","3","+"].
[execution time limit] 4 seconds (py)
[input] array.string expression
An array of tokes of a valid expression in the standard notation.
[output] array. string
Tokens of the expression in the postfix notation.
"""


# https://www.collegenote.net/curriculum/data-structures-and-algorithms/36/181/
# https://www.techiedelight.com/ru/convert-infix-to-postfix-expression/
"""
Следующий алгоритм выводит строку в постфиксном порядке. Мы обрабатываем инфиксное выражение слева направо. Для каждого токена может возникнуть четыре случая:

Если текущий токен является открывающей скобкой, '(', поместите его в stack.
Если текущий токен является закрывающей скобкой, ')', извлекайте токены из stack до тех пор, пока не будет удалена соответствующая открывающая скобка '('. Добавляйте каждый оператор в конец постфиксного выражения.
Если текущий токен является операндом, добавьте его в конец постфиксного выражения.
Если текущий токен является оператором, поместите его на вершину stack. Прежде чем сделать это, сначала извлеките из stack до тех пор, пока у нас не будет оператора с более низким приоритетом наверху, или стек не станет пустым. Добавьте каждый оператор в конец постфиксного выражения.
Наконец, добавьте все оставшиеся операторы в stack в конце постфиксного выражения и верните постфиксное выражение.
"""


def toPostFixExpression(e: list):

    result = []
    stack = []
    rating = {"*": 1, "/": 1,
              "+": 2, "-": 2,
              "(": 5555
              }

    for token in e:

        # 1. Если текущий токен является открывающей скобкой, '(', поместите его в stack.
        if token == "(":
            stack.append("(")

            # print("token =", token, "stack=", stack, "result =", result, )
        # 2 Если текущий токен является закрывающей скобкой, ')', извлекайте токены из stack до тех пор,
        # пока не будет удалена соответствующая открывающая скобка '('.
        # Добавляйте каждый оператор в конец постфиксного выражения.
        elif token == ")":
            while stack[-1] != '(':
                result += stack.pop()
            stack.pop()

            # print("token =", token, "stack=", stack, "result =", result, )
        # 3 Если текущий токен является операндом, добавьте его в конец постфиксного выражения.
        elif token.isdigit() or token.isalpha():
            result.append(token)

            # print("token =", token, "stack=", stack, "result =", result, )
        # 4 Если текущий токен является оператором, поместите его на вершину stack.
        # Прежде чем сделать это, сначала извлеките из stack до тех пор,
        # пока у нас не будет оператора с более низким приоритетом наверху,
        # или стек не станет пустым.
        # Добавьте каждый оператор в конец постфиксного выражения.
        elif token in ["/", "*", "+", "-"]:
            # print("rating = ", rating[token], rating[stack[-1]])
            while stack and rating[token] >= rating[stack[-1]]:
                result += stack.pop()
            stack.append(token)
            # print("token =", token, "stack=", stack, "result =", result, )
        else:
            print(f"ERROR_TOKEN:  [{token}]")
    # Наконец, добавьте все оставшиеся операторы в stack в конце постфиксного выражения и верните постфиксное выражение.
    while stack:
        result += stack.pop()

    return result


e = ["(", "(", "(", "1", "+", "2", ")", "*", "3", ")", "+", "6", ")", "/", "(", "2", "+", "3", ")"]
answer = ['1', '2', '+', '3', '*', '6', '+', '2', '3', '+', '/']
e = ["A", "*", "(", "B", "*", "C", "+", "D", "*", "E", ")", "+", "F"]
answer = ['A', 'B', 'C', '*', 'D', 'E', '*', '+', '*', 'F', '+']

print(toPostFixExpression(e))
print(toPostFixExpression(e)==answer)
