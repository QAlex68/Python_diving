'''
Задание №4 Создайте вручную список с повторяющимися элементами.
Удалите из него все элементы, которые встречаются дважды.
'''

data = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42]
COUNT = 2
for item in set(data):
    if data.count(item) == COUNT:
        for _ in range(COUNT):
            data.remove(item)

print(data)

# 2

# new_list = [item for item in my_list if my_list.count(item) != 2]