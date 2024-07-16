# 2. Иерархия исключений в Python
# Любое исключение в Python является классом. При этом одни классы наследуются от
# других. Общая иерархия классов для встроенных исключений Python выглядит так:
# BaseException
# 11
# ├
# ─
# ─
# B
# a
# s
# e
# E
# x
# c
# e
# p
# t
# i
# o
# n
# G
# r
# o
# u
# p
# ├
# ─
# ─
# G
# e
# n
# e
# r
# a
# t
# o
# r
# E
# x
# i
# t
# ├
# ─
# ─
# K
# e
# y
# b
# o
# a
# r
# d
# I
# n
# t
# e
# r
# r
# u
# p
# t
# ├
# ─
# ─
# S
# y
# s
# t
# e
# m
# E
# x
# i
# t
# └
# ─
# ─
# E
# x
# c
# e
# p
# t
# i
# o
# n
# ├
# ─
# ─
# A
# r
# i
# t
# h
# m
# e
# t
# i
# c
# E
# r
# r
# o
# r │ ├── FloatingPo
# i
# n
# t
# E
# r
# r
# o
# r │ ├── OverflowError │ └── ZeroDivisionError ├── AssertionError ├── AttributeError ├── BufferError ├── EOFError ├── ExceptionGroup [BaseExc
# e
# p
# t
# i
# o
# n
# G
# r
# o
# u
# p
# ]
# ├
# ─
# ─
# I
# m
# p
# o
# r
# t
# E
# r
# r
# o
# r │ └── Module
# N
# o
# t
# F
# o
# u
# n
# d
# E
# r
# r
# o
# r
# ├
# ─
# ─
# L
# o
# o
# k
# u
# p
# E
# r
# r
# o
# r │ ├── IndexE
# r
# r
# o
# r │ └── KeyError ├── MemoryError ├── NameError │ └── UnboundLoc
# a
# l
# E
# r
# r
# o
# r
# ├
# ─
# ─
# O
# S
# E
# r
# r
# o
# r │ ├── Bl
# o
# c
# k
# i
# n
# g
# I
# O
# E
# r
# r
# o
# r │ ├── ChildProcessErr
# o
# r │ ├── ConnectionError │ │ ├── BrokenPipeEr
# r
# o
# r │ │ ├── ConnectionAbort
# e
# d
# E
# r
# r
# o
# r │ │ ├── ConnectionRefusedError │ │ └── ConnectionResetError │ ├── FileExistsError │ ├── FileNotFoundError │ ├── InterruptedError │ ├── IsADirectoryError │ ├── NotADirectoryError │ ├── PermissionError │ ├── ProcessLookupError │ └── TimeoutError ├── ReferenceError ├── RuntimeError │ ├── NotImplementedError │ └── RecursionError ├── StopAsyncIteration ├── StopIteration ├── SyntaxError │ └── IndentationError │ └── TabError ├── SystemError ├── TypeError ├── ValueError │ └── UnicodeError
# 1
# 2
# │ ├── UnicodeDecodeError
# │ ├── UnicodeEncodeError
# │ └── UnicodeTranslateError
# └── Warning
# ├── BytesWarning
# ├── DeprecationWarning
# ├── EncodingWarning
# ├── FutureWarning
# ├── ImportWarning
# ├── PendingDeprecationWarning
# ├── ResourceWarning
# ├── RuntimeWarning
# ├── SyntaxWarning
# ├── UnicodeWarning
# └── UserWarning
# BaseException и его ближайшие
# родственники
# Базовым исключением является класс BaseException. Все остальные исключения
# являются его потомками. Не рекомендуется его перехватывать или использовать в
# создании своих исключений. Оно нужно для правильной иерархии исключений,
# ожидаемого поведения Python.
# Помимо BaseException в подавляющем большинстве случаев не перехватывают и
# следующие исключения:
# ● BaseExceptionGroup — базовое исключение для объединения исключений в
# группу
# ● GeneratorExit — исключение создаёт генератор или корутина при закрытии.
# Подобное ситуация не является ошибкой с технической точки зрения.
# ● KeyboardInterrupt — возникает при нажатии комбинации клавиш,
# прерывающих работу программы. Например Ctrl-C в терминале посылает
# сигнал, требующий завершить процесс
# ● SystemExit — при выходе из программы через функцию exit() поднимается
# данное исключение.
# Основной Exception и его наследники
# 13
# Исключение Exception является базовым для всех исключений Python. Также оно
# используется при создании своих собственных исключений.
# Перечислим некоторые часто встречающиеся исключения и дадим пояснения по
# ним.
# ● ArithmeticError — арифметическая ошибка.
# ○ FloatingPointError — порождается при неудачном выполнении операции
# с плавающей запятой. На практике встречается нечасто.
# ○ OverflowError — возникает, когда результат арифметической операции
# слишком велик для представления. Не появляется при обычной работе
# с целыми числами (так как python поддерживает длинные числа), но
# может возникать в некоторых других случаях.
# ○ ZeroDivisionError — деление на ноль.
# ● AssertionError — выражение в функции assert ложно. Подробнее об assert
# поговорим на следующей лекции, когда будем разбирать тестирование кода.
# ● AttributeError — объект не имеет данного атрибута (значения или метода).
# ● BufferError — операция, связанная с буфером, не может быть выполнена.
# ● EOFError — функция наткнулась на конец файла и не смогла прочитать то, что
# хотела.
# ● ImportError — не удалось импортирование модуля или его атрибута.
# ● LookupError — некорректный индекс или ключ.
# ○ IndexError — индекс не входит в диапазон элементов.
# ○ KeyError — несуществующий ключ (в словаре, множестве или другом
# объекте).
# ● MemoryError — недостаточно памяти.
# ● NameError — не найдено переменной с таким именем.
# ● UnboundLocalError — сделана ссылка на локальную переменную в функции,
# но переменная не определена ранее.
# ● OSError — ошибка, связанная с системой.
# ○ BlockingIOError — возникает, когда операция блокирует объект
# (например, сокет), установленный для неблокирующей операции
# ○ ChildProcessError — неудача при операции с дочерним процессом.
# ○ ConnectionError — базовый класс для исключений, связанных с
# подключениями.
# ■ BrokenPipeError — возникает при попытке записи в канал, в то
# время как другой конец был закрыт, или при попытке записи в
# сокет, который был отключен для записи
# ■ ConnectionAbortedError — попытка соединения прерывается
# узлом
# ■ ConnectionRefusedError — партнер отклоняет попытку
# подключения
# ■ ConnectionResetError - соединение сбрасывается узлом
# 14
# ○ FileExistsError — попытка создания файла или директории, которая уже
# существует.
# ○ FileNotFoundError — файл или директория не существует.
# ○ InterruptedError — системный вызов прерван входящим сигналом.
# ○ IsADirectoryError — ожидался файл, но это директория.
# ○ NotADirectoryError — ожидалась директория, но это файл.
# ○ PermissionError — не хватает прав доступа.
# ○ ProcessLookupError — указанного процесса не существует.
# ○ TimeoutError — закончилось время ожидания.
# ● ReferenceError — попытка доступа к атрибуту со слабой ссылкой.
# ● RuntimeError — возникает, когда исключение не попадает ни под одну из
# других категорий.
# ○ NotImplementedError — возникает, когда абстрактные методы класса
# требуют переопределения в дочерних классах.
# ○ RecursionError — превышена глубина стека вызова функций.
# ● StopAsyncIteration — порождается в корутине (асинхронной функции), если в
# итераторе больше нет элементов.
# ● StopIteration — порождается встроенной функцией next, если в итераторе
# больше нет элементов.
# ● SyntaxError — синтаксическая ошибка.
# ○ IndentationError — неправильные отступы.
# ■ TabError — смешивание в отступах табуляции и пробелов.
# ● SystemError — интерпретатор находит внутреннюю ошибку, но ситуация не
# выглядит настолько серьезной, чтобы заставить его отказаться от всякой
# надежды. Возвращаемое значение представляет собой строку,
# указывающую, что пошло не так.
# ● TypeError — операция применена к объекту несоответствующего типа.
# ● ValueError — функция получает аргумент правильного типа, но некорректного
# значения.
# ○ UnicodeError — ошибка, связанная с кодированием / раскодированием
# unicode в строках.
# ■ UnicodeEncodeError — исключение, связанное с кодированием
# unicode.
# ■ UnicodeDecodeError — исключение, связанное с декодированием
# unicode.
# ■ UnicodeTranslateError — исключение, связанное с переводом
# unicode.
# ● Warning — группа для предупреждений.
# 15
# Группа Warning
# Warning включает в себя ряд базовых предупреждений. Предупреждающие
# сообщения обычно выдаются в ситуациях, когда полезно предупредить
# пользователя о каком-либо состоянии в программе, когда это условие не требует
# возбуждения исключения и завершения программы. Например, может
# потребоваться выдать предупреждение, когда программа использует устаревший
# модуль.