from typing import Annotated

import typer

from toolkit.calculator import calculate
from toolkit.converter import convert

app = typer.Typer(
    name='toolkit',
    help='Консольный набор утилит: калькулятор и конвертер величин.',
    no_args_is_help=True
)


@app.command(
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
def calc(
    expression: Annotated[
        list[str],
        typer.Argument(help='Арифметическое выражение.'),
    ],
) -> None:
    """Вычислить арифметическое выражение."""
    expr = ' '.join(expression)
    typer.echo(calculate(expr))


@app.command(
    name='convert',
    context_settings={
        'ignore_unknown_options': True,
        'allow_extra_args': True,
    },
)
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
    typer.echo(convert(value, unit_from, unit_to))


def main() -> None:
    """Точка входа CLI."""
    app()


if __name__ == '__main__':
    main()