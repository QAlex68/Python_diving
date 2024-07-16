from datetime import datetime


class MyStr(str):
    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = datetime.now().strftime('%y-%m-%d %H:%M')
        return instance

    def __str__(self):
         return f"{super().__str__()} (Автор: {self.author}, Время создания: {self.time})"
         return f"{self} (автор: {self.author}, время создания: {self.time})"

    def __repr__(self):
        return f"MyStr('{self}', '{self.author}')"


# Пример использования
event = MyStr("завершилось тестирование", "john")
print(event)

my_string = MyStr("пример текста", "иван")
print(my_string)

my_string = MyStr("мама мыла раму", "маршак")
print(repr(my_string))
