"""
Задание №9
Выведите в консоль таблицу умножения
от 2х2 до 9х10 как на школьной тетрадке.
"""

# Вариант 1

for k in [0, 4]:
    for i in range(2, 11):
        result = ''
        for j in range(2 + k, 6 + k):
            result += f'{j:^2} x {i:^2} = {i * j:^2}\t'
        print(result)
    print()

# Вариант 2

for k in range(2):
    for i in range (2,10):
        for j in range(k*4 + 2, k*4+6):
            print(f'{j:<2} * {i:<2} = {i * j: < 10}\t', end="")
        print("")
    print("")


