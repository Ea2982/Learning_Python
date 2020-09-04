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
    tree = mkdir(
        'python-package',
        meta={'hidden': True},
        children=[
            mkfile('Makefile'),
            mkfile('README.md'),
            mkdir('dist'),
            mkdir('tests', [
                mkfile('test_solution.py')
            ]),
            mkfile('myproject.toml'),
            mkdir(
                '.venv',
                meta={'owner': 'root', 'hidden': False},
                children= [
                    mkdir(
                        'lib',
                        [
                            mkdir(
                                'python3.6',
                                [
                                    mkdir(
                                        'site-packages',
                                        [
                                            mkfile('hexlet-python-package.egg-link')
                                        ]
                                    )
                                ]
                            )
                        ]
                    )
                ]
            )
        ]
    )

    return tree
print(generator())

'''tree = mkdir('python-package', [
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




{'name': 'python-package', 
 'children': [
     {'name': 'Makefile', 'meta': {}, 'type': 'file'},
     {'name': 'README.md', 'meta': {}, 'type': 'file'}, 
     {'name': 'dist', 'children': [], 'meta': {}, 'type': 'directory'}, 
     {
         'name': 'tests',
         'children': 
             [{'name': 'test_solution.py', 'meta': {}, 'type': 'file'}], 
         'meta': {}, 
         'type': 'directory'
     }, 
     {'name': 'pyproject.toml', 'meta': {}, 'type': 'file'}, 
     {
         'name': '.venv', 
         'children': [{
             'name': 'lib', 
             'children': [{
                 'name': 'python3.6', 
                 'children': [{
                     'name': 'site-packages', 
                     'children': [{
                         'name': 'hexlet-python-package.egg-link', 
                         'meta': {}, 'type': 'file'}], 
                     'meta': {}, 'type': 'directory'}], 
                 'meta': {}, 'type': 'directory'}], 
             'meta': {}, 'type': 'directory'}], 
         'meta': {'owner': 'root', 'hidden': False}, 'type': 'directory'}], 
 'meta': {'hidden': True}, 'type': 'directory'}
    
'''