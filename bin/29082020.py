'''Functions'''


def fn(*arg):
    print(type(arg))
    print(arg)


fn()
fn(1, 'a', None, False)


def greet(name, *arg):
    lst = list((name,) + arg)
    hi = 'Hello, ' + ' and '.join(lst)
    return hi


print(greet('Tom', 'Ann'))
names = ['Tom', 'Ann']
greet()
