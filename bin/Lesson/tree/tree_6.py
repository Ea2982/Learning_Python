'''

Агрегация
Агрегация данных — наиболее важная операция при работе с деревьями. Подсчитать общее число файлов в директории, общий размер всех файлов, получить список всех файлов, найти все файлы по шаблону, всё это примеры агрегирования данных.

Ключевым моментом в агрегирующих операциях является накопление результата. Для данной задачи хорошо подходит обход дерева в глубину с использованием рекурсивного процесса, который подробно рассматривается в предыдущем уроке. С его помощью мы обходим все узлы дерева и собираем результат, начиная с самого нижнего уровня.

Рассмотрим агрегацию с использованием рекурсивного процесса на примере подсчёта общего количества узлов в дереве. То есть мы хотим узнать сколько всего файлов и директорий содержится в нашем файловом дереве.

# >>> from hexlet import fs
'''
'''
>>> tree = fs.mkdir('/', [
...     fs.mkdir('etc', [
...         fs.mkfile('bashrc'),
...         fs.mkfile('consul.cfg'),
...     ]),
...     fs.mkfile('hexletrc'),
...     fs.mkdir('bin', [
...         fs.mkfile('ls'),
...         fs.mkfile('cat'),
...     ]),
... ])
>>>
>>>
>>> # В реализации используем рекурсивный процесс,
... # чтобы добраться до самого дна дерева.
... def get_nodes_count(node):
...     if fs.is_file(node):
...         # Возвращаем 1 для учёта текущего файла
...         return 1
...     # Если узел — директория, получаем его детей
...     children = fs.get_children(node)
...     # Самая сложная часть
...     # Считаем количество потомков для каждого из детей,
...     # вызывая рекурсивно нашу функцию get_nodes_count
...     descendant_counts = list(map(get_nodes_count, children))
...     # Возвращаем 1 (текущая директория) + общее количество потомков
...     return 1 + sum(descendant_counts)
...
>>>
>>> get_nodes_count(tree)
8
https://repl.it/@hexlet/python-trees-aggregation-get-nodes-count

Кода здесь немного, но он довольно хитрый. Есть несколько ключевых моментов:

Функция проверяет тип узла. Если узел — это файл, тогда из функции возвращается единица.
В случае, если узел — директория, тогда получаем детей и для каждого ребёнка вновь вызываем нашу функцию. Затем повторяем алгоритм заново.
Вызов функции на каждом ребёнке возвращает свой собственный результат (количество его потомков). Эти результаты образуют массив с числами, которые нужно объединить.
В конце считается общее количество всех потомков узла + единица (текущий узел сам по себе).
Перед тем как двигаться дальше, с этим кодом нужно "поиграть". Это единственный способ разобраться с ним.


'''


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

def get_hidden_files_count(node):
    name = get_name(node)
    name.startswith()
    if is_file(node) and name[:1] == '.':
        print(name)
        return 1
    if is_file(node):
        return 0

    children = get_children(node)
    count = list(map(get_hidden_files_count, children))
    print(count)
    return sum(count)


tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('.nginx.conf', {'size': 800}),
        ]),
        mkdir('.consul', [
            mkfile('.config.json', {'size': 1200}),
            mkfile('data', {'size': 8200}),
            mkfile('raft', {'size': 80}),
        ]),
    ]),
    mkfile('.hosts', {'size': 3500}),
    mkfile('resolve', {'size': 1000}),
])
print(get_hidden_files_count(tree))
print(get_hidden_files_count(tree) == 3)
