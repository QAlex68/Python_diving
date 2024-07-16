# Напиши программу на python
# В текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых слов.
# Не учитывать знаки препинания и регистр символов.
# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф)
# считать двумя словами.
# Цифры за слова не считаем.
# Отсортируйте о убыванию значения количества повторяющихся слов. Слова выведите в обратном алфавитном порядке.
#
# Входные данные:
# text = 'This is a sample text without repeating words.'
#
# Ожидаемый ответ:
# [('words', 1), ('without', 1), ('this', 1), ('text', 1), ('sample', 1), ('repeating', 1), ('is', 1), ('a', 1)]
#
# Входные данные:
# text = 'Hello world. Hello Python. Hello again.'
#
# Ожидаемый ответ:
# [('hello', 3), ('world', 1), ('python', 1), ('again', 1)]




text = 'This is a sample text without repeating words.'


# # Функция для подсчета количества встречаемых слов и возвращения 10 самых частых слов
# def count_most_common_words(text):
#     # Удаляем знаки препинания и приводим текст к нижнему регистру
#     text = text.replace('.', '').replace(',', '').replace('?', '').replace('!', '').lower()
#
#     # Разбиваем текст на слова
#     words_list = text.split()
#
#     # Создаем словарь для подсчета количества повторений каждого слова
#     word_count = {}
#     for word in words_list:
#         if word.isdigit():
#             continue
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
#
#     # Сортируем слова по убыванию по количеству повторений
#     sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
#
#     # Возвращаем 10 самых часто встречающихся слов, сортированных по убыванию и по алфавиту
#     return sorted(sorted_words[:10], key=lambda x: (-x[1], x[0]), reverse=True)


# Примеры входных данных
# text1 = 'this is a sample text without repeating words.'
# text2 = 'hello world. hello python. hello again.'

# # Вывод результатов
# print(count_most_common_words(text1))
# print(count_most_common_words(text2))

text1 = 'this is a sample text without repeating words.'
text2 = 'hello world. hello python. hello again.'

def count_words(text):
    word_count = {}
    text = text.replace('.', '').replace(',', '').replace('?', '').replace('!', '').replace("'", ' ').lower().split()


    for word in text:
        word = ''.join(filter(str.isalpha, word))
        if word.isalpha():
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    sorted_words = sorted(word_count.items(), key=lambda x: (x[1], x[0]), reverse=True)

    return sorted_words

# sorted_data = sorted(data, key=lambda x: (-x[1], x[0],), reverse=True)


result1 = count_words(text1)[:10]
print(result1)
result2 = count_words(text2)[:10]
print(result2)

