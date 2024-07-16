# !! Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.

# ДЗ к семинару 6 задача 1
# работаете над разработкой программы для проверки корректности даты, введенной пользователем.
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

import argparse
import logging
from datetime import datetime

FORMAT = '{levelname:<8} - {asctime}. Модуль "{name}" ' \
         'строка {lineno:03d} функция "{funcName}()" ' \
         'в {created} сообщение: {msg}'

logging.basicConfig(format=FORMAT, style='{', level=logging.INFO, filemode='a', filename='info_task01.log',
                    encoding='utf-8')
logger = logging.getLogger(__name__)


def _is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def is_valid_date(date: str) -> bool:
    try:
        datetime.strptime(date, '%d.%m.%Y')
        logger.info(
            f'Аргумент: {date}, соответствует заданному формату DD.MM.YYYY!')
    except ValueError:
        logger.error(
            f'Аргумент: {date}, не соответствует заданному формату DD.MM.YYYY!')
        exit()
    day, month, year = map(int, date.split('.'))
    if 1 <= year <= 9999:
        if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
            return True
        elif month in [4, 6, 9, 11] and 1 <= day <= 30:
            return True
        elif month == 2 and 1 <= day <= 28 + _is_leap_year(year):
            return True
    return False


def parse_date():  # python task01.py -d 01.01.2024
    parser = argparse.ArgumentParser(description='Получаем строку в формате DD.MM.YYYY',
                                     epilog='При отсутствии параметра берется  текущая дата')
    parser.add_argument('-d', '--date', default=None, help='Введите дату в формате DD.MM.YYYY', required=False)
    args = parser.parse_args()
    if args.date is None:
        my_date = datetime.now().strftime('%d.%m.%Y')
    else:
        my_date = args.date
    return is_valid_date(my_date)


if __name__ == '__main__':
    # print(is_valid_date('02.12.10000'))
    # print(is_valid_date('02.12.2000'))
    # print(is_valid_date('02.12.1001'))
    # print(is_valid_date('02.23.2000'))
    # print(is_valid_date('50.12.2000'))
    # print(is_valid_date('29.02.2024'))
    # print(is_valid_date('12.5.-2022'))
    parse_date()

# Варианты для запуска из командной строки
# без параметров берет текущую дату
# python task01.py
# невалидные параметры записывает ошибку в лог файл
# python task01.py -d 01.2.20235
# python task01.py -d df012233
# валидные параметры записывает в лог файл, что все в порядке
# python task01.py -d 1.2.2023
# python task01.py -d 29.02.2024


