# Напиши программу на python
# Дан список повторяющихся элементов lst.
# Вернуть список с дублирующимися элементами которых в списке два. В результирующем списке не должно быть дубликатов.
# Пример
# На входе:
# lst = [1, 2, 3, 2, 4, 5, 4]
# На выходе:
# [2, 4]


lst = [1, 2, 3, 2, 4, 5, 4]


def find_duplicates(lst):
    seen = set()
    duplicates = set()

    for item in lst:
        if item in seen:
            duplicates.add(item)
        seen.add(item)

    return list(duplicates)


# Пример использования

result = find_duplicates(lst)
print(result)


