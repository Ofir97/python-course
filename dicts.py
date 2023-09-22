x = {'key': 'value'}
print(x['key'])

y = {0: 'hi', 'key': -1}
print(y)
print(y[0])
print(y['key'])
print('key' in x)  # check if value 'key' exists in dictionary keys
print(0 in y)  # check if 0 exists in dictionary keys
print('hi' in y)
print(list(y.values()))  # returns dictionary values
print(list(y.keys()))  # returns dictionary keys

del y['key']
print(y)

y[2] = 'Bob'

print('--------------------------------')

for key, value in y.items():
    print(key, value)

for key in y:
    print(key, y[key])
