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

def f1(x, y):
    print(x, y)
f1(x=1, y=2)
f1(1, 2)
f1(1, y=2)
#f1(y=2, 1) error point
#f1(x=1, 2) error point


print('|-------------------------------------------------------------------|\n')

def rgb(red=0, green=0, blue=0):
    return 'rgb({}, {}, {})'.format(red, green, blue)


# BEGIN (write your solution here)
def get_colors(*args):
    colors = {'red': rgb(red=255), 'green': rgb(green=255), 'blue': rgb(blue=255)}
    return colors

    # return {
    #     'red': rgb(red=255),
    #     'green': rgb(green=255),
    #     'blue': rgb(blue=255),
    # }


colors = get_colors()
set(colors.keys()) == {'red', 'green', 'blue'}
print(colors['red'])
print(colors['blue'])
print(colors['green'])

for (i, v) in colors.items():
    print(f'i: {i} - v: {type(v)}')


print('|-------------------------------------------------------------------|\n')

def g(**kwargs):
    return kwargs
print(g(x=1, y=2, z=None))
print(type(g(x=1, y=2, z=None)))

def f1(x, y, *args, kx=None, ky=42, **kwargs):
    return (x, y, args, kx, ky, kwargs)

print(f1(1, 2, 3, 4, kx='a', ky='b', kz='c'))
print(type(f1(1, 2, 3, 4, kx='a', ky='b', kz='c')))

tmp = (f1(1, 2, 3, 4, kx='a', ky='b', kz='c'))
for i in tmp:
    print(f'i: {i} - type(i): {type(i)}')

def coords(x, y):
    print(type(x))
    print(type(y))
    return (x, y)
print(coords(x=1, **{'y': 2}))
print(type(coords(x=1, **{'y': 2})))

positional = (2, 3)
named = dict(ky='b', kz='c')
print(f1(1, *positional, 4, kx='a' , **named))

def greet1(*, who):
    print(f'Hello, {who}')

greet1(who='Bob')
# greet1('Bob') -> Error
greet1(**dict(who='Bob'))
# greet1({'who': 'Bob'}) -> Error
greet1(**{'who': 'Bob'})

def updated(d, **kwargs):
    res = d
    print(f'res: {res}')
    res = kwargs.copy()
    print(f'res: {res}')
    # for key, valuse in kwargs.items():
    #     res[key] = kwargs[key]
    return res
d = {'a': 1, 'b': False}
print(updated(d, a=2, b=True, c=None))