# Первая лабораторная работа по Python
CLI-приложение на Python с калькулятором выражений и конвертером величин. 
Интерфейс командной строки реализован с помощью Typer.
## Установка 
- **Python 3.10+**.
- **Git** (для клонирования репозитория).

## Установка

Требуется Python 3.10+.

Все команды выполняются в **PowerShell**.

```bash
# Перейти в домашнюю папку
cd ~
```
```bash
# Клонировать репозиторий
git clone https://github.com/Dmitriika/Laba-1.git
```
```bash
#Перейти в сам репозиторий
cd Laba-1
```
```bash
#Установка пакета
python -m pip install -e .
```

## Команды
Справка CLI интерфейса
``` bash
python -m toolkit --help
```
Калькулятор. Считает выражение внутри "EXPRESSION".
Поддерживаются операторы +, -, *, /, скобки и унарные +, -.
``` bash
python -m toolkit calc "EXPRESSION"
```
Конвертер. Переводит числовое значение VALUE одной величины в другую.
Поддерживаемые единицы:

длина: mm, cm, m, km;

масса: g, kg;

температура: c, f, k.
```bash
python -m toolkit convert VALUE --from UNIT --to UNIT
```

## Принятые решения

### Калькулятор

- Внутри `tokenize_calculator.py` происходит токенизация строки.
- Внутри `validate_calculator.py` происходит проверка синтаксиса токенов.
- Внутри `calculator.py`:
  - `to_rpn` — преобразование в обратную польскую нотацию (алгоритм сортировочной станции Дейкстры);
  - `evaluate_rpn` — вычисление итогового результата.
- Внутри `errors.py` описаны исключения: `EmptyExpressionError`, `InvalidCharacterError`, `MissingOperandError`, `DoubleOperatorError`, `DivisionByZeroError`, `InvalidNumberError`.
- `__main__.py` — точка входа CLI на Typer: команды `calc`, `convert`, `--help`.

### Конвертер

- Внутри `converter.py` описана система величин: `UNITS` (группа и коэффициент перевода к базовой единице).
- Для длины и массы:

  ```
  value * UNITS[from_unit]['to_base'] / UNITS[to_unit]['to_base']
  ```

- Для температуры значение сначала переводится в Кельвины, затем — в целевую единицу.
- Проверки: неизвестная единица, несовместимые группы, температура ниже абсолютного нуля.
- Результат возвращается как `float`, округлённый до 10 знаков.
- Исключения конвертера: `ConverterUnknownUnitError`, `ConverterIncompatibleUnitsError`, `TemperatureBelowAbsoluteZeroError`.
