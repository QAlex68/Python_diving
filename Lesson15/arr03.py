# При этом массив не позволит добавить значение, если оно выходит за пределы
# диапазона, заданного кодом типа при создании. Так же будет поднята ошибка при
# несоответствии типа.
from array import array
long_array = array('l', [-6000, 800, 100500])
# long_array.append(2**32) # OverflowError: Python int too large to convert to C long
# long_array.append(3.14) # TypeError: 'float' object cannot be interpreted as an integer
# Массивы array являются более экономичной по памяти структурой данных, чем
# списки list.

# Задание
# Перед вами несколько строк кода. Напишите что выведет программа, не запуская
# код. У вас 3 минуты.
from collections import namedtuple
Data = namedtuple('Data', ['mathematics', 'chemistry', 'physics', 'genetics'], defaults=[5, 5, 5, 5])
d = {
'Ivanov': Data(4, 5, 3, 5),
'Petrov': Data(physics=4, genetics=3),
'Sidorov': Data(),
}
print(d)