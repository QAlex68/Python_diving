"""
Задание №8
Нарисовать в консоли ёлку спросив
у пользователя количество рядов.
Пример результата:
Сколько рядов у ёлки? 5
 *
 ***
 *****
 *******
*********
"""
# Вариант 1

space = ' '
elem = '*'
rows = 7
spaces = rows - 1
elems = 1
for _ in range(rows):
    print(space * spaces + elem * elems + space * spaces)
    elems += 2
    spaces -= 1

# Вариант 2
height = int(input("Введите количество рядов елки: "))

i = 0
while i < height:
    j = 0

    while j < height - 1 - i:
        print(" ", end="")
        j += 1
    j = 0
    while j < 2 * i + 1:
        print("*", end="")
        j += 1
    print("")
    i += 1
