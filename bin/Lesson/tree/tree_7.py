'''Агрегация 2
Попрактикуемся ещё с одним вариантом агрегации данных на файловых системах. Напишем функцию, которая принимает на вход директорию и возвращает список директорий первого уровня вложенности и количество файлов внутри каждой из них, включая все поддиректории.
'''
#>>> from hexlet import fs
'''
>>> tree = fs.mkdir('/', [
...     fs.mkdir('etc', [
...         fs.mkdir('apache'),
...         fs.mkdir('nginx', [
...             fs.mkfile('nginx.conf'),
...         ]),
...     ]),
...     fs.mkdir('consul', [
...         fs.mkfile('config.json'),
...         fs.mkfile('file.tmp'),
...         fs.mkdir('data'),
...     ]),
...     fs.mkfile('hosts'),
...     fs.mkfile('resolve'),
... ])
>>> 
>>> print(get_subdirectories_info(tree))''' #[('etc', 1), ('consul', 2)]#
'''
https://repl.it/@hexlet/python-trees-search-get-subdirectories-info

Внутри себя эта задача распадается на две:

Подсчёт количества файлов внутри директории
Вызов функции подсчёта файлов на каждой из поддиректорий
Начнём с подсчёта количества файлов. Это классическая задача на агрегацию:

def get_files_count(node):
    if fs.is_file(node):
        return 1  
    children = fs.get_children(node)
    descendant_counts = list(map(get_files_count, children))
    return sum(descendant_counts)
Следующий шаг заключается в том, чтобы извлечь всех детей из исходного узла и к каждому из них применить подсчёт:

def get_subdirectories_info(node):
    children = fs.get_children(node)
    # Нас интересуют только директории
    filtered = filter(fs.is_directory, children)
    # Запускаем подсчёт для каждой директории
    result = map(
        lambda child: (fs.get_name(child), get_files_count(child)),
        filtered,
    )
    return list(result)
    

То есть мы обратились к детям напрямую сначала отфильтровав их, а затем выполнили отображение на необходимый массив, содержащий для каждой директории имя и количество файлов в нем.




