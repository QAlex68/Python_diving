# Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем.
# На вход будет подаваться дата в формате "день.месяц.год". Ваша задача - создать программу, которая проверяет,
# является ли введенная дата корректной или нет.
# Ваша программа должна предоставить ответ "True" (дата корректна) или "False" (дата некорректна)
# в зависимости от результата проверки.
# Пример использования На входе:
# date_to_prove = 15.4.2023
# На выходе:
# True
# На входе:
# date_to_prove = 31.6.2022
# На выходе:
# False
# 💡 Поделиться мнением


# date_to_prove = '15.4.2023' +
# date_to_prove = '0.5.2022'  -
# date_to_prove = '12.0.2022'  -
# date_to_prove = '12.5.-2022' -
# date_to_prove = '29.2.2020'  +
# date_to_prove = '12.5.2022' +
# date_to_prove = '28.2.2021' +
# date_to_prove = '31.12.9999' +
# date_to_prove = '32.5.2022' +
# date_to_prove = '12.13.2022'
# date_to_prove = '29.2.2021'
# date_to_prove = '30.2.2020'


def _is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def is_valid_date(date: str) -> bool:
    day, month, year = map(int, date.split('.'))
    if 1 <= year <= 9999:
        if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
            return True
        elif month in [4, 6, 9, 11] and 1 <= day <= 30:
            return True
        elif month == 2 and 1 <= day <= 28 + _is_leap_year(year):
            return True
    return False


if __name__ == '__main__':
    print(is_valid_date('02.12.2000'))
    print(is_valid_date('02.12.1001'))
    print(is_valid_date('02.23.2000'))
    print(is_valid_date('50.12.2000'))
    print(is_valid_date('02.12.10000'))
    print(is_valid_date('29.02.2024'))
    print(is_valid_date('12.5.-2022'))