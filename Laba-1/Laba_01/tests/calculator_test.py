import pytest
from toolkit.calculator import calculate
from toolkit.errors import (
    DivisionByZeroError,
    DoubleOperatorError,
    EmptyExpressionError,
    InvalidCharacterError,
    InvalidNumberError,
    MissingOperandError,
)

CORRECT_TESTS = [
    ('10 + 5', 15.0),
    ('10 - 5', 5.0),
    ('10 * 5', 50.0),
    ('10 / 5', 2.0),
    ('2 + 3 * 4', 14.0),      # приоритет * над +
    ('10 - 2 - 3', 5.0),      # левая ассоциативность
    ('+5 + -3', 2.0),         # унарные знаки
    ('  10  +  5  ', 15.0),   # пробелы
]

INCORRECT_TESTS = [
    ('', EmptyExpressionError),           # пустое выражение
    ('10 + @', InvalidCharacterError),    # недопустимый символ
    ('10 +', MissingOperandError),        # пропущен операнд
    ('10 + * 5', DoubleOperatorError),    # два оператора подряд
    ('10 / 0', DivisionByZeroError),      # деление на ноль
    ('10.5.5 + 2', InvalidNumberError),   # неверное число
]


@pytest.mark.parametrize('test_input, expected', CORRECT_TESTS)
def test_correct(test_input, expected):
    """Корректные выражения возвращают ожидаемый результат."""
    assert calculate(test_input) == expected


@pytest.mark.parametrize('test_input, error_class', INCORRECT_TESTS)
def test_incorrect(test_input, error_class):
    """Ошибочные выражения выбрасывают нужное исключение."""
    with pytest.raises(error_class):
        calculate(test_input)