# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
# Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.
# Для проверки своего кода используйте модуль fractions.


from fractions import Fraction

frac1 = "1/2"
frac2 = "1/3"

from fractions import Fraction

def calculate_fractions(frac1, frac2):
    # Преобразуем строки в дроби
    fraction1 = Fraction(frac1)
    fraction2 = Fraction(frac2)

    # Считаем сумму дробей
    sum_result = fraction1 + fraction2
    # Считаем произведение дробей
    prod_result = fraction1 * fraction2

    # Выводим результаты
    print(f"Сумма дробей: {sum_result}")
    print(f"Произведение дробей: {prod_result}")
    print(f"Сумма дробей: {sum_result}")
    print(f"Произведение дробей: {prod_result}")


calculate_fractions(frac1, frac2)