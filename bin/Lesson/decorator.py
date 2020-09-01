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


def memoized(func):
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

@memoized
def f(x):
    print('Calculating...')
    return x * 10

print(f(1))
# print(f(2))
print(f(1))
# print(f(3))
# print(f(2))