def push_and_count(target, *, value):
    print(type(target))
    print(target)
    target.append(target)
    return len(target)

def shoot():
    return 'Bang!'

def call_twice(func, *args, **kwargs):
    return (func(*args, **kwargs), func(*args, **kwargs))


#print(call_twice(input, 'Enter value: '))
#print(call_twice(shoot))
print(call_twice(push_and_count, [], value=42))




# print(call_twice(push_and_count, [], value=42))
# def f(*args, **kwargs):
#     return args, kwargs
# print(f([], value=42))

