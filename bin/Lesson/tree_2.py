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