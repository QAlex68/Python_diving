# Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.
# Создайте файл __init__.py и запишите в него все функции:
# get_dir_size,
# save_results_to_json,
# save_results_to_csv,
# save_results_to_pickle, traverse_directory.


with open('__init__.py', 'w', encoding='utf-8') as f:
    f.write('''
    def get_dir_size(directory):
    total_size = 0
    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            results.append({'path': path, 'type': 'file', 'size': size})
            total_size += size
        for name in dirs:
            path = os.path.join(root, name)
            dir_size = get_dir_size(path)
            results.append({'path': path, 'type': 'directory', 'size': dir_size})
            total_size += dir_size
    return total_size
    
    def save_results_to_json(results, file_name):
    with open(file_name, 'w') as file:
        json.dump(results, file, indent=4)
        
    def save_results_to_csv(results, file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['path', 'type', 'size'])
        writer.writeheader()
        for result in results:
            writer.writerow(result)
            
    def save_results_to_pickle(results, file_name):
    with open(file_name, 'wb') as file:
        pickle.dump(results, file)
        
        
    def traverse_directory(directory):
    results = []
    #
    # def get_dir_size(directory):
    #     total_size = 0
    #     for root, dirs, files in os.walk(directory):
    #         for name in files:
    #             path = os.path.join(root, name)
    #             size = os.path.getsize(path)
    #             results.append({'path': path, 'type': 'file', 'size': size})
    #             total_size += size
    #         for name in dirs:
    #             path = os.path.join(root, name)
    #             dir_size = get_dir_size(path)
    #             results.append({'path': path, 'type': 'directory', 'size': dir_size})
    #             total_size += dir_size
    #     return total_size

    total_size = get_dir_size(directory)

    return results, total_size''')