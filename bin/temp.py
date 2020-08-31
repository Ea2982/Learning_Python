def shoot():
    return 'Bang!'
def call_twice(fn, **args):
    return fn(), fn()

#print(call_twice(input, 'Enter value'))
print(call_twice(shoot))