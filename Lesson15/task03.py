# А теперь рассмотрим ситуацию с несколькими файлами, когда мы работаем со
# сложным проектом.
# Код основного файла:
import logging
from other import log_all
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger('Основной файл проекта')
logger.warning('Внимание! Используем вызов функции из другого модуля')
log_all()

# В основном коде определили уровень логирования - WARNING. Логер вывел
# сообщение и вместо root указал текст, переданный в функцию getLogger.
# Далее мы вызываем импортированную функцию и…
# В файле other так же импортирован модуль logging. Далее мы получаем регистратор
# с именем other, оно содержится в __name__. И не смотря на попытку использовать
# все уровни логирования, срабатывают только предупреждения и выше. Функция
# getLogger взяла конфигурацию basicConfig из основного файла проекта.
