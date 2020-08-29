'''Functions'''

def fn(*arg):
    print(type(arg))
    print(arg)
fn()
fn(1, 'a', None, False)

def greet(*arg):
    print(len(arg))
    if len(arg) == 0:
        return None
    lst = list(arg)
    print(len(lst))

    if len(lst) == 0:
        return
    hi = 'Hello, ' +  ' and '.join(lst)
    return hi

print(greet('Tom', 'Ann'))
names = ['Tom', 'Ann']
greet()

