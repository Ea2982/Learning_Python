'''Анонимные функции lambda'''

print(lambda x: x +1)

l = [1, 2, 5, 3, 4]
l.sort(key=lambda x: -x)
print(l)

print(1 + (lambda x: x * 5)(8) + 1)

def caller(arg):
    return lambda f: f(arg)

call_with_five = caller(5)
print(call_with_five)
print(call_with_five(str))
print(call_with_five(lambda x: x +1))

f = lambda x: (
    x + 1
)
print(f)
# f = lambda x: error
#     x +1

# f = lambda x: return x + 1 Error

# lambda f(x): Error
#     x + 1

f = lambda x: x +1
print(f)


def make_module(step=1):
    return {'inc': lambda x: x + step, 'dec': lambda x: x - step}


m = make_module()
print(m['inc'](10)) #11
print(m['dec'](20)) #19
m2 = make_module(step=2)
print(m2['inc'](1)) #3

inc, dec = map(make_module(step=5).get, ['inc', 'dec'])
print(inc)
print(dec)
print(inc(inc(inc(dec(0)))))
