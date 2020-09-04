'''Dict'''

user = {
    'name': 'superjob',
    'email': 'bob.is.super@gmail.com',
    'age': 35
}
print(user)

dictionary = {
    'foo': 'bar',
    'baz': 42,
    'items': {
        1: 'apple',
        2: 'orange',
        100500: 'lemon'
    },
}
print(dictionary)
print('baz' in dictionary)
print('BANZ' in dictionary)
for k in {'a': 1, 'b': 2}:
    print(k)
print(list({'a': 1, 'b': 2}.keys()))
print(list({'a': 1, 'b': 2}.values()))
for k, v in {'a': 1, 'b': 2}.items():
    print(k, v)
print(list(dictionary))


def make_user(name: str, age: int) -> dict:
    return {'name': name, 'age': age}


def format_user(dct: dict) -> str:
    return f'{dct["name"]}, {dct["age"]}'


phil = make_user('phil', 25)
phil = format_user(phil)
print(phil)

d = {'a': 100}
print(d)
d['b'] = 200
d['a'] = 0
print(d)

d = {'a': 1, 'b': 2}
print(d)
d.pop('a')
print(d)


def count_all(obj) -> dict:
    dct = dict()
    for item in obj:
        dct[item] = dct.get(item, 0) + 1
    return dct


print(count_all(['cat', 'dog', "cat"]))
print(count_all('Hello'))
print(count_all('*' * 20))

dictionary.clear()
print(dictionary)
key = 'a'
if key not in dictionary:
    dictionary[key] = []
dictionary[key].append(key)
print(dictionary)
key = 'b'
dictionary.setdefault(key, []).append(key)
print(dictionary)

from collections import defaultdict

d = defaultdict(int)
print(d)
d['a'] += 5
d['b'] = d['c'] + 10
print(d)
print(dict(d))

d = {}
d.setdefault('a', d.setdefault('b', [])).append(1)
print(d)


def collect_indexes(iter):
    dct = defaultdict(int)
    for index in range(len(iter)):
        dct.setdefault(iter[index], []).append(index)
    return dict(dct)


d = collect_indexes([])
print(d)
d = collect_indexes([1])
print(d)
d = collect_indexes([1, 2])
print(d)
d = collect_indexes('lol')
print(d)
d = collect_indexes('coco')
print(d)
d = collect_indexes('hello')
print(d)

'''SET'''
print('SET')
s = set()
s = {1, 2, 3, 2, 1}
print(s)
s = set('abracadabra')
print(s)
s = set([1, 2, 3, 2, 1])
print(s)
print()
print()
s = set([])
print(s)
print(type(s))
s = set()
print(s)
print(type(s))
s = {}
print(s)
print(type(s))
s = set('')
print(s)
print(type(s))


def all_unique(data):
    items = list(data)
    return len(items) == len(set(items))


def all_unique_old(data):
    i = iter(data)
    next_elem = True
    count = 0
    lst = list()

    while next_elem:
        try:
            item = next(i)
            lst.append(item)
            count += 1
        except StopIteration:
            next_elem = False

    print('lst ', lst)
    print('Set', set(lst))
    print('len ', len(set(lst)))
    print('Count ', count)
    if count == len(set(lst)):
        return True

    return False
    # print(data, type(data))
    # data = list(data)
    # print(data, type(data), len(data))
    # if len(data) == 0:
    #     return False
    # return len(set(data)) == len(data)


# i = iter([])
# print()
# i = list(i)
# print(type(i), i)
# print()
# print(next(i))
# print(type(i), id(i))
# i = iter([1])
# print(next(i))
# print((next(i)))
# print(type(i), id(i))

print()
print()
print()
print(iter([]))
print(all_unique(iter([])))
print(iter([1]))
print(all_unique(iter([1])))
#
# print(all_unique([]))
# print(all_unique('cat'))
# print(all_unique('lol'))
print([1, 2, 3])
print(all_unique([1, 2, 3]))
print([1, 2, 1])
print(all_unique([1, 2, 1]))
print('-----------------------------------------------------------------\n')
s = set()
s.add(1)
s.add(2)
s.add(2)
print(s)
s.discard(1)
print(s)
s.discard(1)
print(s)
s.remove(2)
print(s)
s1 = {1, 2, 3}
s2 = s1.copy()
print("s2 ", s2)
s2.add(4)
print("s1 ", s1)
print("s2 ", s2)

READ_ONLY = 'read_only'
flags = set()


def toggle(name, flags: set):
    if name in flags:
        flags.discard(name)
    else:
        flags.add(name)


def toggled(name, flags: set):
    l_flags = flags.copy()
    print(l_flags)
    if name in l_flags:
        l_flags.discard(name)
    else:
        l_flags.add(name)
    return l_flags


a, b, c = 'abc'

flags = {a, b}
print(toggled(c, flags))

a = {1, 2}
b = {2, 3}
c = a ^ b
print(c)
d = a & b
print(d)
print((1 in c and 3 in c) and not 2 in c)

print(set([42]) == set((42,)))
print(set(['a', 'c', 't']) == set('cat'))
print(set('terror') == set('torero'))
print(set(['d', 'o', 'd', 'o']) == set('Dodo'))
print(set('terror'), set('torero'))

print('-----------------------------------------------------------------\n')


def diff_keys(old_dict: dict, new_dict: dict) -> dict:
    res_dict = dict()
    res_dict['kept'] = set(old_dict) & set(new_dict)
    res_dict['added'] = set(new_dict) - set(old_dict)
    res_dict['removed'] = set(old_dict) - set(new_dict)
    return res_dict


print(diff_keys({'name': 'Bob', 'age': 42}, {}), '\n\n')

print(diff_keys({}, {'name': 'Bob', 'age': 42}), '\n\n')
print(diff_keys({'a': 2}, {'a': 1}))
