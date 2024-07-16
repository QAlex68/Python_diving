# Метод вызова функции __call__
# Создадим класс, экземпляры которого можно вызывать. Например для добавления
# очередного элемента во внутренний словарь класса по типам.
from collections import defaultdict


class Storage:
    def __init__(self):
        self.storage = defaultdict(list)

    def __str__(self):
        txt = '\n'.join((f'{k}: {v}' for k, v in self.storage.items()))
        return f'Объекты хранилища по типам:\n{txt}'

    def __call__(self, value):
        self.storage[type(value)].append(value)
        return f'К типу {type(value)} добавлен {value}'


s = Storage()
print(s(42))
print(s(72))
print(s('Hello world!'))
print(s(0))
print(s)


# При создании класса используется продвинутая версия словаря из модуля
# collections — defaultdict. Словарю передана функция list. При обращении к
# несуществующему ключу вместо ошибки будет создан ключ и вызвана функция list
# для создания значения ключа.
# Каждый вызов экземпляра добавляет переданный аргумент value в словарь storage
# и возвращает строку с информацией о выполненном действии.
# Последовательно вызывая экземпляр с числами и текстом выводим его не печать и
# видим содержимое на момент печати.
# Плюсом вызова экземпляра является то, что он не удаляется из памяти после
# вызова как обычная функция. Следовательно экземпляр может накапливать
# значения, использоваться в технологии мемоизации. Её рассматривали на лекции о
# декораторах.

# Задание
# Перед вами несколько строк кода. Напишите что выведет программа, не запуская
# код. У вас 3 минуты.
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'MyClass(a={self.a}, b={self.b})'

    def __call__(self, *args, **kwargs):
        self.a.append(args)
        self.b.update(kwargs)
        return True


x = MyClass([42], {73: True})
y = x(3.14, 100, 500, start=1)
x(y=y)
print(x)
