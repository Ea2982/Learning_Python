'''Functions'''

def fn(*arg):
    print(type(arg))
    print(arg)
fn()
fn(1, 'a', None, False)

def greet(name, *arg):
    print((name,) + arg)
    for n in (name,) + arg:
        print(f'Hello {n}!')

greet('Tom', 'Ann')
names = ['Tom', 'Ann']
greet(*names)