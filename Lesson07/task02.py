# Методы перемещения в файле
# При работе с файлом можно управлять положением файлового объекта в открытом
# файле. Действия напоминают движение курсора в строке стрелками влево и
# вправо.
# ● Метод tell
# Метод tell возвращает текущую позицию в файле.
text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
        'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
with open('new_data.txt', 'w', encoding='utf-8') as f:
    print(f.tell())
    for line in text:
        f.write(f'{line}\n')
        print(f.tell())
    print(f.tell())
# print(f.tell()) # ValueError: I/O operation on closed file.
# Для пустого файла возвращается ноль — начало файла. По мере записи или чтения
# информации позиция сдвигается к концу файла.
# Метод использую для определения в каком месте файла будет произведены чтение или запись.

# ● Метод seek
# Метод seek позволяет изменить положение “курсора” в файле.
# seek(offset, whence=0), где offset — смещение относительно опорной точки, whence -
# способ выбора опороной точки.
# ● whence = 0 - отсчёт от начала файла
# ● whence = 1 - отсчёт от текущей позиции в файле
# ● whence = 2 - отсчёт от конца файла
# 🔥 Важно! Значения 1 и 2 допустимы только для работы с бинарными файлами. Исключение seek(0, 2) для перехода
# в конец текстового файла.
# Метод возвращает новую позицию “курсора”.
last = before = 0
text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
        'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
    print(f'{last = }, {before = }')
    print(f'{f.seek(before, 0) = }')
    f.write('\n'.join(text))
# В примере выше мы открыли текстовый файл для одновременного чтения и записи.
# Переменные last и before хранят позиции двух последних прочитанных строк.
# Дочитав файл в цикле while до конца изменяем позицию “курсора” на начало
# последней строки и начинаем запись. Таким образом мы сохранили все строки
# файла кроме последней и записали новый текст в конец.

# ● Метод truncate
# truncate(size=None) — метод изменяет размер файла. Если не передать значение в
# параметр size будет удалена часть файла от текущей позиции до конца. Метод
# возвращает позицию после изменения файла.
last = before = 0
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
    print(f.seek(before, 0))
    print(f.truncate())
# Если передать параметр size метод изменяет размер файла до указанного числа
# символов или байт от начала файла.
size = 64
with open('new_data.txt', 'r+', encoding='utf-8') as f:
    print(f.truncate(size))
# Если size меньше размера файла, происходит усечение файла. Если size больше
# размера файла, он увеличивается до указанного размера. При этом добавленный
# размер обычно заполняется нулевыми байтами. Заполнение зависит от конкретной ОС.

# Задание
# Перед вами несколько строк кода. Что будет хранится в файле после завершения
# работы программы? И что будет выведено на печать? У вас 3 минуты.
start = 10
stop = 100
with open('data.bin', 'bw+') as f:
    for i in range(start, stop + 1):
        f.write(str(i).encode('utf-8'))
        if i % 3 == 0:
            f.seek(-2, 1)
    f.truncate(stop)
    f.seek(0)
    res = f.read(start)
    print(res.decode('utf-8'))
