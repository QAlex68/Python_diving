# Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num = 255

hex_num = hex(num)

if num == 0:
    print("Шестнадцатеричное представление числа: ")
else:
    print("Шестнадцатеричное представление числа:", format(num, 'X'))
print("Проверка результата:", hex_num)

# Шестнадцатеричное представление числа: FF
# Проверка результата: 0xff
