# При создании класса можно дополнительно передать список значений по
# умолчанию. И если дефолтных значений меньше, чем свойств в классе, назначение
# происходит справа налево
import time
from collections import namedtuple
from datetime import datetime
User = namedtuple('User', ['first_name', 'last_name', 'birthday'], defaults=['Иванов', datetime.now()])
u_1 = User('Исаак')
print(f'{u_1.last_name}, {u_1.birthday.strftime("%H:%M:%S")}')
time.sleep(7)
u_2 = User('Галилей', 'Галилео')
print(f'{u_2.last_name}, {u_2.birthday.strftime("%H:%M:%S")}')
# Составление списка с именами полей и значениями по умолчанию движется справа
# налево, поэтому в birthday попадает текущая дата, а фамилию по умолчанию -
# Иванов. Значения подставляются только в том случае, когда экземпляр не передаёт
# свои, как и с обычными классами.
# 💡 Внимание! Посмотрите на даты у каждого из экземпляров. Время
# совпадает до секунды несмотря на 7 секунд разницы в создании. Значения для
# birthday было вычислено один раз, в момент создания класса.
# На самом деле ситуация с функциями неоднозначно. С одной стороны ничего не
# мешает присвоить экземпляру в качестве свойства созданную функцию. Но в
# отличии от классических классов, классы namedtuple рассчитаны на хранение
# свойств, а не методов.
# 🔥 Важно! Если вам нужен объект с методами, используйте классический ООП.