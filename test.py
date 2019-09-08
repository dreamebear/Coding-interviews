import array as arr

a = arr.array('d', [2,3,4,5,7])

# remove(item) did not return anything
print(a.remove(2))
print(a)

# pop() return deleted item
print(a.pop())
print(a)

# pop by index
print(a.pop(2))
print(a)

