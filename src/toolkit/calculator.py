"""
Калькулятор: преобразование в ОПН и вычисление.
"""

from toolkit.errors import (
    DivisionByZeroError,
    MissingOperandError,
)
from toolkit.tokenize_calculator import NUMBER, OPERATOR, tokenize
from toolkit.validate_calculator import validate

PRIORITY = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
}

def to_rpn(tokens: list) -> list:
    """
    Преобразует инфиксную запись (список токенов) в ОПН.
    Алгоритм сортировочной станции Дейкстры.

    Возвращает список чисел (float) и операторов (str).
    """
    output = []  # выходная очередь
    stack = []   # стек операторов

    for token in tokens:
        if token[0] == NUMBER:
            output.append(float(token[1]))

        elif token[0] == OPERATOR:
            # Пока на вершине стека оператор с приоритетом >= текущего,
            # выталкиваем его в выход.
            while stack and PRIORITY[stack[-1]] >= PRIORITY[token[1]]:
                output.append(stack.pop())
            stack.append(token[1])

    # Выталкиваем всё, что осталось в стеке
    while stack:
        output.append(stack.pop())

    return output


def evaluate_rpn(rpn: list) -> float:
    """
    Вычисляет значение по обратной польской нотации.
    Возвращает float.
    """
    stack = []

    for item in rpn:
        if isinstance(item, float):
            stack.append(item)
        else:
            if len(stack) < 2:
                raise MissingOperandError('Недостаточно операндов')

            right = stack.pop()   # правый операнд (верх стека)
            left = stack.pop()    # левый операнд

            if item == '+':
                stack.append(left + right)
            elif item == '-':
                stack.append(left - right)
            elif item == '*':
                stack.append(left * right)
            elif item == '/':
                if right == 0:
                    raise DivisionByZeroError('Нельзя делить на ноль')
                stack.append(left / right)

    if len(stack) != 1:
        raise MissingOperandError('Неверное выражение')

    return stack[0]


def calculate(expression: str) -> float:
    """
    Полный цикл: tokenize → validate → to_rpn → evaluate_rpn.
    Принимает строку, возвращает float.
    """
    tokens = tokenize(expression)
    validate(tokens)
    rpn = to_rpn(tokens)
    return evaluate_rpn(rpn)