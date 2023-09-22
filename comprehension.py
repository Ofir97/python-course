x = [x for x in range(5)]
print(x)

x = [x + 1 for x in range(10)]
print(x)

print([0 for x in range(10)])

print([[0 for _ in range(10)] for x in range(5)])
print([x for x in range(100) if x % 2 == 0])  # list
print({i: 0 for i in range(100) if i % 2 == 0})  # dictionary
print({i for i in range(100) if i % 2 == 0})  # set
print(tuple(i for i in range(100) if i % 2 == 0))  # tuple
