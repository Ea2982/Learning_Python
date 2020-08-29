'''Functions'''


def fn(*arg):
    print(type(arg))
    print(arg)


fn()
fn(1, 'a', None, False)


def greet(name, *arg):
    lst = list((name,) + arg)
    hi = 'Hello, ' + ' and '.join(lst) + '!'
    return hi


print(greet('Tom', 'Ann'))
print(greet('Bob'))

print('|-------------------------------------------------------------------|\n')

def bar(length, char1='-', char2='*'):
    return (char1 + char2) * length + char1

print(bar(5, '-', '*'))
print(bar(5))
print(bar(3, '.'))
print(bar(3, ':', '|'))
print(bar(3, char2='#'))
print(bar(char2='$', length=3))

def f(*args, x=None, y=None):
    print('args =', args, ', x =', x, ', y =', y)

f(*(1, 2), x='a', *[3, 4], y='b', *(5, 6))
#args = (1, 2, 3, 4, 5, 6), x = a, y = b
