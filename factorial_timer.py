import timeit
from math import factorial, prod
from functools import reduce


def math_prod(n):
    return prod(range(1, n + 1))


def math_factorial(n):
    return factorial(n)


def factorial_iter(n):
    counter = 1
    for i in range(1, n + 1):
        counter *= i
    return counter


def factorial_recursion_ternary(n):
    return 1 if n == 1 else factorial_recursion_ternary(n - 1) * n


def f2(n1, n2):
    return n1 * n2


def factorial_reduce2(n):
    return reduce(f2, range(1, n + 1))


def factorial_reduce(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


def factorial_recursion(n):
    if n == 1:
        return 1
    return n * factorial_recursion(n - 1)


def timer(func, n):
    time_run = timeit.timeit('func(n)', number=1_000_000, globals={'func': func, 'n': n})
    print(f'{func.__name__:<30} {time_run}')


def timer2(func, n):
    time_run = timeit.repeat('func(n)', number=1_000_000, repeat=5, globals={'func': func, 'n': n})
    print(time_run)


rec_value = 10
rec_list = [math_factorial, math_prod, factorial_iter,
            factorial_recursion_ternary, factorial_recursion, factorial_reduce2, factorial_reduce]

for func in rec_list:
    timer(func, rec_value)


'''
math_factorial                 0.12152320001041517
math_prod                      0.45572500000707805
factorial_iter                 0.7426269000279717
factorial_recursion_ternary    1.005446600029245
factorial_recursion            1.0625144999939948
factorial_reduce2              1.5066453000181355
factorial_reduce               1.5290826999698766
'''