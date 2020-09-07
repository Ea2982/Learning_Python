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

test_tree = {
    'name': 'my documents',
    'type': 'directory',
    'children': [
        {'name': 'avatar.jpg', 'meta': {'size': 50}, 'type': 'file'},
        {'name': 'photo.jpg', 'meta': {'size': 75}, 'type': 'file'},
    ],
    'meta': {'hide': False},
}
def to_two_size(node):
    if is_file(node) and get_name(node)[-3:] == 'jpg':
        meta = copy.deepcopy(get_meta(node))
        meta['size'] = meta['size'] / 2
        return mkfile(get_name(node), meta)
    return node

def compress_images(tree):
    children = list(map(to_two_size, get_children(tree)))
    tree2 = mkdir(get_name(tree), children, get_meta(tree))
    return tree2



tree = mkdir(
    'my documents',
    [
        mkfile('avatar.jpg', {'size': 100}),
        mkfile('photo.jpg', {'size': 150}),
    ],
    {'hide': False}
)
print(compress_images(tree))
print(compress_images(tree) == test_tree)






