# '''
# Аккумулятор
# В некоторых ситуациях во время обхода дерева нужна дополнительная информация, которая зависит от расположения узла. Её невозможно получить из описания самого узла, так как узел её не содержит. Эту информацию нужно собирать прямо во время обхода.
#
# К такой информации, например, относится полный путь до файла или глубина текущего узла. Конкретный узел не знает о том, где он находится. Расположение файла в файловой структуре определяется узлами, которые ведут к конкретному файлу.
#
# В этом уроке мы познакомимся с понятием аккумулятор, специальным параметром, который собирает нужные данные во время обхода дерева. Его введение усложняет код, но без него подобные задачи выполнить невозможно.
#
# Возьмём для примера такую задачу: найдём все пустые директории в нашей файловой системе. Сначала реализуем простую версию, затем усложним её и внедрим аккумулятор. Пример файловой системы ниже:
#
# from hexlet import fs
#
# tree = fs.mkdir('/', [
#     fs.mkdir('etc', [
#         fs.mkdir('apache'),
#         fs.mkdir('nginx', [
#             fs.mkfile('nginx.conf'),
#         ]),
#         fs.mkdir('consul', [
#             fs.mkfile('config.json'),
#             fs.mkdir('data'),
#         ]),
#     ]),
#     fs.mkdir('logs'),
#     fs.mkfile('hosts'),
# ])
# В этой структуре три пустых директории: /logs, /etc/apache и /etc/consul/data. Код, решающий эту задачу, выглядит так:
#
# def find_empty_dir_paths(tree):
#     name = fs.get_name(tree)
#     # Если узел — директория, получаем его детей
#     children = fs.get_children(tree)
#     # Если детей нет, то добавляем директорию
#     if len(children) == 0:
#         return name
#     # Фильтруем файлы, они нас не интересуют
#     dir_names = filter(lambda child: not fs.is_file(child), children)
#     # Ищем пустые директории внутри текущей
#     empty_dir_names = map(
#         lambda dir: find_empty_dir_paths(dir),
#         dir_names,
#       )
#     # flatten выправляет список, так что он становится плоским
#     return fs.flatten(empty_dir_names)
#
#
# print(find_empty_dir_paths(tree))
# # => ['apache', 'data', 'logs']
# https://repl.it/@hexlet/python-trees-search-find-empty-dirs
#
# Самое необычное в этой реализации функция flatten(). Зачем она нужна? Если оставить только map(), то результат может удивить:
#
# find_empty_dir_paths(tree)
# # [['apache', [], ['data']], 'logs']
# Такое происходит из-за возврата списка на каждом уровне вложенности. На выходе получается список списков, напоминающий по структуре исходное файловое дерево. Чтобы этого не происходило, нужно выправлять код с помощью flatten().
#
# Попробуем усложнить задачу. Найдём все пустые директории, но с максимальной глубиной поиска 2 уровня. То есть директории /logs и /etc/apache подходят под это условие, а вот /etc/consul/data — нет.
#
# Для начала нужно понять, откуда брать глубину. В деревьях глубина считается как количество рёбер от корня до нужного узла. Визуально её посчитать легко, а что насчёт кода? Глубину конкретного узла можно представить как глубину предыдущего узла плюс единица.
#
# #Следующий шаг – добавить переменную, которая передаётся при каждом рекурсивном вызове (проваливающимся в директорию). Эта переменная, в случае нашей задачи, содержит внутри себя текущую глубину. То есть на каждом уровне (внутри каждой директории) к ней добавляется единица. Такую переменную называют аккумулятором, так как она аккумулирует, то есть накапливает данные.
#
# Единственная проблема заключается в том, что у исходной функции find_empty_dir_paths() ровно один параметр – узел. С её помощью невозможно передавать глубину всем вложенным директориям и файлам. Поэтому придётся ввести внутреннюю функцию, которая сможет "пробрасывать" аккумулятор дальше по дереву:
# #
# def find_empty_dir_paths(tree):
#     # Внутренняя функция, которая может передавать аккумулятор
#     # Аккумулятором выступает depth, переменная, содержащая текущую глубину
#     def iter(node, depth):
#         name = fs.get_name(node)
#         children = fs.get_children(node)
#         # Если детей нет, то добавляем директорию
#         if len(children) == 0:
#             return name
#         # Если это второй уровень вложенности, и директория не пустая
#         # то не имеет смысла смотреть дальше
#         if depth == 2:
#             # Почему возвращается именно пустой список?
#             # Потому что снаружи выполняется flatten
#             # Он раскрывает пустые списки
#             return []
#         # Оставляем только директории
#         dir_paths = filter(fs.is_directory, children)
#         # Не забываем увеличивать глубину
#         output = map(
#             lambda child: iter(child, depth + 1),
#             dir_paths,
#           )
#         # Перед возвратом "выпрямляем" список
#         return fs.flatten(output)
#
#     # Начинаем с глубины 0
#     return iter(tree, 0)
#
#
# print(find_empty_dir_paths(tree))
# # => ['apache', 'logs']
# https://repl.it/@hexlet/python-trees-accumulator-find-empty-dirs-with-depth
#
# Можно пойти ещё дальше и позволить указывать максимальную глубину снаружи:
#
# def findEmptyDirPaths(tree, depth=2):
#     # ...
# Но возникает вопрос, а как сделать так, чтобы по умолчанию просматривалось всё дерево? Например, можно взять заведомо большое число и сделать его значением по умолчанию. Такой подход сработает, но это хак. Правильный способ сделать это – использовать в качестве значения по умолчанию бесконечность Infinity:
#
# def findEmptyDirPaths(tree, depth='inf'):
#     # ...
# '''
import copy, os


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

def find_files_by_name(tree, file_find):
    def iter(node, path):
        name = get_name(node)
        children = get_children(node)
        if is_file(node):
            if file_find in name:
                print("kjkjnknkj ", os.path.join(path, name))
                return os.path.join(path, name)
            else:
                return []

        path = os.path.join(path, name)
        print(os.path.normpath(path))
        result = map(
            lambda dir: iter(dir, path),
            children
        )
        # print(list(result))

        return flatten(result)
    return iter(tree, file_find)

tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('nginx.conf', {'size': 800}),
        ]),
        mkdir('consul', [
            mkfile('config.json'),
            mkfile('data'),
            mkfile('raft'),
        ]),
    ]),
    mkfile('hosts', {'size': 3500}),
    mkfile('resolve', {'size': 1000}),
])

print('|' * 200)
print(find_files_by_name(tree, 'co'))
# print(find_files_by_name(tree, 'co') == ['/etc/nginx/nginx.conf', '/etc/consul/config.json'])

# print('|' * 200)
# print(find_files_by_name(tree, 'co'))