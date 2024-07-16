# ...............   Задание №4   .................

# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 15
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 3
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.


import os
from string import ascii_letters, ascii_lowercase
from random import randint, choices, randbytes


def file_gen(
        extent: str,
        min_len: int = 6,
        max_len: int = 30,
        min_size: int = 256,
        max_size: int = 4096,
        file_num: int = 3
) -> None:
    for _ in range(file_num):
        # data = bytes(randint(0,255)) for i in range(randint(min_size, max_size))
        data = randbytes(randint(min_size, max_size))
        #

        file_name = ''.join(choices(ascii_lowercase + '_', k=randint(min_len, max_len)))
        with open(f'C:\\Users\\annao\\Documents\\NEW_LIFE_PYTHON\\new_file\\{file_name}.{extent}', 'wb') as f_wb:
            f_wb.write(data)


# .................   Задание №5   ....................

# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

def gen_files(**kwargs) -> None:
    for extent, count in kwargs.items():
        file_gen(extent, file_num=count)


if __name__ == '__main__':
    gen_files(txt=2, jpeg=1)