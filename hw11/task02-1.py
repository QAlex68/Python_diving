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

# Пример использования:
archive1 = Archive("Запись 1", 42)
print(archive1)  # Text is Запись 1 and number is 42. Also ['Запись 1'] and [42]

archive2 = Archive("Запись 2", 3.14)
print(archive2)  # Text is Запись 2 and number is 3.14. Also ['Запись 1', 'Запись 2'] and [42, 3.14]



