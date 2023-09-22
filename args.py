def func(y):
    def func2():
        print(y)

    return func2


func(3)()

###########################################

x = [23, 99, 10, -2, 34, 883, 293]

print(x)
print(*x)  # unpack all items from list/tuple


###########################################

def func(p1, p2):
    print(p1, p2)


pairs = [(1, 2), (3, 4)]
for pair in pairs:
    func(*pair)

func(**{'p2': 1, 'p1': 2})


###########################################

def func2(*args, **kwargs):  # args: tuple, key-word args
    print(args, kwargs)


func2(1, 2, 3, 4, 5, one=1, two=2, three=3)
