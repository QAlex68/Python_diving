# Строки
text = 'Hello world!'
print(text[6])
print(text[3:7])

new_txt = text.replace('l', 'L', 2)
print(text, new_txt, sep='\n')

# Методы count, index, find

text = 'Hello world!'
print(text.count('l'))
print(text.index('l'))
print(text.find('l'))
print(text.find('z'))

# Реверс строк

text = 'Hello world!'
print(text[::-1])

# Форматирование через %

name = 'Alex'
age = 12
text = 'Меня зовут %s и мне %d лет' % (name, age)
print(text)


# Метод format

name = 'Alex'
age = 12
text = 'Меня зовут {} и мне {} лет'.format(name, age)
print(text)


# f-строка

name = 'Alex'
age = 12
text = f'Меня зовут {name} и мне {age} лет'
print(text)

# Уточнение формата
pi = 3.1415
print(f'Число Пи с точностью два знака: {pi:.2f}')
data = [3254, 4364314532, 43465474, 2342, 462256, 1747]
for item in data:
    print(f'{item:>10}')
num = 2 * pi * data[1]
print(f'{num = :_}')


# Метод split

link = 'https://habr.com/ru/users/dzhoker1/posts/'
urls = link.split('/')
print(urls)
a, b, c = input('Введите 3 числа через пробел: ').split()
print(c, b, a)


# Метод join
data = ['https:', '', 'habr.com', 'ru', 'users', 'dzhoker1', 'posts']
url = '/'.join(data)
print(url)


# Методы upper, lower, title, capitalize

text = 'однажды в СТУДЁНУЮ зИмнЮЮ ПоРУ'
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())


# Методы startswith и endswith

text = 'Однажды в студёную зимнюю пору'
print(text.startswith('Однажды'))
print(text.endswith('зимнюю', 0, -5))






