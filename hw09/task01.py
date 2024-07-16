# Создайте функцию на языке python generate_csv_file(file_name, rows), которая будет генерировать по три случайны числа в каждой строке,
# от 100-1000 строк, и записывать их в CSV-файл. Функция принимает два аргумента:
# file_name (строка) - имя файла, в который будут записаны данные.
# rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.
# Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения вида ax^2 + bx + c = 0.
# Функция принимает три аргумента:
# a, b, c (целые числа) - коэффициенты квадратного уравнения.
# Функция возвращает:
# None, если уравнение не имеет корней (дискриминант отрицателен).
# Одно число, если уравнение имеет один корень (дискриминант равен нулю).
# Два числа (корни), если уравнение имеет два корня (дискриминант положителен).
# Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots.
# Декоратор выполняет следующие действия:
# Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
# Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
# Сохраняет результаты в формате JSON в файл results.json. Каждая запись JSON содержит параметры a, b, c
# и результаты вычислений.
# Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json
# будет сохранена информация о параметрах и результатах вычислений для каждой строки данных из CSV-файла.
#
# Пример
# На входе:
# generate_csv_file("input_data.csv", 101)
# find_roots("input_data.csv")
#
# with open("results.json", 'r') as f:
#     data = json.load(f)
#
# if 100<=len(data)<=1000:
#     print(True)
# else:
#     print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")
#
# print(len(data)==101)
# На выходе:
# True
# True
# Формат JSON файла определён следующим образом:
#
# [
#     {"parameters": [a, b, c], "result": result},
#     {"parameters": [a, b, c], "result": result},
#     ...
# ]


import csv
import json
import random


def generate_csv_file(file_name, rows):
    with open(file_name, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        for _ in range(rows):
            row = [random.randint(100, 1000) for _ in range(3)]
            csv_writer.writerow(row)


def save_to_json(func):
    def wrapper(file_name):
        data = []
        with open(file_name, mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                a, b, c = map(int, row)
                roots = func(a, b, c)
                data.append({"parameters": [a, b, c], "result": roots})

        with open('results.json', 'w') as f:
            json.dump(data, f, indent=4)

    return wrapper


@save_to_json
def find_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        root = -b / (2 * a)
        return root
    else:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        return root1, root2


generate_csv_file("input_data.csv", 101)
find_roots("input_data.csv")

with open("results.json", 'r') as f:
    data = json.load(f)

if 100<=len(data)<=1000:
    print(True)
else:
    print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

print(len(data)==101)


