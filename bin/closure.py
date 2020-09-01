'''Closure - Замыкание'''

G = 10
def make_closure():
    a = 1
    b = 2
    def inner(x):
        return x + G + a
    return inner

print(make_closure()(100))

def make_closure1():
    y = 1
    def inner(x):
        return x + y
    y = 42
    return inner

print(make_closure1()(100))

printers = []

for i in range(10):
    def make_printer(arg):
        def printer():
            return arg
        return printer
    p = make_printer(i)
    printers.append(p)

print(printers[0]())
print(printers[5]())
print(printers[9]())

name = 'Bob'

def make_closure2():
    name = 'Alice'

    def inner():
        print(f'Hello, {name}')

    name = 'Grace'

    return inner

name = 'Thomas'

print(make_closure2()())

def f():
    x = 1
    def g():
        return x
    x = 2

    def h():
        return x

    x = 3
    return g() == h(), g() + h()

print(f())


def greet(name, surname):
    return 'Hello, {name} {surname}!'.format(name=name, surname=surname)
def partial_apply(func, args1):
    def inner(args2):
        return func(args1, args2)
    return inner


f = partial_apply(greet, 'Dorian')

print(f('Grey')) #'Hello, Dorian Grey!'

def greet(name, surname):
    return 'Hello, {name} {surname}!'.format(name=name, surname=surname)

def flip(func):
    def inner(args1, args2):
        return func(args1, args2)

    return inner


f = flip(greet)
print(f('Christian', 'Teodor')) #'Hello, Teodor Christian!')
