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

tree = mkdir('/', [
    mkdir('etc', [
        mkfile('bashrc'),
        mkfile('consul.cfg'),
    ]),
    mkfile('hexletrc'),
    mkdir('bin', [
        mkfile('ls'),
        mkfile('cat'),
    ]),
])


# В реализации используем рекурсивный процесс,
# чтобы добраться до самого дна дерева.
def get_nodes_count(node):
    if is_file(node):
        # Возвращаем 1 для учёта текущего файла
        return 1
    # Если узел — директория, получаем его детей
    children = get_children(node)
    # Самая сложная часть
    # Считаем количество потомков для каждого из детей,
    # вызывая рекурсивно нашу функцию get_nodes_count
    descendant_counts = list(map(get_nodes_count, children))
    # Возвращаем 1 (текущая директория) + общее количество потомков
    return 1 + sum(descendant_counts)


print(get_nodes_count(tree))


>>> from hexlet.fs import mkdir, mkfile
>>> from solution import get_hidden_files_count

>>> tree = mkdir('/', [
...     mkdir('etc', [
...         mkdir('apache'),
...         mkdir('nginx', [
...             mkfile('.nginx.conf', {'size': 800}),
...         ]),
...         mkdir('.consul', [
...             mkfile('.config.json', {'size': 1200}),
...             mkfile('data', {'size': 8200}),
...             mkfile('raft', {'size': 80}),
...         ]),
...      ]),
...      mkfile('.hosts', {'size': 3500}),
...      mkfile('resolve', {'size': 1000}),
... ])
>>> get_hidden_files_count(tree)
3
>>>