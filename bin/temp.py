def filter_map(func, items):
    # lst = map(make_stars, items)
    # print(lst)
    lst = list()

    for i1, i2 in map(make_stars, items):
        if i1:
            lst.append(i2)
    return lst



def make_stars(x):
    if x > 0:
        return True, '*' * x
    return False, ''

for s in filter_map(make_stars, [1, 0, 5, -5, 2]):
    print(s)


