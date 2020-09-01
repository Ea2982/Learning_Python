'''Декораторы'''

def printing(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'result = {result}')
        return result
    return inner

@printing
def add_one(x):
    return x + 1

# add_one = printing(add_one)
y = add_one(10)
print(y)


def memoized1(func):
    dct = dict()
    def inner(x):
        '''inner'''
        m_res = dct.get(x)
        if m_res is None:
            m_res = func(x)
            dct[x] = m_res
        print(dct)
        return m_res
    return inner
def memoized(func):
    def inner(x):
        if inner.dict.get(x):
            inner.dual += 1
            return inner.dict.get(x)
        result = func(x)
        inner.dict.update({x: result})
        inner.list.append(x)
        print(inner.dict)
        print(inner.list)
        print(inner.dual)
        return inner.dict.get(x)

    inner.dict = {}
    inner.list = []
    inner.dual = 0
    print(inner.dict)
    return inner

@memoized
def f(x):
    print('Calculating...')
    return x * 10

print(f(1))
print(f(1))
print(f(1))
print(f(1))
print(f(1))
print(f(1))
print(f(1))
print(f(10))
print(f(10))