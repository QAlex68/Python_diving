import doctest


def load_tests(loader, tests, ignore):
    """Загружает тесты из документации."""
    tests.addTests(doctest.DocTestSuite(Rectangle))
    return tests


class NegativeValueError(Exception):
    """Исключение для отрицательных значений."""


def __init__(self, value):
    super().__init__(f"Значение должно быть положительным, а не {value}")


class Rectangle:
    def __init__(self, width, height=None):
        if width <= 0:
            raise NegativeValueError(width)
        self.width = width
        if height is None:
            self.height = width
        elif height <= 0:
            raise NegativeValueError(height)
        else:
            self.height = height

    def perimeter(self):
        return float(2 * (self.width + self.height))

    def area(self):
        """Возвращает площадь прямоугольника."""
        return float(self.width * self.height)

    def __add__(self, other):
        """Операция сложения двух прямоугольников.
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r3 = r1 + r2
        >>> r3.width
        8.0
        >>> r3.height
        6.0
        """
        return Rectangle(float(self.width + other.width), float(self.height + other.height))

    def __sub__(self, other):
        """Операция вычитания двух прямоугольников.
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r3 = r1 - r2
        >>> r3.width
        2.0
        >>> r3.height
        2.0
        """
        return Rectangle(float(self.width - other.width), float(self.height - other.height))
