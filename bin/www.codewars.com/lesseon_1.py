'''www.codewars.com'''
'''example 1'''
def solution(number):
    if number < 0:
        return 0
    res = 0
    for num in range(number):
        if num % 3 == 0 or num % 5 == 0:
            # print(num)
            res += num

    return res
def solution1(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

print(f'solution1(10): {solution1(10)}')
print(f'solution1(23): {solution1(23)}')
print(f'solution(0): {solution(0)}')
print(f'solution(-5): {solution(-5)}')

print('////////////////////////////////////////////////////////////\n\n')

'''exemple 2'''

def array_diff(a, b):
    lst = a.copy()
    for item_b in b:
        for item_a in a:
            if item_a == item_b:
                lst.remove(item_b)
    print(lst)
    return lst

print(array_diff([5],[-20, 1, -8, 6, 10, 11, -13, -8]))
# print(array_diff([1,2],[1]) == [2])
# print(array_diff([1,2,2], [2]) == [1])
# print(array_diff([], [1,2]) == [])