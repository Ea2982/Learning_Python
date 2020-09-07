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
def dfg(node):
    print(get_name(node))
    if is_file(node):
        return

    children = get_children(node)
    list(map(dfg, children))

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
print('/' + '-' * 200 + '/')
print(tree)
print(downcase_file_names(tree))
print(tree)
# new_tree = downcase_file_names(tree)
# print(tree)
# new_file = get_children(new_tree)[1]
# print(new_tree)
# print(get_name(new_file) == 'hosts')
print('/' + '-' * 200 + '/')
def test_be_immutable():
    tree = mkdir('/', [
        mkdir('eTc', [
            mkdir('NgiNx', [], {'size': 4000}),
            mkdir(
                'CONSUL',
                [mkfile('config.JSON', {'uid': 0})],
            ),
        ]),
        mkfile('hOsts'),
    ])
    original = copy.deepcopy(tree)
    downcase_file_names(tree)
    print(tree == original)
    print(original)
    print(tree)
    # dfg(original)
    # dfg(downcase_file_nam/es(tree))
# test_be_immutable()
print('/' + '-' * 200 + '/')


def test_downcase_file_names():
    tree = mkdir('/', [
        mkdir('eTc', [
            mkdir('NgiNx', [], {'size': 4000}),
            mkdir(
                'CONSUL',
                [mkfile('config.JSON', {'uid': 0})],
            ),
        ]),
        mkfile('hOsts'),
    ])

    expected = {
        'name': '/',
        'meta': {},
        'type': 'directory',
        'children': [
            {
                'name': 'eTc',
                'meta': {},
                'type': 'directory',
                'children': [
                    {
                        'name': 'NgiNx',
                        'meta': {'size': 4000},
                        'type': 'directory',
                        'children': [],
                    },
                    {
                        'name': 'CONSUL',
                        'meta': {},
                        'type': 'directory',
                        'children': [
                            {
                                'name': 'config.json',
                                'type': 'file',
                                'meta': {'uid': 0},
                            },
                        ],
                    },
                ],
            },

        ],
    }
    print(expected)
    print(downcase_file_names(tree))
    print(downcase_file_names(tree) == expected)

# test_downcase_file_names()
print('/' + '-' * 200 + '/')