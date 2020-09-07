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
'''
#То есть мы обратились к детям напрямую сначала отфильтровав их, а затем выполнили отображение на необходимый массив, содержащий для каждой директории имя и количество файлов в нем.



import copy


def mkfile(name, meta={}):
    '''Return file node.'''
    return {
        'name': name,
        'meta': meta,
        'type': 'file',
    }


def mkdir(name, children=[], meta={}):
    '''Return directory node.'''
    return {
        'name': name,
        'children': children,
        'meta': meta,
        'type': 'directory',
    }


def is_directory(node):
    '''Check is node a directory.'''
    return node.get('type') == 'directory'


def is_file(node):
    '''Check is node a file.'''
    return node.get('type') == 'file'


def get_children(directory):
    '''Return children of node.'''
    return directory.get('children')

def get_meta(node):
    '''Return meta of node.'''
    return node.get('meta')


def get_name(node):
    '''Return name of node.'''
    return node.get('name')


def flatten(tree):
    result = []

    def walk(subtree):
        for item in subtree:
            if isinstance(item, list):
                walk(item)
            else:
                result.append(item)

    walk(tree)
    return result
def du(tree):
    return

tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('nginx.conf', {'size': 800}),
        ]),
        mkdir('consul', [
            mkfile('.config.json', {'size': 1200}),
            mkfile('data', {'size': 8200}),
            mkfile('raft', {'size': 80}),
        ]),
    ]),
    mkfile('hosts', {'size': 3500}),
    mkfile('resolve', {'size': 1000}),
])
print(du(tree))
print(du(tree) == [('etc', 10280), ('hosts', 3500), ('resolve', 1000)])

