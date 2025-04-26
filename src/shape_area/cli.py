"""Консольный скрипт для работы с библиотекой shape_area."""

import typer
from rich.console import Console
from shape_area.factory import shape_factory

app = typer.Typer(invoke_without_command=True)
console = Console()


@app.callback(invoke_without_command=True)
def main(values: list[float] = typer.Argument(...)):
    """
    Вычисляет площадь фигуры.

    Args:
        values (float): Параметры фигуры через пробел.
    """
    try:
        shape = shape_factory(values)
        console.print(f"Площадь фигуры: {shape.area():.4f}")
        # Дополнительная информация про треугольник
        if hasattr(shape, "is_right"):
            if shape.is_right():
                console.print("[green]Этот треугольник является прямоугольным.[/green]")
            else:
                console.print("[yellow]Этот треугольник не является прямоугольным.[/yellow]")

    except Exception as e:
        console.print(f"[red]Ошибка:[/red] {e}")
        raise typer.Exit(1)

if __name__ == "__main__":
    app()
