def push_and_count(target, *, value):
    print(target)
    target.append(target)
    return len(target)

def shoot():
    return 'Bang!'

def call_twice(func, *args, **kwargs):


#print(call_twice(input, 'Enter value'))
#call_twice(shoot)




print(call_twice(push_and_count, [], value=42))

