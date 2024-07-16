# Задание №1 Вариант2
# Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и их факториалов.
from collections import deque


class Factorial:

    def __init__(self, k: int = 1) -> None:
        self.memory = deque(maxlen=k)

    def __call__(self, num: int = 1):
        if num < 0:
            raise ValueError('Задано отрицательное значение!')
        else:
            result = 1
            for i in range(2, num + 1):
                result *= i
            self.memory.append({num: result})
        return result
        # return self.memory[-1]

    def get_memory(self):
        return self.memory


if __name__ == '__main__':
    f1 = Factorial(3)
    f1(3)
    f1(5)
    f1(2)
    f1(6)
    f1(4)
    f1(9)
    print(f1.get_memory())
    f2 = Factorial(10)
    f2(7)
    f2(8)
    f2(1)
    f2(2)
    f2(4)
    f2(9)
    print(f1.get_memory())
    print(f2.get_memory())