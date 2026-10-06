"""
Валидация: проверяет список токенов на синтаксические ошибки.
"""

from toolkit.errors import (
    DivisionByZeroError,
    DoubleOperatorError,
    EmptyExpressionError,
    MissingOperandError,
)
from toolkit.tokenize_calculator import NUMBER, OPERATOR


def validate(tokens: list) -> list:
    """
    Проверяет список токенов на синтаксические ошибки.
    Выбрасывает исключения при обнаружении ошибок.
    """
    if not tokens:
        raise EmptyExpressionError('Пустое выражение')

    if tokens[-1][0] == OPERATOR:
        raise MissingOperandError(
            f'Выражение заканчивается оператором: {tokens[-1][1]}'
        )

    for i in range(len(tokens) - 1):
        # 1. Проверка деления на ноль
        if tokens[i][1] == '/':
            try:
                if float(tokens[i + 1][1]) == 0:
                    raise DivisionByZeroError('Нельзя делить на ноль')
            except ValueError:
                pass

        # 2. Два оператора подряд
        if tokens[i][0] == OPERATOR and tokens[i + 1][0] == OPERATOR:
            raise DoubleOperatorError(
                f'Два оператора подряд: {tokens[i][1], tokens[i + 1][1]}'
            )

        # 3. Два числа подряд
        elif (tokens[i][0] == tokens[i + 1][0]) and tokens[i][0] == NUMBER:
            raise MissingOperandError(
                f'Пропущен операнд между {tokens[i][1]} и {tokens[i + 1][1]}'
            )

    # 4. Оператор стоит первым
    if tokens[0][0] == OPERATOR:
        raise MissingOperandError(
            f'Оператор стоит первым: {tokens[0][1]}'
        )

    return tokens