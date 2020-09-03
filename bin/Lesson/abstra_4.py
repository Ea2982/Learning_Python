from math import gcd


def make_rational(numer, denom):
    deletes = gcd(numer, denom)

    return {
        'numer': int(numer / deletes),
        'denom': int(denom / deletes)
    }


def get_numer(rat):
    return rat['numer']


def get_denom(rat):
    return rat['denom']

def add(rat1, rat2):
    if get_denom(rat1) == get_denom(rat2):
        res = make_rational(
        get_numer(rat1) + get_numer(rat2),
        get_denom(rat1)
        )
    else:
        res = make_rational(
            (get_numer(rat1) * get_denom(rat2)) + (get_numer(rat2) * get_denom(rat1)),
            get_denom(rat1) * get_denom(rat2)
        )
    return res

def rat_to_string(rat):
    return f'{get_numer(rat)}/{get_denom(rat)}'
def sub(rat1, rat2):
    if get_denom(rat1) == get_denom(rat2):
        res = make_rational(
            get_numer(rat1) - get_numer(rat2),
            get_denom(rat1)
        )
    else:
        res = make_rational(
            (get_numer(rat1) * get_denom(rat2)) - (get_numer(rat2) * get_denom(rat1)),
            get_denom(rat1) * get_denom(rat2)
        )
    return res


# rat1 = make_rational(3, 9)
# print(get_numer(rat1))
# print(get_denom(rat1))
# rat2 = make_rational(10, 3)
# print(get_numer(rat2))
# print(get_denom(rat2))
# rat3 = add(rat1, rat2)
# print(get_numer(rat3))
# print(get_denom(rat3))
# print(rat_to_string(rat3))
# rat4 =sub(rat1, rat2)
# print(rat_to_string(rat4))

rat5 = make_rational(-4, 16)
rat6 = make_rational(12, 5)
print(rat_to_string(add(rat5, rat6)))
print(rat_to_string(sub(rat5, rat6)))



