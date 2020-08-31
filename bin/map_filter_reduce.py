'''Lessen map'''

def mmap(func, items):
    result = list()
    for item in items:
        result.append(func(item))
    return result
print(mmap(str, range(5)))
print(*(map(str, range(5))))


'''filter'''
def ffilter(pre, items):
    result = list()
    for item in items:
        if pre(item):
            result.append(item)
    return result

def is_odd(x):
    return x % 2

print(ffilter(is_odd, range(6)))
print(*(filter(is_odd, range(6))))

'''reduce'''
def rrduce(oper, init_value, items):
    acc = init_value
    for item in items:
        acc = oper(acc, item)
    return acc
from operator import add, mul

print(rrduce(add, 0, range(6)))
print(rrduce(mul, 1, range(1, 6)))

