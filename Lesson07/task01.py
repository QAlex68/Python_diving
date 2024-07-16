f = open('text_data.txt')
print(f)
print(list(f))

f = open('text_data.txt', 'r', encoding='utf-8')
print(f)
print(list(f))

f = open('text_data.txt', 'a', encoding='utf-8')
f.write('Окончание файла\n')
f.close()

# ➢ 'r' — открыть для чтения (по умолчанию)
# ➢ 'w' — открыть для записи, предварительно очистив файл
# ➢ 'x' — открыть для эксклюзивного создания. Вернёт ошибку, если файл уже существует
# ➢ 'a' — открыть для записи в конец файла, если он существует
# ➢ 'b' — двоичный режим
# ➢ 't' — текстовый режим (по умолчанию)
# ➢ '+' — открыть для обновления (чтение и запись)

f = open('bin_data', 'wb', buffering=64)
f.write(b'X' * 1200)
f.close()

f = open('data.txt', 'wb')
f.write('Привет, '.encode('utf-8') + 'мир!'.encode('cp1251'))
f.close()

f = open('data.txt', 'r', encoding='utf-8')
# print(list(f)) # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xec in position 14: invalid continuation byte
f.close()

f = open('data.txt', 'r', encoding='utf-8', errors='replace')
print(list(f))
f.close()

# Прочие необязательные параметры функции open
# ✔ buffering — определяет режим буферизации
# ✔ errors — используется только в текстовом режиме и определяет поведение в случае ошибок кодирования или декодирования
# ✔ newline — отвечает за преобразование окончания строки
# ✔ closefd — указывает оставлять ли файловый дескриптор открытым при закрытии файла
# ✔ opener — позволяет передать пользовательскую функцию для открытия файла

# Менеджер контекста with open
with open('text_data.txt', 'r+', encoding='utf-8') as f:
    print(list(f))
# ✔ with гарантирует закрытие файла и сохранение информации

with open('text_data.txt', 'r+', encoding='utf-8') as f1, \
        open('bin_data', 'rb') as f2, \
        open('data.txt', 'r', encoding='utf-8', errors='backslashreplace') as f3:
    print(list(f1))
    print(list(f2))
    print(list(f3))
# Открытие нескольких файлов одновременно
# Если версия 3.10 и более
with (
    open('text_data.txt', 'r+', encoding='utf-8') as f1,
    open('bin_data', 'rb') as f2,
    open('data.txt', 'r', encoding='utf-8', errors='backslashreplace') as f3
):
    print(list(f1))
    print(list(f2))
    print(list(f3))

# Чтение файла
# list(f)
# Чтение в список
# res = f.read()
# Чтение методом read
# res = f.readline()
# Чтение методом readline
# for line in f:
# Чтение циклом for

# ● Чтение в список
with open('text_data.txt', 'r', encoding='utf-8') as f:
    print(list(f))
# ● Чтение методом read
# Ещё один вариант чтения файла — метод read().
# 9
# read(n=-1) — читает n символов или n байт информации из файла. Если n
# отрицательное или не указана, читает весь файл. Попытка чтения будет даже в том
# случае, когда файл больше оперативной памяти.
with open('text_data.txt', 'r', encoding='utf-8') as f:
    res = f.read()
    print(f'Читаем первый раз\n{res}')
    res = f.read()
    print(f'Читаем второй раз\n{res}')

SIZE = 100
with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.read(SIZE):
        print(res)

# ● Чтение методом readline
# Для чтения текстового файла построчно используют метод readline.
with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.readline():
        print(res)

SIZE = 100
with open('text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.readline(SIZE):
        print(res)
# Передача положительного числа в качестве аргумента задаёт границу для длины строки

# ● Чтение циклом for
# Вместо метода readline без аргумента можно использовать более короткую запись с циклом for
with open('text_data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')

SIZE = 100
with open('text_data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line[:-1])
        print(line.replace('\n', ''))

# Запись и добавление в файл
# С режимами записи мы уже познакомились.
# ➢ w — создаём новый пустой файл для записи. Если файл существует,
# открываем его для записи и удаляем данные, которые в нём хранились.
# ➢ x — создаём новый пустой файл для записи. Если файл существует, вызываем
# ошибку.
# ➢ a — открываем существующий файл для записи в конец, добавления данных.
# Если файл не существует, создаём новый файл и записываем в него.

# Запись и добавление в файл
# res = f.write(text)
# Запись методом write
# f.writelines('\n'.join(text))
# Запись методом writelines
# print(text, file=f)
# print в файл

# ● Запись методом write
# Метод write принимает на вход строку или набор байт в зависимости от того как вы открыли файл. После записи метод
# возвращает количество записанной информации.
text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit.'
with open('new_data.txt', 'a', encoding='utf-8') as f:
    res = f.write(text)
    print(f'{res = }\n{len(text) = }')

# Метод не добавляет символ перехода на новую строку. Если произвести несколько
# записей, они “склеиваются” в файле.
text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
        'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        res = f.write(line)
        print(f'{res = }\n{len(line) = }')
# Если каждая строка должна сохранятся в файле с новой строки, необходимо
# самостоятельно добавить символ переноса - \n
text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
        'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        res = f.write(f'{line}\n')
        print(f'{res = }\n{len(line) = }')

# ● Запись методом writelines
# Метод writelines принимает в качестве аргумента последовательность и записывает
# каждый элемент в файл. Элементы последовательности должны быть строками или
# байтами в зависимости от режима записи. В отличии от write этот метод ничего не возвращает.
text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
        'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
with open('new_data.txt', 'a', encoding='utf-8') as f:
    f.writelines('\n'.join(text))
# Для того чтобы каждый элемент списка text сохранялся в файле с новой строки
# воспользовались строковым методом join. writelines не добавляет переноса между
# элементами последовательности.

# ● print в файл
# Функция print по умолчанию выводит информацию в поток вывода. Обычно это
# консоль. Но можно явно передать файловый объект для печати в файл. Для этого
# надо воспользоваться ключевым параметром file.
text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
        'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        print(line, file=f)
# В отличии от методов записи в файл, функция print добавляет перенос строки.
# Кроме того ничто не мешает явно изменить параметр end функции.
text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
        'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
        'Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
with open('new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        print(line, end='***\n##', file=f)


