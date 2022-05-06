# Reverse Order Tuple Second Value
val = [('v', 3), ('a', 4), ('b', 2)]
val.sort(key = lambda x: x[1], reverse=True)
print(val)

# Cube od first 5 Odd Numbers
arr = [i*3 for i in range(10) if i%2]
print(arr)

# Dict Comprehension
dic = [(i, i*2) for i in range(10)]
print(dict(dic))

# Using Map
print(list(map(lambda x: x*2, range(10))))

# Using filter
print(list(map(lambda x: x*2, range(10))))