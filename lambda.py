sum = lambda x, y: x + y

print(sum(5, 2))


# map and filter:


def func(i):
    return i > 10


x = [2, 9, 1, 74, 8, 4, 19, 2, 4, 9, 3, 1]

mp = map(lambda i: i + 1, x)  # returns a map obj
print(list(mp))
print(list(filter(lambda i: i % 2 == 0, x)))
print(list(filter(func, x)))
