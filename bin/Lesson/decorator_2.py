from functools import wraps


def memoized(limit):
    '''memoized'''

    def wrapper(func):
        '''wrapper'''

        dct = dict()
        lst = list()

        @wraps(func)
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
            # print(dct)
            # print(lst)

            return m_res

        return inner

    return wrapper


@memoized(3)
def f(x):
    print('Calculating...')
    return x * 10


args = list()


@memoized(3)
def inc(arg):
    args.append(arg)
    return arg + 1


print(args)

# print(f(1))
# print(f(1))
# print(f(2))
# print(f(3))
# print(f(4))
# print(f(1))
