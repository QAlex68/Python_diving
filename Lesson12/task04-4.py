# Антипаттерн геттера, сеттера, делейтера
# Представленный ниже код является кодам ради кода и не имеет смысла в языке
# Python. Избегайте подобного. И да, код работает верно. Просто он не делает ничего нового.
class BadPattern:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


# Все три декоратора ничего не делают. Подобный код в Python должен выглядеть
# так, без защиты переменной x

class GoodPattern:
    def __init__(self, x):
        self.x = x


# Задание
# Перед вами несколько строк кода. Напишите что выведет программа, не запуская
# код. У вас 3 минуты.
class MyCls:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    @full_name.setter
    def full_name(self, value: str):
        self.first_name, self.last_name, _ = value.split()
        

x = MyCls('Стивен', 'Хокинг')
print(x.full_name)
x.full_name = 'Гвидо ван Россум'
print(x.full_name)
