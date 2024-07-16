# Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.
# Создайте файл __init__.py и запишите в него все функции:
# save_to_json,
# find_roots,
# generate_csv_file.

with open('__init__.py', 'w', encoding='utf-8') as f:
    f.write('''
    def save_to_json(func):
        pass    
    def find_roots(a, b, c):
        pass
    def generate_csv_file(file_name, rows):
        pass''')