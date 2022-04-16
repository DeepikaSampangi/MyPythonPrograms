input_list = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

print(f"Before {input_list}")

k=1
result = [sub[k] for sub in input_list]
print(f"Kth Col is {result}")