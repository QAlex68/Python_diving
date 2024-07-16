# Задание №3 вариант 1
# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом
# step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.

from collections import deque
import json


class Factorial:

    def __init__(self, *args) -> None:
        self.start = 1
        self.stop = 1
        self.step = 1

        match args:
            case (stop,):
                self.stop = stop
            case (start, stop):
                self.start = start
                self.stop = stop
            case (start, stop, step):
                self.start = start
                self.stop = stop
                self.step = step
            case _:
                raise ValueError("Too many parameters\n")

    def __iter__(self):
        return self

    def __next__(self):
        while self.start <= self.stop:
            result = 1
            for mult in range(1, self.start + 1):
                result *= mult
            temp = self.start
            self.start += self.step
            return {temp: result}
        raise StopIteration


if __name__ == '__main__':
    f1 = Factorial(3, 6)
    for item in f1:
        print(item)