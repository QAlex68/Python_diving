# Задание №5
# Доработаем задачи 3 и 4. Создайте класс проекта, который
# имеет следующие методы:
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя. Для
# проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение
# доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# добавление пользователя. Если уровень пользователя
# меньше, чем ваш уровень, вызывайте исключение уровня
# доступа.

# Задание №6
# Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках.
# Передавайте необходимые данные из основного кода проекта.

import json


class UserException(Exception):
    pass


class LevelError(UserException):
    def __init__(self, user, new_user):
        self.user = user
        self.new_user = new_user

    def __str__(self):
        return (f'Ошибка уровня: Вы вошли как - {self.user.name} и ограничены уровнем {self.user.user_level}.\n'
                f' Нельзя добавить пользователя - {self.new_user.name} с уровнем {self.new_user.user_level}!!!\n'
                f'Наказание РАСТРЕЛЛ!!')


class AccessError(UserException):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return f'Ошибка доступа: Отсутствует пользователь с именем {self.name} и идентификатором {self.id}!!'


class User:
    def __init__(self, name: str, user_id: str, user_level: str):
        self.name = name
        self.user_id = user_id
        self.user_level = user_level

    def __eq__(self, other):
        return self.user_id == other.user_id and self.name == other.name

    def __hash__(self) -> int:
        return hash((self.name, self.user_id))

    def __str__(self):
        return f'{self.name} {self.user_id} {self.user_level}'

    def __repr__(self):
        return f'User({self.name}, {self.user_id}, {self.user_level})'


class Project:
    def __init__(self):
        self.users = set()
        self.user = None

    def login(self, name, id):
        login_user = User(name, id, '0')
        if login_user not in self.users:
            raise AccessError(name, id)

        for cur_user in self.users:
            if login_user == cur_user:
                self.user = cur_user
                return self.user

    def add_user(self, name, id, level):
        new_user = User(name, id, level)
        if int(self.user.user_level) > int(level):
            raise LevelError(self.user, new_user)
        # new_user = User(name, id, level)
        self.users.add(new_user)
        return new_user

    def load_json(self, filename):
        with open(filename, 'r', encoding='utf-8') as f_read:
            data = json.load(f_read)

        for level, users_dict in data.items():
            for id, name in users_dict.items():
                self.users.add(User(name, id, level))
        return self.users


if __name__ == '__main__':
    file = 'users.json'
    project1 = Project()
    project1.load_json(file)
    print(project1.login('Dasha', '3'))
    print(project1.add_user('new_user', '10', '3'))

