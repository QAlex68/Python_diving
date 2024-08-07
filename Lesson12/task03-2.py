# ● Действия при выходе из менеджера контекста, __exit__
# Добавим дандер метод __exit__ и пропишем в нём операции, обязательные при
# завершении работы с базой данных.
import sqlite3


class DB:
    def __init__(self, name):
        self.name = name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.name)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()
        self.cursor = self.connection = None


db = DB('sqlite.db')
with db as cur:
    cur.execute("""create table if not exists users(name, age);""")
    cur.execute("""insert into users values ('Гвидо', 66);""")


# Внутри __exit__ подтверждаем изменения, закрываем соединения с базой и
# обнуляем свойства экземпляра. Параметры дандер __exit__ содержат информацию
# о типе и значении ошибки и трассировку, если она возникла внутри менеджера.
# Если ошибок не было, все три параметра содержат None.


# Задание
# Перед вами несколько строк кода. Напишите что выведет программа, не запуская
# код. У вас 3 минуты.
class MyCls:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __enter__(self):
        self.full_name = self.first_name + ' ' + self.last_name
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.full_name = self.full_name.upper()


x = MyCls('Гвидо ван', 'Россум')
with x as y:
    print(y.full_name)
    print(x.full_name)
print(y.full_name)
print(x.full_name)
