import warnings

warnings.filterwarnings('ignore')

import pytest


class NegativeValueError(ValueError):
    pass


class Rectangle:
    def __init__(self, width, height=None):
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = (perimeter / 2) - width
        return Rectangle(width, height)

    def __sub__(self, other):
        width = abs(self._width - other._width)
        perimeter = abs(self.perimeter() - other.perimeter())
        height = (perimeter / 2) - width
        if width <= 0 or height <= 0:
            raise NegativeValueError('Результат вычитания должен быть положительным')
        return Rectangle(width, height)


class TestRectangle:
    def test_width(self):
        rect = Rectangle(5)
        assert rect.width == 5

    def test_height(self):
        rect = Rectangle(3, 4)
        assert rect.height == 4

    def test_perimeter(self):
        rect = Rectangle(5)
        assert rect.perimeter() == 20

    def test_area(self):
        rect = Rectangle(3, 4)
        assert rect.area() == 12

    def test_addition(self):
        rect1 = Rectangle(5, 1)
        rect2 = Rectangle(3, 4)
        rect3 = rect1 + rect2
        assert rect3.width == 8
        assert rect3.height == 6.0

    def test_negative_width(self):
        with pytest.raises(NegativeValueError):
            Rectangle(-5)

    def test_negative_height(self):
        with pytest.raises(NegativeValueError):
            Rectangle(5, -4)

    def test_set_width(self):
        rect = Rectangle(5)
        rect.width = 10
        assert rect.width == 10

    def test_set_negative_width(self):
        rect = Rectangle(5)
        with pytest.raises(NegativeValueError):
            rect.width = -10

    def test_set_height(self):
        rect = Rectangle(3, 4)
        rect.height = 6
        assert rect.height == 6

    def test_set_negative_height(self):
        rect = Rectangle(3, 4)
        with pytest.raises(NegativeValueError):
            rect.height = -6

    def test_subtraction(self):
        rect1 = Rectangle(10, 1)
        rect2 = Rectangle(3, 4)
        rect3 = rect1 - rect2
        assert rect3.width == 7
        assert rect3.height == 2.0

    def test_subtraction_negative_result(self):
        rect1 = Rectangle(3, 4)
        rect2 = Rectangle(10, 1)
        with pytest.raises(NegativeValueError):
            rect1 - rect2

    def test_subtraction_same_perimeter(self):
        rect1 = Rectangle(5, 1)
        rect2 = Rectangle(4, 3)
        rect3 = rect1 - rect2
        assert rect3.width == 1
        assert rect3.height == 1.0


import os
import sys

# Текущее имя файла
current_filename = __file__

# Новое имя файла с добавлением "test_" в начале
new_filename = "test_506.py"
# + os.path.basename(current_filename))

# Откройте текущий файл для чтения
with open(current_filename, 'r') as source_file:
    source_code = source_file.read()
    source_file.close()

# Запишите код в новый файл
with open(new_filename, 'w') as new_file:
    new_file.write(source_code)
    new_file.close()

with open(new_filename, 'r') as new_file:
    file_contents = new_file.read()
    # Выводим содержимое файла на экран
    # print(file_contents)

# Открываем файл для записи
with open('pytest_output.txt', 'w') as file:
    # Перенаправляем stdout в файл
    sys.stdout = file

    # Запускаем pytest.main() с нужными параметрами
    pytest.main(["--no-header", '-q', "--durations=0", new_filename])

# Возвращаем stdout в исходное состояние
sys.stdout = sys.__stdout__
# Считываем содержимое файла
with open('pytest_output.txt', 'r') as file:
    lines = file.readlines()
    first_line = file.readline()
    first_five_lines = lines[:1]

# Выводим первые 5 строк
for line in first_five_lines:
    print(line)