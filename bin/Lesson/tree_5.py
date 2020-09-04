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

def downcase_file_names(node):
    name = get_name(node).lower()
    meta = copy.deepcopy(get_meta(node))
    if is_file(node):
        return mkfile(name, meta)
    children = get_children(node)
    # new_children = list(map(lambda child: downcase_file_names(child), children))
    new_children = list()
    ##########################
    for child in children:
        new_children.append(downcase_file_names(child))
    ##########################
    tree = mkdir(name, new_children, meta)
    return tree

tree = mkdir('/', [
    mkdir('eTc', [
        mkdir('NgiNx', [], {'size': 4000}),
        mkdir(
            'CONSUL',
            [mkfile('config.JSON', {'uid': 0})],
        ),
    ]),
mkfile('HOSTS'),
])
new_tree = downcase_file_names(tree)
new_file = get_children(new_tree)[1]
print(get_name(new_file) == 'hosts')
