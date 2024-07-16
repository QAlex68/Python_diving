# Напишите функцию на python get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
# Пример использования.
# На входе:
# file_path = "C:/Users/User/Documents/example.txt"
# На выходе:
# ('C:/Users/User/Documents/', 'example', '.txt')

file_path = "C:/Users/User/Documents/example.txt"

# file_path = 'file_in_current_directory.txt'

import os


def get_file_info(file_path):
    path, filename = os.path.split(file_path)
    name, extension = os.path.splitext(filename)
    if path != '':
        path = path + '/'
    return path, name, extension


info = get_file_info(file_path)
print(info)

# string = "C:/Алексей/Desktop/GreekBrains/ДОМАШКА/Python_advanced/Seminar2/seminar.py"
#
# import os
# def get_file_info(f_path: str) -> tuple:
#     path, filename = os.path.split(f_path)
#     name, extension = filename.split('.')
#     return path, name, extension
#
# print(get_file_info(file_path))
