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

def checking_that_arg_is(pre, error_msg):
    def wrapper(func):
        def inner(arg):
            if not pre(arg):
                raise ValueError('Value too low!')
            return func(arg)
        return inner
    return wrapper

def greater_than(value):
    def predicate(arg):
        return arg > value
    return predicate

def in_(*values):
    def predicate(arg):
        return arg in values
    return predicate

def not_(other_predicate):
    def predicate(arg):
        return not other_predicate(arg)
    return predicate

@checking_that_arg_is(greater_than(0), 'Non-positive!')
@checking_that_arg_is(not_(in_(5, 15, 42)), 'Bad value!')
def foo(arg):
    return arg
print('/' + '-' * 80 + '/\n\n')
# foo(0)
# foo(5)
print(foo(6))
from functools import wraps
print('/' + '-' * 80 + '/\n\n')
def add_one1(arg):
    '''
    add one to argument.
    argument should a number
    '''
    return arg + 1
print(add_one1)
print(help(add_one1))

def wrapped(func):
    def inner(arg):
        return func(arg)
    return inner

add_one1 = wrapped(add_one1)
print(add_one1)
help(add_one1)

def wrapped_n(func):
    @wraps(func)
    def inner(arg):
        return func(arg)
    return inner

def foo1(_):
    '''Bar.'''
    return 42

foo1 = wrapped_n(foo1)
print(foo1)
help(foo1)

print(foo1.__doc__)