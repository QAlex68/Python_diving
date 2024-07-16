# Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.
# На языке python cоздайте файл __init__.py и запишите в него функцию rename_files


with open('__init__.py', 'w', encoding='utf-8') as f:
    f.write('''
        def rename_files(desired_name, num_digits, source_ext, target_ext):
    file_list = os.listdir("test_folder")
    count = 1
    for file_name in file_list:
        if file_name.endswith("." + source_ext):
            file_prefix = file_name[3:7]  # Taking characters from 3 to 6 of the original file name
            if desired_name:
                new_name = desired_name + str(count).zfill(num_digits) + "." + target_ext
            else:
                new_name = file_prefix + str(count).zfill(num_digits) + "." + target_ext
            original_path = os.path.join("test_folder", file_name)
            new_path = os.path.join("test_folder", new_name)
            os.rename(original_path, new_path)
            count += 1''')