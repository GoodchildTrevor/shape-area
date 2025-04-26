from typing import Any, Sequence
from .figures import Circle, Triangle
from .base import Figure


def shape_factory(*args: Any) -> Figure:
    """
    Фабрика для вычисления площади геометрических фигур.
    Принимает параметры в виде одного числа/строки для круга,
    либо трёх чисел/строк или последовательности из трёх чисел/строк для треугольника.
    Parameters:
        args (Any): Один аргумент или три аргумента, либо список/кортеж из трёх значений.
    Returns:
        Shape: Объект фигуры (Circle или Triangle)
    Raises:
        ValueError: Если переданы неподходящие аргументы.
    """
    # Если три отдельных аргумента — это всегда треугольник
    if len(args) == 3:
        return Triangle(*args)

    # Если ровно один аргумент — решаем по типу
    if len(args) == 1:
        single = args[0]
        # простой тип → круг
        if isinstance(single, (int, float, str)):
            return Circle(single)
        # последовательность длины 3 → треугольник
        if isinstance(single, Sequence) and not isinstance(single, (str, bytes)) and len(single) == 3:
            return Triangle(*single)

    # всё остальное — ошибка
    raise ValueError(
        f"Ожидается либо три числа: Triangle(a,b,c), "
        f"либо одно число/строка для круга, либо одну последовательность из трёх чисел, "
        f"а получено: {args!r}"
    )
