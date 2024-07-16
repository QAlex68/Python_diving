"""
Задание №5
Работа в консоли в режиме интерпретатора Python.
Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
Используйте while и if.
Попробуйте разные значения e и n.
"""

n = 20
e = 3
sum_num = 0
number = 0
while number <= n:
    number += 1
    if number % 2 == 0:
        if number % e == 0:
            continue
        sum_num += number
print(f'Сумма = {sum_num}')



