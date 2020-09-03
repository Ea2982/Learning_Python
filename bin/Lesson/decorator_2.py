from functools import wraps

def memoized(limit):
    def wraper(func):
        '''wraper'''
        dct = dict()
        lst = list()
        @wraper(func)
        def inner(x):
            '''inner'''
            m_res = dct.get(x)
            if m_res is None:
                m_res = func(x)
                dct[x] = m_res
                lst.append(x)
                if len(lst) > limit:
                    tmp = lst.pop(0)
                    dct.pop(tmp)
            print(dct)
            print(lst)

            return m_res
        return inner
    return wraper

@memoized(3)
def f(x):
    print('Calculating...')
    return x * 10

print(f(1))
print(f(1))
print(f(2))
print(f(3))
print(f(4))
print(f(1))
