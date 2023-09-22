def func(x, y, z=None):
    print('run', x, y, z)

    def inner_func():
        print('hi')

    inner_func()
    return x * y, x + y  # value returned as a tuple


r1, r2 = func(4, 5)
print(r1, r2)
