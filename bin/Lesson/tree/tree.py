import itertools
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



def remove_first_level(tree):
    children = filter(lambda item: isinstance(item, list), tree)
    print(list(children))
    return list(itertools.chain(*children))


def remove_first_level_old(tree):
    level = 0
    lst = list()
    for i in tree:
        if type(tree) == type(i):
            for j in i:
                lst.append(j)
    return lst

tree = [
    3,
    [5, 3],
    [[2]]
]
print(tree)
print(remove_first_level(tree))

tree1 = [
    [5],
    1,
    [3, 4]
]
print(tree1)
print(remove_first_level(tree1))
#
# tree3 = [1, 2, [3, 5], [[4, 3], 2]]
# print(tree3)
# print(remove_first_level(tree3))
#
# tree = (1, 2, (3, 5), ((4, 3), 2))
# print(tree)
# print(remove_first_level(tree))
#
# tree = (1, 2, ({[3, 5]}), ((4, 3), [2]))
# print(tree)
# print(remove_first_level(tree))

print('/' + '-' * 200 + '/\n\n')

tree = mkdir('/', [mkfile('hexlet.log')], {'hidden': True})
print(get_name(tree))
print(get_meta(tree))
print(get_meta(tree).get('hidden'))
[file] = get_children(tree)
print(get_name(file))
print(get_meta(file).get('unknown'))
print('/' + '-' * 200 + '/')
print(is_directory(tree))
print(is_file(tree))
[file] = get_children(tree)
print(is_file(file))
print(is_directory(file))
print('/' + '-' * 200 + '/')
file = mkfile('one', {'size': 35})
print(file)
new_meta = copy.deepcopy(get_meta(file))
new_file = mkfile('new_file', new_meta)
print(new_file)
print(file)
print('/' + '-' * 200 + '/')
tree =mkdir('/',[
            mkfile('one'),
            mkfile('two'),
            mkfile('three')
            ])
print(tree)
children =get_children(tree)
print(children)
new_meta = copy.deepcopy(get_meta(tree))
print(new_meta)
new_children = children[:]
print(new_children)
new_children.reverse()
print(new_children)
tree2 = mkdir(get_name(tree), new_children, new_meta)
print(tree2)
print(list(map(lambda node: get_name(node), tree2.get('children'))))
print('/' + '-' * 200 + '/')
tree =mkdir('/', [
    mkfile('oNe'),
    mkfile('Two'),
    mkfile('THREE'),
    mkdir('four', [
        mkfile('one')
    ])
])
print(tree)
def to_lower(node):
    name = get_name(node)
    print(name)
    new_meta = copy.deepcopy(get_meta(node))
    print(new_meta)
    if is_directory(node):
        return mkdir(name.lower(), get_children(node), new_meta)
    return mkfile(name.lower(), new_meta)

children = get_children(tree)
print(children)
new_children = list(map(to_lower, children))
print(new_children)
new_meta = copy.deepcopy(get_meta(tree))
print(new_meta)
tree2 = mkdir(get_name(tree), new_children, new_meta)
print(tree2)
print(list(map(lambda node: get_name(node), tree2.get('children'))))

