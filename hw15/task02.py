# !! Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.
"""
ДЗ к семинару 11 задача 4
Создайте класс Матрица. Добавьте методы для:
○ вывода на печать,
○ сравнения,
○ сложения,
○ *умножения матриц
"""

import logging

FORMAT = '{levelname:<8} - {asctime}. Модуль "{name}" ' \
         'строка {lineno:03d} функция "{funcName}()" ' \
         'в {created} сообщение: {msg}'

logging.basicConfig(format=FORMAT, style='{', level=logging.INFO, filemode='w', filename='log_task02.log',
                    encoding='utf-8')
logger = logging.getLogger('task02')


class Matrix:

    def __init__(self, matr):
        self._matr = matr

    def get_matrix(self):
        return self._matr

    def __add__(self, other):
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            logger.error(
                f'Операция сложения невозможна, матрицы разных размеров: '
                f'[{len(self._matr)}]x[{len(self._matr[0])}] !=  [{len(other._matr)}]x[{len(other._matr[0])}]')
            return f'Error: Сложение матриц невозможно, матрицы разных размеров!!'
        else:
            new_matr = Matrix([[self._matr[i][j] + other._matr[i][j] for j in range(len(self._matr[0]))] for i in
                               range(len(self._matr))])
            logger.info(f'сложение матриц: {self._matr} + {other._matr} = {new_matr}')
            return new_matr

    def __mul__(self, other):
        if len(self._matr[0]) != len(other._matr):
            logger.error(
                f'Операция умножения  невозможна, количество столбцов != количеству строк: '
                f'[{len(self._matr[0])}] != [{len(other._matr)}]')
            return f'Error: Произведение матриц  невозможно, количество столбцов != количеству строк!!'
        else:
            new_matr = [[sum(i * j for i, j in zip(i_row, j_col)) for j_col in zip(*other._matr)] for i_row in
                        self._matr]
            logger.info(f'произведение матриц: {self._matr} * {other._matr} = {new_matr}')
            return Matrix(new_matr)

    def __eq__(self, other):
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            logger.error(
                f'Операция сравнения невозможна, матрицы разных размеров: '
                f'[{len(self._matr)}]x[{len(self._matr[0])}] !=  [{len(other._matr)}]x[{len(other._matr[0])}]')
            return f'Error: Сравнение матриц невозможно, матрицы разных размеров!!'
        else:
            for i in range(len(self._matr)):
                for j in range(len(self._matr[0])):
                    if self._matr[i][j] != other._matr[i][j]:
                        logger.info(f'сравнение матриц: {self._matr} != {other._matr}')
                        return False
            logger.info(f'сравнение матриц: {self._matr} == {other._matr}')
            return True

    def __str__(self):
        res = ''
        for i in range(len(self._matr)):
            res += str(self._matr[i]) + ', '
        return '[' + res[:-2] + ']'

    def __repr__(self):
        res = ''
        for i in range(len(self._matr)):
            res += str(self._matr[i]) + ', '
        return f'Matrix([{res[:-2]}])'


if __name__ == '__main__':
    m_1 = [[1, 2, 4],
           [5, 6, 8],
           [2, 5, -2],
           [10, 5, 0]]

    m_2 = [[1, 2, 4],
           [5, 6, 8],
           [5, 6, 8],
           [-2, 2, 0]]

    m_3 = [[1, 2, 4, 5],
           [5, 6, 8, 0],
           [5, 0, -7, 1]]

    m_4 = [[1, 2, 4, 5, 0],
           [5, 6, 8, 0, 0],
           [5, 0, -7, 1, 0]]

    matr_1 = Matrix(m_1)
    matr_2 = Matrix(m_2)
    matr_3 = Matrix(m_3)
    matr_4 = Matrix(m_4)

    print("Cложение матриц:")
    print(matr_1 + matr_2)
    print(matr_1 + matr_4)

    print("Умножение матриц:")
    print(matr_1 * matr_3)
    print(matr_1 * matr_4)
    print(matr_4 * matr_1)

    print("Cравнение матриц:")
    print(matr_1 == matr_1)
    print(matr_1 == matr_2)
    print(matr_4 == matr_1)
