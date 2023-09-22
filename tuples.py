# Tuple (immutable: cannot append, cannot remove, cannot change)

x = (0, 0, 2, 2)
# x[0] = -1 ---> error!
# x.append(2) ---> error!
print(x[0])
