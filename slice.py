x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = ['hi', 'hello', 'goodbye', 'cya', 'sure']
s = 'hello'

# list[start(index) : stop(index) exclude : step]
sliced = x[0:4:2]
print(sliced)
print(x[2:])  # start at index 2 -> to the end
print(x[:5])  # start from beginning -> until index 5 (exclude)
print(x[2:4])  # start from index 2 -> until index 4 (exclude)
print(x[4:2:-1])  # start from index 4 -> until index 2 (exclude)
print(x[::2])  # start from beginning to end -> jump by 2

print('Reversed list: ', x[::-1])
print('Reversed list: ', y[::-1])

print('Reversed tuple: ', (1, 2, 8, 2, 9)[::-1])

