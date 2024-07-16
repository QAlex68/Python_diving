# Функции

# def my_func():
#     pass


# if __name__ == "__main__":
#     my_func()

# Квадратное уравнение
# def quadratic_equations(a: int | float, b: int | float, c: int | float) -> tuple[float, float] | float | str:
#     d = b ** 2 - 4 * a * c
#     if d > 0:
#         return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
#     elif d == 0:
#         return -b / (2 * a)
#     else:
#         return 'Нет решений'

# Лучше так

def quadratic_equations(a: int | float, b: int | float, c: int | float) -> tuple[float, float] | float | None:
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    elif d == 0:
        return -b / (2 * a)
    else:
        return None


print(quadratic_equations(2, -3, -9))


# Внешний объект не изменяется
def no_mutable(a: int) -> int:
    a += 1
    print(f'In func {a = }')  # Для демонстрации работы, но не для привычки принтить из функции
    return a


a = 42
print(f'In main {a = }')
z = no_mutable(a)
print(f'{a = }\t{z = }')


# В данном случае затрагивает и внешний объект
def mutable(data: list[int]) -> list[int]:
    for i, item in enumerate(data):
        data[i] = item + 1
        print(f'In func {data = }')  # Для демонстрации работы, но не для привычки принтить из функции
    return data


my_list = [2, 4, 6, 8]
print(f'In main {my_list = }')
new_list = mutable(my_list)
print(f'{my_list = }\t{new_list = }')


# Возврат значения

def quadratic_equations1(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    if d == 0:
        return -b / (2 * a)
    return None  # Если это убрать python сам вернет None


print(quadratic_equations1(2, -3, -9))


# Неявный возврат

def no_return(data: list[int]):
    for i, item in enumerate(data):
        data[i] = item + 1
        print(f'In func {data = }')  # Для демонстрации работы, но не для привычки принтить из функции


my_list = [2, 4, 6, 8]
print(f'In main {my_list = }')
new_list = no_return(my_list)
print(f'{my_list = }\t{new_list = }')


# Значения по умолчанию

def quadratic_equations2(a, b=0, c=0):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    if d == 0:
        return -b / (2 * a)


print(quadratic_equations2(2, -9))


# Изменяемый объект как значение по умолчанию
# В качестве значения по умолчанию нельзя указывать изменяемы типы: списки,
# словари и т.п. Это приведёт к неожиданным результатам:

def from_one_to_n(n, data=[]):
    for i in range(1, n + 1):
        data.append(i)
    return data


new_list = from_one_to_n(5)
print(f'{new_list = }')
other_list = from_one_to_n(7)
print(f'{other_list = }')


# Объект сохраняется внутри функции и при следующем вызове дописывает в себя
# Как правильно использовать

def from_one_to_n1(n, data=None):
    if data is None:
        data = []
    for i in range(1, n + 1):
        data.append(i)
    return data


new_list = from_one_to_n1(5)
print(f'{new_list = }')
other_list = from_one_to_n1(7)
print(f'{other_list = }')


# Позиционные и ключевые параметры
# Пришло время поговорить о позиционных и ключевых параметрах функции. Начнём
# с общего синтаксиса.
# def func(positional_only_parameters, /, positional_or_keyword_parameters, *, keyword_only_parameters):
#     pass

# Пример обычной функции:
def standard_arg(arg):
    print(arg)  # Принтим для примера, а не для привычки


# standard_arg(42)
standard_arg(arg=42)


# Пример только позиционной функции:
def pos_only_arg(arg, /):
    print(arg)  # Принтим для примера, а не для привычки


pos_only_arg(42)


# pos_only_arg(arg=42)  # TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'


# Теперь функция принимает только позиционные параметры.


# Пример только ключевой функции:
def kwd_only_arg(*, arg):
    print(arg)  # Принтим для примера, а не для привычки


# kwd_only_arg(42)
kwd_only_arg(arg=42)


# А теперь наоборот, можем принимать только значения по ключу

# Пример функции со всеми вариантами параметров:
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)  # Принтим для примера, а не для привычки


# combined_example(1, 2, 3)  # TypeError: combined_example() takes 2 positional arguments but 3 were given
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)


# combined_example(pos_only=1, standard=2,
# kwd_only=3)  # TypeError: combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'
# И наконец пример со всеми возможными вариантами параметров


# Параметры args и kwargs
# Отдельно разберём пару особых параметров. Звёдочка args и две звёздочки kwargs.
# Важно! Python в первую очередь смотрит на звёздочки, а не на имя переменной. Но
# среди разработчиков приняты имена args и kwargs. Они делают код привычным, т.е.
# повышают читаемость. Не используйте другие переменные.
# Начнём с *args

def mean(*args):
    return sum(args) / len(args)


print(mean(*[1, 2, 3]))
print(mean(1, 2, 3))


# Теперь функция принимает любое число позиционных аргументов. Переменная args
# превращается в кортеж. Можно сказать, что звёздочка упаковала все позиционные
# аргументы в один кортеж.

# Параметр **kwargs работает аналогично, но принимает ключевые параметры и
# возвращает словарь.
def school_print(**kwargs):
    for key, value in kwargs.items():
        print(f'По предмету "{key}" получена оценка {value}')


school_print(химия=5, физика=4, математика=5, физра=5)


# Области видимости: global и nonlocal
# Хорошая функция работает как чёрный ящик. Использует только переданные ей
# значения и возвращает ответ. Но в Python функции могут обращаться к внешним
# переменным без явной передачи в качестве аргумента.
# В Python есть несколько областей видимости:
# ● локальная — код внутри самой функции, т.е. переменные заданные в теле
# функции.
# ● глобальная — код модуля, т.е. переменные заданные в файле py содержащем
# функцию.
# ● не локальная — код внешней функции, исключающий доступ к глобальным
# переменным.
# Разберем на примерах

# Локальные переменные:
def func(y: int) -> int:
    x = 100
    print(f'In func {x = }')  # Для демонстрации работы, но не для привычки принтить из функции
    return y + 1


x = 42
print(f'In main {x = }')
z = func(x)
print(f'{x = }\t{z = }')


# Глобальные переменные:
def func1(y: int) -> int:
    global x
    x += 100
    print(f'In func {x = }')  # Для демонстрации работы, но не для привычки принтить из функции
    return y + 1


x = 42
print(f'In main {x = }')
z = func1(x)
print(f'{x = }\t{z = }')


# Не локальные переменные:
def main(a):
    x = 1

    def func(y):
        nonlocal x
        x += 100
        print(f'In func {x = }')  # Для демонстрации работы, но не для привычки принтить из функции
        return y + 1

    return x + func(a)


x = 42
print(f'In main {x = }')
z = main(x)
print(f'{x = }\t{z = }')
# Функция func вложена в функцию main. Благодаря команде nonlocal мы смогли
# получить доступ к x = 1. В результат внутри func x увеличился до 101. В отличии от
# команды global, мы не смогли увидеть внешний x = 42. nonlocal позволяет заглянуть
# на верхний уровень вложенности, но не выходить на глобальные переменные
# модуля.


# Доступ к константам
# Один из случаев когда обращение из тела функции к глобальной переменной
# считается нормальным — доступ к константам.
LIMIT = 1_000


def func2(x, y):
    result = x ** y % LIMIT
    return result


print(func2(42, 73))

# Константа LIMIT является глобальной. При обращении к ней из функции
# производится поиск в локальной области, т.е. в теле функции. Далее поиск
# переходит на уровень выше, в глобальную область видимости модуля. Чтение
# значений констант внутри функции будет работать без ошибок.


# Анонимная функция lambda
# Анонимные функции, они же лямбда функции — синтаксический сахар для обычных
# питоновских функций с рядом ограничений. Они позволяют задать функцию в одну
# строку кода без использования других ключевых слов.
# Рассмотрим пример обычной функции и её аналог в виде лямбды для проведения
# параллели.
def add_two_def(a, b):
    return a + b
add_two_lambda = lambda a, b: a + b

print(add_two_def(42, 3.14))
print(add_two_lambda(42, 3.14))

my_dict = {'two': 2, 'one': 1, 'four': 4, 'three': 3, 'ten': 10}
s_key = sorted(my_dict.items())
s_value = sorted(my_dict.items(), key=lambda x: x[1])
print(f'{s_key = }\n{s_value = }')

# В первом случае словарь сортируется по ключам, т.е. по алфавиту. Во втором
# благодаря лямбде указали сортировку по второму (индексация начинается с нуля)
# элементу, т.е. по значению.


# Документирование кода функций
# Несколько слов о документировании функций. Начнём с того, что документация
# обычно пишется на английском языке, как универсальном для программистов из
# любой страны. Вполне допустим и родной язык, если проект локальный. Но лучше
# воспользоваться онлайн переводчиком и сразу привыкнуть к документированию на
# английском.
# def max_before_hundred(*args):
# """Return the maximum number not exceeding 100."""
# m = float('-inf')
# for item in args:
# if m < item < 100:
# m = item
# return m
# print(max_before_hundred(-42, 73, 256, 0))
# 19
# Пояснения к однострочной строке документации
# ● Тройные кавычки используются, даже если строка помещается на одной
# строке. Это позволяет легко расширить его позже.
# ● Закрывающие кавычки находятся на той же строке, что и открывающие. Это
# выглядит лучше для однострочников.
# ● Нет пустой строки ни до, ни после строки документации.
# ● Строка документации — это фраза, заканчивающаяся точкой. Он описывает
# действие функции или метода как команду
# ● Однострочная строка документации не должна повторять параметры
# функции.
# 🔥 Внимание! В программе использована переменная, а точнее константа
# “минус бесконечность” float('-inf'). Это особая форма представления
# бесконечности в памяти интерпретатора, аналогичная бесконечности из
# модуля math.
# Если описание функции подразумевает больше подробностей, после первой строки
# документации оставляют одну пустую. Далее в несколько строк даётся всё
# необходимое описание. Закрывающие кавычки ставятся на отдельной строке, без
# текста.
# def max_before_hundred(*args):
# """Return the maximum number not exceeding 100.
# :param args: tuple of int or float numbers
# :return: int or float number from the tuple args
# """
# ...
# Подобная запись автоматические помещает текст в переменную __doc__. Описание
# функции можно будет получить через вызов справки help с передачей функции в
# качестве аргумента.
# help(max_before_hundred)

# Функции “из коробки”
# В Python есть ряд встроенных функций. Они доступны всегда, без импортов и
# других подготовительных операций. Перечислим их в алфавитном порядке:
# abs(), aiter(), all(), any(), anext(), ascii(), bin(), bool(), breakpoint(), bytearray(), bytes(),
# callable(), chr(), classmethod(), compile(), complex(), delattr(), dict(), dir(), divmod(),
# enumerate(), eval(), exec(), filter(), float(), format(), frozenset(), getattr(), globals(),
# hasattr(), hash(), help(), hex(), id(), input(), int(), isinstance(), issubclass(), iter(), len(),
# list(), locals(), map(), max(), memoryview(), min(), next(), object(), oct(), open(), ord(),
# pow(), print(), property(), range(), repr(), reversed(), round(), set(), setattr(), slice(),
# sorted(), staticmethod(), str(), sum(), super(), tuple(), type(), vars(), zip().
# Часть функций мы уже разбирали на прошлых лекциях. Ещё часть разберём
# сегодня. О некоторых функциях поговорим на следующих лекциях курса.


data = [25, -42, 146, 73, -100, 12]
print(list(map(str, data)))
print(max(data, key=lambda x: -x))
print(*filter(lambda x: not x[0].startswith('__'), globals().items()))





