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

# tree = mkdir('etc',[
#         mkdir('bashrc'),
#         mkdir('consul', [
#             mkfile('config.json')
#               ])
#     ]
# )
#
# print(tree)

def generator():
    tree = mkdir('python-package', [
        mkfile('Makefile'),
        mkfile('README.md'),
        mkdir('dist'),
        mkdir('tests', [
            mkfile('test_solution.py')
        ]),
        mkfile('pyproject.toml'),
        mkdir('.venv', [
            mkdir('lib', [
                mkdir('python3.6', [
                    mkdir('site-packages', [
                        mkfile('hexlet-python-package.egg-link')
                    ])
                ])
            ])
        ], {'owner': 'root', 'hidden': False})


    ], {'hidden': True})
    return tree

print(generator())