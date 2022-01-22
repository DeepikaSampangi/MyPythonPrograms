# Write your code above 👆

import os
import json

curr_dir = os.path.dirname(__file__)

with open(curr_dir + "/file1.txt") as file1:
    list1 = file1.readlines()

with open(curr_dir + "/file2.txt") as file2:
    list2 = file2.readlines()

result = [int(num) for num in list1 if num in list2]

print(result)
