import itertools
def remove_first_level(tree):
    children = filter(lambda item: isinstance(item, list), tree)
    print(list(children))
    return list(itertools.chain(*children))


def remove_first_level_old(tree):
    level = 0
    lst = list()
    for i in tree:
        if type(tree) == type(i):
            for j in i:
                lst.append(j)
    return lst

tree = [
    3,
    [5, 3],
    [[2]]
]
print(tree)
print(remove_first_level(tree))

tree1 = [
    [5],
    1,
    [3, 4]
]
print(tree1)
print(remove_first_level(tree1))
#
# tree3 = [1, 2, [3, 5], [[4, 3], 2]]
# print(tree3)
# print(remove_first_level(tree3))
#
# tree = (1, 2, (3, 5), ((4, 3), 2))
# print(tree)
# print(remove_first_level(tree))
#
# tree = (1, 2, ({[3, 5]}), ((4, 3), [2]))
# print(tree)
# print(remove_first_level(tree))