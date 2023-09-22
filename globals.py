x = 'tim'


def func(name):
    global x  # reference x defined in the global scope
    x = name


print(x)
func('changed')
print(x)
