# В организации есть два типа людей: сотрудники и обычные люди.
# Каждый человек (и сотрудник, и обычный) имеет следующие атрибуты:
# Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка, не пустая) Возраст (целое положительное число)
# Сотрудники имеют также уникальный идентификационный номер (ID), который должен быть шестизначным
# положительным целым числом.
# Ваша задача:
# Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях
# (Фамилия, Имя, Отчество, Возраст). Класс должен проверять валидность входных данных и генерировать исключения
# InvalidNameError и InvalidAgeError, если данные неверные.
# Создать класс Employee, который будет наследовать класс Person и добавлять уникальный идентификационный номер (ID).
# Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.
# Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.
# Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника на основе суммы цифр в его ID
# (по остатку от деления на 7).
# Создать несколько объектов класса Person и Employee с разными данными и проверить, что исключения работают корректно
# при передаче неверных данных.

class InvalidNameError(ValueError):
    pass


class InvalidAgeError(ValueError):
    pass


class InvalidIdError(ValueError):
    pass


class Person:
    def __init__(self, last_name: str, first_name: str, middle_name: str, age: int):
        if not all(isinstance(name, str) and name for name in [last_name, first_name, middle_name]):
            raise InvalidNameError("Invalid name: . Name should be a non-empty string.")
        if not (isinstance(age, int) and age > 0):
            raise InvalidAgeError(f"Invalid age: {age}. Age should be a positive integer.")

        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.age = age

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}, возраст: {self.age}"


class Employee(Person):
    def __init__(self, last_name: str, first_name: str, middle_name: str, age: int, employee_id: int):
        super().__init__(last_name, first_name, middle_name, age)
        if not (isinstance(employee_id, int) and 100000 <= employee_id <= 999999):
            raise InvalidIdError(
                f"Invalid id: {employee_id}. Id should be a 6-digit positive integer between 100000 and 999999.")

        self.employee_id = employee_id

    def get_level(self):
        return sum(map(int, str(self.employee_id))) % 7

    def __str__(self):
        return f"{super().__str__()}, ID: {self.employee_id}, уровень: {self.get_level()}"


# Примеры использования и тестирование
person = Person("Alice", "Smith", "Johnson", 25)
print(person.get_age())
