expected = {
        'name': 'python-package',
        'meta': {'hidden': True},
        'type': 'directory',
        'children': [
            {'name': 'Makefile', 'meta': {}, 'type': 'file'},
            {'name': 'README.md', 'meta': {}, 'type': 'file'},
            {'name': 'dist', 'meta': {}, 'type': 'directory', 'children': []},
            {
                'name': 'tests',
                'meta': {},
                'type': 'directory',
                'children':
                    [{'name': 'test_solution.py', 'meta': {}, 'type': 'file'}],
            },
            {'name': 'pyproject.toml', 'meta': {}, 'type': 'file'},
            {
                'name': '.venv',
                'meta': {'owner': 'root', 'hidden': False},
                'type': 'directory',
                'children': [{
                    'name': 'lib',
                    'meta': {},
                    'type': 'directory',
                    'children': [{
                        'name': 'python3.6',
                        'meta': {},
                        'type': 'directory',
                        'children': [{
                            'name': 'site-packages',
                            'meta': {},
                            'type': 'directory',
                            'children': [{
                                'name': 'hexlet-python-package.egg-link',
                                'meta': {},
                                'type': 'file',
                            }],
                        }],
                    }],
                }],
            },
        ],
    }