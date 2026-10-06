"""
Исключения для калькулятора и конвертера.
"""


# ==========================================
# КАЛЬКУЛЯТОР
# ==========================================
class CalculatorError(Exception):
    """Базовый класс для всех ошибок калькулятора."""


class EmptyExpressionError(CalculatorError):
    """Выбрасывается, когда выражение пустое или состоит только из пробелов."""


class InvalidCharacterError(CalculatorError):
    """
    Выбрасывается, когда встречается символ, не являющийся
    числом, оператором или пробелом.
    """


class MissingOperandError(CalculatorError):
    """Выбрасывается, когда пропущен операнд."""


class DoubleOperatorError(CalculatorError):
    """Выбрасывается, когда два оператора идут подряд."""


class DivisionByZeroError(CalculatorError):
    """Выбрасывается при попытке деления на ноль."""


class UnknownUnitError(CalculatorError):
    """
    Выбрасывается, когда в выражении встречается неизвестная
    единица измерения (для калькулятора с поддержкой единиц).
    """


class IncompatibleUnitsError(CalculatorError):
    """
    Выбрасывается, когда складываются или вычитаются единицы
    разных групп (например, длина и масса).
    """


class InvalidNumberError(CalculatorError):
    """Выбрасывается при неверном числовом формате."""


# ==========================================
# КОНВЕРТЕР
# ==========================================
class ConverterError(Exception):
    """Базовый класс для всех ошибок конвертера."""


class ConverterUnknownUnitError(ConverterError):
    """Выбрасывается, когда единица измерения не найдена в справочнике."""


class ConverterIncompatibleUnitsError(ConverterError):
    """Выбрасывается, когда единицы относятся к разным группам."""


class TemperatureBelowAbsoluteZeroError(ConverterError):
    """Выбрасывается, когда температура ниже абсолютного нуля."""