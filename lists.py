# List (mutable - can change values)
x = [4, True, 'Ok', 2]
y = 'hi'

x.append('hello')
print(len(x), len(y))
print(x)

x.extend([5, 5, 5])

print(x)
print(x.pop())  # removes and returns last element in the list
print(x.pop(0))  # removes and returns first element (index 0) in the list
print(x)
print(x[1])  # access element at index 1
x[1] = 'Not Ok'  # modify value at index 1
print(x[1])
print(x[0] + x[len(x) - 1])

# ----------------------------

list1 = [1, 2, 3]
list2 = list1  # by reference: if first element in list1 changes -> affects list2
list3 = list1[:]  # copy of list1. changes to list1 not applied to list3
list1[0] = -1
print(list2)
print(list3)
