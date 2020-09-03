from math import factorial, fabs
'''Рекурсия'''

def my_factorial(n):
    if n <= 0:
        return 1
    return n * factorial(n - 1)

print(factorial(1) == my_factorial(1))
print(factorial(10) == my_factorial(10))
print(factorial(100) == my_factorial(100))

print(my_factorial(10))
# линейная рекурсия
def collatz(n): # Гипотиза Коллатца
    if n == 1:
        return True
    if n % 1 == 0:
        return collatz(n // 2)
    return collatz(n * 3 + 1)

print(collatz(3))
# каскадная рекурсия
def my_fibonacci(n):
    if n <= 2:
        return 1
    return my_fibonacci(n - 1) + my_fibonacci(n - 2)

print(my_fibonacci(5))
print(my_fibonacci(5) == fabs(5))


def is_odd(num):
    return num % 2 == 1

def is_even(num):
    return num % 2 == 0
print(is_odd(42))
print(is_even(42))
