# Модуль collections
# Модуль предоставляет доступ к встроенным в Python типам данных, но
# “спрятанным” от начинающего разработчика. Внутри хранится много интересных и
# полезных структур данных. А в collections.abc огромный набор абстрактных типов.
# Но сегодня мы рассмотрим функцию namedtuple из модуля.
# Фабричная функция namedtuple
# Функция namedtuple является фабрикой классов. Из названия следует, что она
# создаёт именованные кортежи. Рассмотрим простой пример, чтобы понять что это.
from collections import namedtuple
from datetime import datetime
User = namedtuple('User', ['first_name', 'last_name', 'birthday'])
u_1 = User('Исаак', 'Ньютон', datetime(1643, 1, 4))
print(u_1)
print(f'{type(User)}, {type(u_1)}')
