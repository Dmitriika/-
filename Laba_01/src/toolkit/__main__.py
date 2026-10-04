import typer

from toolkit.calculator import calculate
from toolkit.converter import convert

app = typer.Typer(
    name='toolkit',
    help='Консольный набор утилит: калькулятор и конвертер величин.',
    no_args_is_help=True,
)
@app.command()
def calc(
    expression: str = typer.Argument(
        ...,
        help='Арифметическое выражение, например "2 + 3 * 4".',
    ),
) -> None:
    """Вычислить арифметическое выражение."""
    result = calculate(expression)
    typer.echo(result)

def convert_cmd(
    value: float = typer.Argument(..., help='Числовое значение.'),
    unit_from: str = typer.Option(
        ...,
        '--from',
        help='Исходная единица (mm, cm, m, km, g, kg, c, f, k).',
    ),
    unit_to: str = typer.Option(
        ...,
        '--to',
        help='Целевая единица.',
    ),
) -> None:
    """Конвертировать значение между единицами измерения."""
    result = convert(value, unit_from, unit_to)
    typer.echo(result)


# Регистрируем команду convert с нужным именем
app.command(name='convert')(convert_cmd)


def main() -> None:
    """Точка входа CLI."""
    app()


if __name__ == '__main__':
    main()

