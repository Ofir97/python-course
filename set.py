# set: unique unordered list (no duplicates)
# fast at lookups, removals, additions, element existence checks

x = set()  # empty set
s = {4, 2, 5, 5}  # populated set (same {} as dictionary)
s.add(5)
s.remove(5)

print(s)
print(4 in s)  # check if element with value 4 exists in set
print(90 in s)  # check if element with value 90 exists in set

# this existence check is much faster in set than regular list

s2 = {-2, -3, -1, -2, -5, 2}
print(s.union(s2))
print(s.difference(s2))

