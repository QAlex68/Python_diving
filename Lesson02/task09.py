LIMIT = 120
ATTENTION = 'Внимание!'
name = input('Твоё имя? ')
age = int(input('Твой возраст? '))
text = ATTENTION + ' Хоть тебе и осталось ' + str(100 - age) +\
" до ста лет, но длинна строки не должна превышать " +\
str(LIMIT) + ' символов.'
print(text)


empty_str = ''
en_str = 'Text'
ru_str = 'Текст'
unicode_str = '😀😍😉🙃'
print(empty_str.__sizeof__())
print(en_str.__sizeof__())
print(ru_str.__sizeof__())
print(unicode_str.__sizeof__())