# # # import math
# # #
# # #
# # # def hello(name: str) -> str:
# # #     return f'Hi {name}'
# # #
# # #
# # # def sum_of_ints(start: int, end: int) -> int:
# # #     n = 0
# # #     for i in range(start, end + 1):
# # #         n += i
# # #     return n
# # #
# # #
# # # def sum_of_squares(start: int, end: int) -> int:
# # #     n = 0
# # #     for i in range(start, end + 1):
# # #         n += i ** 2
# # #     return n
# # #
# # #
# # # def sum_of_cubes(start: int, end: int) -> int:
# # #     n = 0
# # #     for i in range(start, end + 1):
# # #         n += i ** 3
# # #     return n
# # #
# # #
# # # # def ints(x:int) -> int: return x
# # # #
# # # #
# # # # def squarse(x): return x ** 2
# # # #
# # # #
# # # # def cobes(x): return x ** 3
# # # #
# # # #
# # # # def areas(x): return x ** 2 * 3.14
# # #
# # #
# # # def sum_of(start: int, end: int, fn):
# # #     n = 0
# # #     for i in range(start, end + 1):
# # #         n += fn(i)
# # #     return n
# # #
# # #
# # # # print(sum_of(1, 10, lambda x: x))
# # # # print(sum_of(1, 10, lambda x: x ** 2))
# # # # print(sum_of(1, 10, lambda x: x ** 3))
# # # # print(sum_of(1, 10, lambda x: x ** 2 * math.ceil(math.pi)))
# # # #
# # # # hi = hello
# # # #
# # # # print(hi('Jenny'))
# # # # print(hello('Sasha'))
# # #
# # # # lst = [1, 2, 3, 4, 5, 6, 7]
# # # # new_lst = list
# # # # new_lst = [str(i) for i in lst]
# # # #
# # # # new_lst = list(map(lambda i: i*10, lst))
# # # # print(new_lst)
# # #
# # # lst = [6, 3, 7, 2, 6, 9, 4, 8]
# # # new_lst = list(filter(lambda i: i > 3, lst))
# # # print(new_lst)
# # # new_lst = set(filter(lambda i: i > 3, lst))
# # # print(new_lst)
# # #
# # from functools import reduce
# #
# # #
# # # lst = [i for i in range(1, 6)]
# # # print(lst)
# # #
# # # sum_all = reduce(lambda a, b: a + b, lst, 100)
# # # print(sum_all)
# # #
# # # lst = [6, 3, 7, 2, 6, 9, 4, 8]
# # # m = reduce(lambda a, b: a if (a>b) else b, lst)
# # # print(m)
# # #
# # # a = [1, 2, 3]
# # # b = 'xyz'
# # # c = (None, True)
# # #
# # # print(list(zip(a, b, c)))
# # #
# #
# # lst = [6, 3, 7, 2, 6, 9, 4, 8]
# # l1 = list(filter(lambda i: i > 5, lst))
# # l2 = list(map(lambda i: i * 10, l1))
# # l = reduce(lambda a, b: a + b, l2)
# # print(l)
#
#
# def compose(f, g):
#     return lambda x: f(g(x))
#
#
# double = lambda x: x * 2
# inc = lambda x: x + 1
#
# inc_and_double = compose(double, inc)
# print(inc_and_double(2))
#
#
# def add(x):
#     return lambda y: x + y
#
# a = add(10)
# print(a(10))
#
#
# def setup(lst):
#     i = 0
#     def ret():
#         nonlocal i
#         v = lst[i]
#         i += 1
#         return v
#     return ret
# next_val = setup([i for i in range(1, 6)])
#
# print(next_val)



def add_underscores(understroke):
    def decor(fn):
        def wrapper(name):
            s = f'_{fn(name)}_'
            s += '\n' + understroke
            return s
        return wrapper
    return decor

@add_underscores('===')
def hello(name):
    return f'Hi, {name}'


print(hello('test'))


import functools

@functools.lru_cache(maxsize=None)
def square(n):
    print('here')
    return n ** 2

print(square(4))
print(square(4))
print(square(4))
print(square(5))
print(square(5))