for i in range(10):
    print(i, end=' ')

# range args:
# stop -> starts at 0 until value (exclude)
# start, stop -> start at given value, until stop (exclude)
# start, stop, step -> start at value, until stop value, and override default step (1)

print('\n----------------')

for i in range(10, -1, -1):
    print(i, end=' ')

print('\n----------------')

x = [3, 4, 1, 9, 2, 8, 2, 7]
for i in x:
    print(i, end=' ')

print('\n----------------')

for i in range(len(x)):
    print(x[i], end=' ')

print('\n----------------')

for i, element in enumerate(x):
    print(i, element)
