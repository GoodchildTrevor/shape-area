from decimal import Decimal, getcontext, InvalidOperation
from .base import Figure
from math import pi

# Настройка точности Decimal
getcontext().prec = 28
# Задаём число Пи
PI = Decimal.from_float(pi)


class Circle(Figure):
    """
    Класс для определения круга и вычисления его площади.
    """

    def __init__(self, radius: float | str | Decimal):
        """
        Инициализация объекта круга.

        Parameters:
            radius (float | str | Decimal): Радиус круга.
                Должен быть положительным числом или строкой, представляющей число.

        Raises:
            ValueError: При некорректном формате или отрицательном значении.
        """
        try:
            self.radius = Decimal(radius)
        except InvalidOperation:
            raise ValueError(f"Невозможно интерпретировать радиус: {radius!r} — ожидается число.")

        if self.radius <= 0:
            raise ValueError(f"Радиус должен быть положительным числом, а не {self.radius}.")

    def area(self) -> Decimal:
        """
        Вычисляет площадь круга по формуле π * r².

        Returns:
            Decimal: Площадь круга в квадратных единицах.
        """
        return PI * self.radius ** 2


class Triangle(Figure):
    """
    Класс для треугольника.
    """

    def __init__(self, a: float | str | Decimal, b: float | str | Decimal, c: float | str | Decimal):
        """
        Инициализация объекта треугольника.

        Parameters:
            a, b, c (float | str | Decimal): Стороны треугольника.

        Raises:
            ValueError: При некорректных значениях сторон или невозможности построения треугольника.
        """
        try:
            self.a = Decimal(a)
            self.b = Decimal(b)
            self.c = Decimal(c)
        except InvalidOperation:
            raise ValueError(f"Одна или несколько сторон некорректны: {a!r}, {b!r}, {c!r}")

        if any(side <= 0 for side in (self.a, self.b, self.c)):
            raise ValueError("Все стороны должны быть положительными числами.")

        if not self._is_valid_triangle():
            raise ValueError("Стороны не образуют корректный треугольник.")

    def _is_valid_triangle(self) -> bool:
        """
        Проверяет возможность существования треугольника.

        Returns:
            bool: True, если треугольник может существовать, иначе False.
        """
        return (self.a + self.b > self.c and
                self.a + self.c > self.b and
                self.b + self.c > self.a)

    def area(self) -> Decimal:
        """
        Вычисляет площадь треугольника по формуле Герона.

        Returns:
            Decimal: Площадь треугольника в квадратных единицах.
        """
        p = (self.a + self.b + self.c) / 2
        area_squared = p * (p - self.a) * (p - self.b) * (p - self.c)
        return area_squared.sqrt()

    def is_right(self) -> bool:
        """
        Проверяет, является ли треугольник прямоугольным.

        Сравнивает квадрат самой длинной стороны с суммой квадратов двух других,
        используя теорему Пифагора: c² = a² + b².

        Returns:
            bool: True, если треугольник прямоугольный, иначе False.
        """
        sides = sorted([self.a, self.b, self.c])
        return sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2


class Quadrilateral(Figure):
    pass
