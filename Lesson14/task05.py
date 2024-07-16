# 🔥 Важно! Обычно документацию пишут на английском языке. В учебном
# примере специально был выбран русский как основной язык на учебной
# платформе. Вы всегда можете использовать современные online переводчики
# для получения нужного языка.
# В документации есть несколько примеров, имитирующих работу в режиме
# интерпретатора. Убедимся, что они рабочие, написав в отдельном файле пару строк кода.
import doctest

doctest.testfile('prime.md', verbose=True)

# Функция testfile построчно читает переданный ей файл и если встречает примеры
# выполнения кода, тестирует их работоспособность. Обратите внимание, что мы
# указываем на необходимость импорта функции в самом начале документации. И
# после вызова оставили пустую строку. doctest сделает импорт и не будет ожидать
# ничего в ответ. Да, это строчка будет воспринята как тест. И без него все
# последующие примеры провалятся. Ведь режим интерпретатора работает
# последовательно.

# Запуск тестов из командной строки
# Прежде чем завершить введение работу с модулем doctest пара примеров запуска
# из терминала.
# 🔥 Важно! Не путайте терминал (консоль, командную строку) операционной
# системы и консольный режим работы интерпретатора Python.
# PS C:\Users\PycharmProjects> python -m doctest .\prime.py
# PS C:\Users\PycharmProjects> python -m doctest .\prime.py -v
# PS C:\Users\PycharmProjects> python -m doctest .\prime.md
# PS C:\Users\PycharmProjects> python -m doctest .\prime.md -v
# Вызываем интерпретатор python и в качестве модуля указываем doctest. Далее
# передаём путь до файла, который хотим тестировать. Если файл имеет расширение
# py, запускает функция testmod (строки 1 и 2). А если у файла другое расширение,
# предполагается что это исполняемая документация и запускается функция testfile
# (строки 3 и 4). Дополнительный ключ -v включает режим подробного вывода
# результатов тестирования.
# 🔥 Внимание! Пример кода сделан в терминале PowerShell. В зависимости
# от используемого вами терминала строка приглашения может быть другой. Но
# текст команд одинаков для любой ОС и любого терминала.