# Дополнительный файл для запуска task02 из командной строки, результаты операций и ошибки записываются в log_task02.log
import argparse
import json
from task02 import Matrix


def parse_args():
    parser = argparse.ArgumentParser(description="Операции над двумя матрицами (+, *, =).")
    parser.add_argument('-m1', '--matrix1', type=str, default='[[1, 2, 3], [4, 5, 6], [7, 8, 9]]',
                        help='1-я матрица в in JSON формате, пример - "[[1, 2, 3], [4, 5, 6], [7, 8, 9]]"')
    parser.add_argument('-m2', '--matrix2', type=str, default='[[9, 8, 7], [6, 5, 4], [3, 2, 1]]',
                        help='2-я матрица в JSON формате, пример - "[[1, 2, 3], [4, 5, 6], [7, 8, 9]]"')
    parser.add_argument('-o', '--operation', choices=['+', '*', '='], default='+',
                        help='Доступные операции: "+", "*" или "="!')
    return parser.parse_args()


def main():
    args = parse_args()

    try:
        m1 = json.loads(args.matrix1)
        m2 = json.loads(args.matrix2)
    except json.JSONDecodeError:
        print('Error: Неверный  формат матриц, используйте аргументы в виде "[[1, 2, 3], [4, 5, 6], [7, 8, 9]]"!')
        return

    matrix1 = Matrix(m1)
    matrix2 = Matrix(m2)

    if args.operation == '+':
        result = matrix1 + matrix2
    elif args.operation == '*':
        result = matrix1 * matrix2
    elif args.operation == '=':
        result = matrix1 == matrix2
    else:
        print('Error: Неверный формат данных используйте аргумент "-o" в виде - "+", "*" или "=" !')
        return
    print(f'Результат операции: {matrix1} {args.operation} {matrix2} = {result}')


if __name__ == "__main__":
    main()

    # Примеры вызова из командной строки:
    # python task02_terminal.py - все аргументы по умолчанию
    # Валидный вызов в разных вариантах
    # python task02_terminal.py -m1 '[[1, 2, 3], [4, 5, 6], [7, 8, 9]]' -m2 '[[9, 8, 7], [6, 5, 4], [3, 2, 1]]' -o +
    # python task02_terminal.py -m1 '[[1, 2, 3], [4, 5, 6], [7, 8, 9]]' -m2 '[[9, 8, 7], [6, 5, 4], [3, 2, 1]]'
    # python task02_terminal.py -m2 '[[9, 8, 7], [6, 5, 4], [3, 2, 1]]' -o +
    # python task02_terminal.py -o +
    # Невалидный вызов:
    # python task02_terminal.py -m1 '[[1, 2, 3], [4, 5, 6], [7, 8, 9]]' -m2 '[[9, 8, 7], [6, 5, 4], [3, 2, 1]]' -o 7
    # python task02_terminal.py -m1 '[[1, 2, 3], [4, 5, 6], [7, 8, 9'
    # Сложение:
    # python task02_terminal.py -m1 '[[1, 2, 4], [5, 6, 8], [2, 5, -2], [10, 5, 0]]' -m2 '[[1, 2, 4], [5, 6, 8], [5, 6, 8], [-2, 2, 0]]' -o +
    # python task02_terminal.py -m1 '[[1, 2, 4], [5, 6, 8], [2, 5, -2], [10, 5, 0]]' -m2 '[[1, 2, 4, 5, 0], [5, 6, 8, 0, 0], [5, 0, -7, 1, 0]]' -o +
    # Умножение:
    # python task02_terminal.py -m1 '[[1, 2, 3], [4, 5, 6], [7, 8, 9]]' -m2 '[[1, 2, 4, 5], [5, 6, 8, 0], [5, 0, -7, 1]]' -o *
    # python task02_terminal.py -m1 '[[1, 2, 3], [4, 5, 6], [7, 8, 9]]' -m2 '[[1, 2, 4, 5, 0], [5, 6, 8, 0, 0], [5, 0, -7, 1, 0]]' -o *
    # python task02_terminal.py -m1 '[[1, 2, 4, 5, 0], [5, 6, 8, 0, 0], [5, 0, -7, 1, 0]]' -m2 '[[9, 8, 7], [6, 5, 4], [3, 2, 1]]' -o *
    # Сравнение:
    # python task02_terminal.py -m1 '[[1, 2, 3], [4, 5, 6], [7, 8, 9]]' -m2 '[[1, 2, 3], [4, 5, 6], [7, 8, 9]]' -o =
    # python task02_terminal.py -m1 '[[1, 2, 3], [4, 5, 6], [7, 8, 9]]' -m2 '[[9, 8, 7], [6, 5, 4], [3, 2, 1]]' -o =
    # python task02_terminal.py -m1 '[[1, 2, 4, 5, 0], [5, 6, 8, 0, 0], [5, 0, -7, 1, 0]]' -m2 '[[9, 8, 7], [6, 5, 4], [3, 2, 1]]' -o =