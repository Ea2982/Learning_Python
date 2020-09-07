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
        mkfile('consul.log')
    ]),
    mkfile('hexletrc'),
    mkdir('bin', [
        mkfile('ls'),
        mkfile('cat')
    ])
])

print(tree)
def dfg(node):
    print(get_name(node))
    if is_file(node):
        return

    children = get_children(node)
    list(map(dfg, children))
dfg(tree)
def change_owner(node, owner):
    name = get_name(node)
    # print(name)
    meta = copy.deepcopy(get_meta(node))
    # print(meta)
    meta['owner'] = owner
    if is_file(node):
        # print(name, meta)
        return mkfile(name, meta)
    children = get_children(node)
    # print(children)
    new_children = list(map(lambda child: change_owner(child, owner), children))
    # print(new_children)
    new_tree = mkdir(name, new_children, meta)
    # print(new_tree)
    return new_tree
print('/' + '-' * 200 + '/')
tree = change_owner(tree, 'Leonardo')
print('/' + '-' * 200 + '/')
# print(tree)
print(get_children(tree)[1])
# print(flatten(tree))