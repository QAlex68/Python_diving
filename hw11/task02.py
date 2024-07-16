# Разработайте программу  на пайтон для хранения и управления текстовыми и числовыми записями.
# Вам нужно создать класс Archive, который будет представлять архив и реализовывать следующую функциональность:
# Методы и операции:
# При создании экземпляра класса Archive с указанием текстовой и числовой записи (text и number),
# записи добавляются в соответствующие атрибуты archive_text и archive_number.
# Если архив уже существует, текущие записи (text и number) добавляются в архив.
# Метод __str__ возвращает строковое представление объекта,
# включая текущие записи (text и number) и архивированные записи (archive_text и archive_number).
# Метод __repr__возвращает строковое представление объекта,
# которое можно использовать для создания нового объекта того же класса с теми же записями.
# Архивированные записи могут быть получены через атрибуты archive_text и archive_number.
# Метод __new__ - это статический метод, который создает новый экземпляр класса.
# Первым аргументом метод __new__ получает ссылку на класс (cls),
# а затем может принимать дополнительные аргументы.
# Метод __new__ проверяет, существует ли уже экземпляр класса Archive (с использованием атрибута _instance).
# Если экземпляр существует, то метод вместо создания нового экземпляра добавляет текущие значения text и number в архив
# (списки archive_text и archive_number) для уже существующего экземпляра. Если экземпляр еще не существует,
# метод создает новый экземпляр класса Archive с пустыми архивами для текстовых и числовых записей.
# В любом случае метод возвращает созданный или существующий экземпляр класса Archive.
# Метод __init__ - это конструктор экземпляра класса, который вызывается после создания экземпляра с использованием метода __new__.
# Метод __init__ принимает два аргумента: text (строка) и number (целое число или число с плавающей точкой).
# В методе __init__устанавливаются атрибуты text и number текущего экземпляра класса для хранения переданных
# текстовой и числовой записей. Эти записи могут быть затем добавлены в архив (списки archive_text и archive_number)
# с использованием метода __new__.
# Пример
# На входе:
# archive1 = Archive("Запись 1", 42)
# archive2 = Archive("Запись 2", 3.14)
# На выходе:
# Text is Запись 1 and number is 42. Also ['Запись 1'] and [42]
# Text is Запись 2 and number is 3.14. Also ['Запись 1', 'Запись 2'] and [42, 3.14]

class Archive:
    _instance = None
    _archive_text = []
    _archive_number = []

    def __new__(cls, text, number):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, text, number):
        if not hasattr(self, 'text'):  # Инициализируем только первый раз
            self.text = text
            self.number = number
            self._archive_text.append(self.text)
            self._archive_number.append(self.number)
        else:
            # Обновляем текущие значения и добавляем их в архив
            self.text = text
            self.number = number
            self._archive_text.append(self.text)
            self._archive_number.append(self.number)

    def __str__(self):
        return f"Text is {self.text} and number is {self.number}. Also {self._archive_text} and {self._archive_number}"

    def __repr__(self):
        return f"Archive(text={self.text!r}, number={self.number!r})"

    @property
    def archive_text(self):
        return self._archive_text

    @property
    def archive_number(self):
        return self._archive_number



archive1 = Archive("Запись 1", 42)
print(archive1)
archive2 = Archive("Запись 2", 3.14)
print(archive2)
archive3 = Archive("Запись 3", 8)
print(archive3)




