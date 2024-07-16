# Напиши на python функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:
# a. принимать параметр желаемое конечное имя файлов desired_name. При переименовании в конце имени добавляется
# порядковый номер.
# b. принимать параметр количество цифр в порядковом номере num_digits.
# c. принимать параметр расширение исходного файла source_ext . Переименование должно работать только для этих файлов
# внутри каталога.
# d. принимать параметр расширение конечного файла target_ext.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из
# исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# f. Папка test_folder доступна из текущей директории.
# Пример использования.
# На входе:
# rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")
# На выходе:
# new_file_008.doc, test.doc, new_file_004.doc, new_file_005.doc, new_file_007.doc, new_file_001.doc, new_file_006.doc,
# new_file_003.doc, new_file_002.doc, new_file_009.doc, new_file_010.doc


import os


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
            count += 1


# Example usage
rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")
