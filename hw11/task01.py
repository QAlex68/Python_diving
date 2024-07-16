# напиши на языке Python:
# Создайте класс MyStr, который наследуется от встроенного класса str и добавлять дополнительную информацию о
# создателе строки и времени ее создания. Этот класс будет представлять строки с информацией о событиях.
# Класс MyStr должен иметь следующие атрибуты и методы:
# value (str): Строковое значение с описанием события.
# author (str): Имя автора, создавшего запись.
# time: Время создания записи в формате '%Y-%m-%d %H:%M'.
# Магические методы (Dunder-методы):
# Реализуйте метод __new__(cls, value, author), который создает новый объект класса MyStr с заданным value и author.
# Метод также автоматически фиксирует время создания записи.
# В этом методе создается новый объект MyStr с указанными атрибутами и текущим временем в атрибуте time.
# Реализуйте метод __str__(self), который возвращает строковое представление объекта класса MyStr с информацией
# о событии, авторе и времени создания.
# Реализуйте метод __repr__(self), который возвращает строковое представление объекта класса MyStr.
# Метод __repr__ возвращает строку, которая может быть использована для создания точно такого же объекта MyStrс теми же
# значениями value и author`.
# Пример использования.
# На входе:
# event = MyStr("Завершилось тестирование", "John")
# print(event)
# На выходе:
# Завершилось тестирование (Автор: John, Время создания: [ в формате '%Y-%m-%d %H:%M'])
# На входе:
# my_string = MyStr("Пример текста", "Иван")
# print(my_string)
# На выходе:
# Пример текста (Автор: Иван, Время создания: 2023-10-10 15:56)
# На входе:
# my_string = MyStr("Мама мыла раму", "Маршак")
# print(repr(my_string))
# На выходе:
# MyStr('Мама мыла раму', 'Маршак')


import datetime


class MyStr(str):

    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        return instance

    def __init__(self, value, author):
        self.value = value
        self.author = author

    def __str__(self):
        """Информация для юзера"""
        return f'{self.value} (Автор: {self.author}, Время создания: {self.time})'

    def __repr__(self):
        """Информация для разработчика"""
        return f"MyStr('{self.value}', '{self.author}')"


event = MyStr("Завершилось тестирование", "John")
print(event)
print(repr(event))

# print('Начало программы')
# a = MyStr('hello', 'Pupkin')
# b = MyStr('bay', 'Pivkin')
# c = MyStr('goodBay', 'Klein')
# d = MyStr('bu bu bu', 'people')
# e = a
# print(a, b, c, d, e)
# print(a.author, b.time, c, d, e)
# print(issubclass(MyStr, str))
# print(issubclass(str, MyStr))
# print(isinstance(str(), MyStr))
# print(isinstance(a, str))
