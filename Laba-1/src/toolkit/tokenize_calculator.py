"""
Токенизация: разбивает строку на токены (числа и операторы).
"""

from toolkit.errors import (
    InvalidCharacterError,
    InvalidNumberError,
)

# Константы (PEP 8: заглавными буквами)
NUMBER = 'NUMBER'
OPERATOR = 'OPERATOR'

OPERATIONS = ['+', '-', '*', '/']

# Шаблоны некорректных чисел
ERROR_PATTERNS = ['+.', '*.', '-.', '.-', '.+', '.-']


def tokenize(text: str) -> list:
    """
    Разбивает входную строку на токены (числа и операторы).
    Выбрасывает исключения при обнаружении недопустимых символов или чисел.
    """
    tokens = []
    pos = 0

    while pos < len(text):
        place = text[pos]

        # Пропуск пробелов
        if place == ' ':
            pos += 1
            continue

        # Обработка чисел (включая унарные + и -)
        elif place.isdigit() or (
            place in '+-'
            and (not tokens or tokens[-1][0] == OPERATOR)
            and pos + 1 < len(text)
            and (text[pos + 1].isdigit() or text[pos + 1] == '.')
        ):
            start = pos
            float_count = 0

            if place in '+-':
                pos += 1

            while pos < len(text) and (text[pos].isdigit() or text[pos] == '.'):
                if text[pos] == '.':
                    float_count += 1
                    if float_count > 1:
                        raise InvalidNumberError(
                            f'Ошибка в выражении: {text[start:pos + 1]}'
                        )
                pos += 1

            num_str = text[start:pos]
            if num_str in ERROR_PATTERNS:
                raise InvalidNumberError(f'Ошибка в выражении: {num_str}')

            tokens.append([NUMBER, num_str, start])

        # Обработка операторов
        elif place in OPERATIONS:
            tokens.append([OPERATOR, place, pos])
            pos += 1

        # Обработка недопустимых символов
        else:
            raise InvalidCharacterError(f'Недопустимый символ: {place}')

    return tokens