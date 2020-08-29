'''Functions'''

def fn(*arg):
    print(type(arg))
    print(arg)
fn()
fn(1, 'a', None, False)

def greet(*arg):
    lst = list(arg)
    hi = ' and '.join(lst)
    print(f'Hello, {hi}')

greet('Tom', 'Ann')
names = ['Tom', 'Ann']
greet(*names)

