import pytest

from toolkit.converter import convert
from toolkit.errors import (
    ConverterIncompatibleUnitsError,
    ConverterUnknownUnitError,
    TemperatureBelowAbsoluteZeroError,
)

CORRECT_TESTS = [
    # Длина
    (100, 'cm', 'm', 1.0),
    (1, 'km', 'm', 1000.0),
    (5000, 'mm', 'm', 5.0),
    # Масса
    (1000, 'g', 'kg', 1.0),
    (2.5, 'kg', 'g', 2500.0),
    # Температура
    (0, 'c', 'f', 32.0),
    (100, 'c', 'f', 212.0),
    (0, 'c', 'k', 273.15),
    (300, 'k', 'c', 26.85),
    (32, 'f', 'c', 0.0),
    # Регистр не учитывается
    (100, 'CM', 'M', 1.0),
]

INCORRECT_TESTS = [
    # Неизвестная единица
    (100, 'xyz', 'm', ConverterUnknownUnitError),
    (100, 'm', 'xyz', ConverterUnknownUnitError),
    # Несовместимые группы
    (100, 'cm', 'kg', ConverterIncompatibleUnitsError),
    (100, 'm', 'c', ConverterIncompatibleUnitsError),
    (100, 'kg', 'c', ConverterIncompatibleUnitsError),
    # Ниже абсолютного нуля
    (-300, 'c', 'k', TemperatureBelowAbsoluteZeroError),
    (-10, 'k', 'c', TemperatureBelowAbsoluteZeroError),
]


@pytest.mark.parametrize('value, unit_from, unit_to, expected', CORRECT_TESTS)
def test_correct(value, unit_from, unit_to, expected):
    """Корректная конвертация возвращает ожидаемый результат."""
    assert convert(value, unit_from, unit_to) == expected


@pytest.mark.parametrize(
    'value, unit_from, unit_to, error_class',
    INCORRECT_TESTS,
)
def test_incorrect(value, unit_from, unit_to, error_class):
    """Некорректная конвертация выбрасывает нужное исключение."""
    with pytest.raises(error_class):
        convert(value, unit_from, unit_to)