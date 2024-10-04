import os
import time

# Путь к каталогу
directory = 'D:\PROJECTS\pythonProjects\module_7'

# Обход каталога
for dirpath, dirnames, filenames in os.walk(directory):
    print(f'Текущий каталог: {dirpath}')

    if dirnames:
        print('Подкаталоги:')
        for dirname in dirnames:
            print(f' {dirname}')

            full_dir_path = os.path.join(dirpath, dirname)
            print(f' {full_dir_path}')

    if filenames:
        print('Файлы')
        for filename in filenames:
            print(f' {filename}')

            # Получение полного пути к файлу
            full_file_path = os.path.join(dirpath, filename)
            print(f' {full_file_path}')

            # Получение времени последнего изменения файла
            modification_time = os.path.getmtime(full_file_path)
            readable_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modification_time))
            print(f' {full_file_path} - последнее изменение: {readable_time}')

            # Получение размера файла
            file_size = os.path.getsize(full_file_path)
            print(f' {full_file_path} - размер: {file_size} байт')

            # Получение родительской директории
            parent_directory = os.path.dirname(full_file_path)
            print(f' Родительская директория: {parent_directory}')

    print() # Пустая строка для разделения блоков вывода

# print('Текущая директория: ', os.getcwd())
# if os.path.exists('second'):
#     os.chdir('second')
# else:
#     os.mkdir('second')
#     os.chdir('second')
# print('Текущая директория: ', os.getcwd())
# print(os.listdir())
# os.chdir(r'D:\PROJECTS\pythonProjects\module_7')
# print('Текущая директория: ', os.getcwd())
# print(os.listdir())
# file = [f for f in os.listdir() if os.path.isfile(f)]
# dirs = [d for d in os.listdir() if os.path.isdir(d)]
# print(dirs)
# print(file)
# print(os.stat(file[3]).st_size)
# os.system('pip install random2')
