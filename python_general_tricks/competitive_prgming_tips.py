# Reverse Order Tuple Second Value
val = [('v', 3), ('a', 4), ('b', 2)]
val.sort(key = lambda x: x[1], reverse=True)
print(val)