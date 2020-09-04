def is_continuous_sequence(lst: list) -> bool:
    if len(lst) < 2:
        return False

    lst_next = [i for i in range(len(lst))]
    first_elem = lst[0]
    b_lst = list(map(lambda i, j: i == j + first_elem, lst, lst_next))
    if False in b_lst:
        return False
    return True


print(is_continuous_sequence([10, 11, 12, 13]) == True)
print(is_continuous_sequence([-5, -4, -3]) == True)
print(is_continuous_sequence([10, 11, 12, 14, 15]) == False)
print(is_continuous_sequence([1, 2, 2, 3]) == False)
print(is_continuous_sequence([7]))
print(is_continuous_sequence([]) == False)
