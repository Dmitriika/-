from toolkit.errors import (
    ConverterIncompatibleUnitsError,
    ConverterUnknownUnitError,
    TemperatureBelowAbsoluteZeroError,
)

# ==========================================
# СПРАВОЧНИК ЕДИНИЦ ИЗМЕРЕНИЯ
# ==========================================
UNITS = {
    # Длина (база — метр)
    'mm': {'group': 'length', 'to_base': 0.001},
    'cm': {'group': 'length', 'to_base': 0.01},
    'm':  {'group': 'length', 'to_base': 1.0},
    'km': {'group': 'length', 'to_base': 1000.0},

    # Масса (база — грамм)
    'g':  {'group': 'mass', 'to_base': 1.0},
    'kg': {'group': 'mass', 'to_base': 1000.0},

    # Температура (обрабатывается отдельно)
    'c':  {'group': 'temperature'},
    'f':  {'group': 'temperature'},
    'k':  {'group': 'temperature'},
}


ABSOLUTE_ZERO = {
    'c': -273.15,
    'f': -459.67,
    'k': 0.0,
}


# ==========================================
# КОНВЕРТАЦИЯ
# ==========================================
def convert(value: float, unit_from: str, unit_to: str) -> float:
    """
    Конвертирует значение из одной единицы измерения в другую.

    Параметры:
        value:     число
        unit_from: исходная единица (например, 'cm')
        unit_to:   целевая единица (например, 'm')

    Возвращает:
        float — результат конвертации.

    Исключения:
        ConverterUnknownUnitError              — единица не найдена
        ConverterIncompatibleUnitsError        — единицы из разных групп
        TemperatureBelowAbsoluteZeroError      — температура ниже абсолютного нуля
    """
    unit_from = unit_from.lower()
    unit_to = unit_to.lower()

    # 1. Проверяем, что единицы известны
    if unit_from not in UNITS:
        raise ConverterUnknownUnitError(f'Неизвестная единица: {unit_from}')
    if unit_to not in UNITS:
        raise ConverterUnknownUnitError(f'Неизвестная единица: {unit_to}')

    # 2. Приводим значение к float
    value = float(value)

    # 3. Получаем группы единиц
    group_from = UNITS[unit_from]['group']
    group_to = UNITS[unit_to]['group']

    # 4. Проверяем, что единицы из одной группы
    if group_from != group_to:
        raise ConverterIncompatibleUnitsError(
            f'Единицы относятся к разным группам: '
            f'{group_from}, {group_to}'
        )

    # 5. Линейная конвертация (длина, масса)
    if group_from == 'length' or group_from == 'mass':
        value_in_base = value * UNITS[unit_from]['to_base']
        return round(float(value_in_base / UNITS[unit_to]['to_base']),10)

    # 6. Конвертация температуры
    if group_from == 'temperature':
        if value < ABSOLUTE_ZERO[unit_from]:
            raise TemperatureBelowAbsoluteZeroError(
                f'Температура {value} {unit_from} '
                f'меньше абсолютного нуля'
            )

        if unit_to == unit_from:
            return float(value)

        if unit_from == 'c':
            if unit_to == 'f':
                value = value * 1.8 + 32
            else:
                value = value + 273.15

        elif unit_from == 'f':
            if unit_to == 'c':
                value = (value - 32) / 1.8
            else:
                value = (value + 459.67) / 1.8

        else:  # unit_from == 'k'
            if unit_to == 'c':
                value = value - 273.15
            elif unit_to == 'f':
                value = value * 1.8 - 459.67

    return round(float(value),10)
