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


def filter_map(func, items):
    # lst = map(make_stars, items)
    # print(lst)
    lst = list()

    for i1, i2 in map(func, items):
        if i1:
            lst.append(i2)
    return lst


def make_stars(x):
    if x > 0:
        return True, '*' * x
    return False, ''


for s in filter_map(make_stars, [1, 0, 5, -5, 2]):
    print(s)

'''
def filter_map(function, items):
    result = []
    for item in items:
        keep, value = function(item)
        if keep:
            result.append(value)
    return result
'''
