import functools, operator

def keep_truthful(itr):
    return filter(None, itr)

print(list(keep_truthful([True, False, "", "foo"]))) # [True, 'foo']


def abs_sum(itr):
    return sum(list(map(abs, itr)))

print(abs_sum([-3, 7])) #10
print(abs_sum([])) #0
print(abs_sum([42])) # 42

def walk(source, road):
    # p1 = operator.getitem(source, road[0])
    # print(road[0])
    # print('p1: ',sep=' ', end='')
    # print(p1)
    # p2 = operator.getitem(source, road[1])
    # print(road[1])
    # print('p2: ', sep=' ', end='')
    # print(p2)
    # p1 = operator.getitem(operator.getitem(operator.getitem(source, road[0]), road[1]), road[2])
    # print(p1)
    return functools.reduce(operator.getitem, road, source)
    #print(operator.getitem(source, road[0]))
print(walk({'a': {7: {'b': 42}}}, ["a", 7, "b"])) # 42
print(walk({'a': {7: {'b': 42}}}, ["a", 7])) # {'b': 42}

#