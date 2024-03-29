# Reverse Order Tuple Second Value
val = [('v', 3), ('a', 4), ('b', 2)]
val.sort(key=lambda x: x[1], reverse=True)
print(val)

# Cube od first 5 Odd Numbers
arr = [i*3 for i in range(10) if i%2]
print(arr)

# Dict Comprehension
dic = [(i, i*2) for i in range(10)]
print(dict(dic))

# Using Map
print(list(map(lambda x: x*2, range(10))))

income = [10, 30, 75]
def double_money(x):
    return x*2
updated_income = list(map(double_money, income))
print(updated_income)

# Using filter
print(list(map(lambda x: x*2, range(10))))

# Using Reduce
from functools import reduce
print(reduce(lambda x,y: x+y, range(10)))

# Random Numbers
import random
print(random.choice(range(1, 10)))

#Permutations
import itertools
itertools.permutations('ABCD', 2)

#Char frequency
from collections import Counter
print(dict(Counter("ababacd")))

# List Comprehension
msg = "ababcd"
dic = [(i, msg.count(i)) for i in set(msg)]
print(dict(dic))

# Dict to list
dic = {'a': 3, 'b': 2, 'c': 1, 'd': 1}
# list of dictionary keys
print(list(dic))
# list of dictionary values
print([v for k, v in dic.items()])

# Decimal to Binary
num = 9
binary_num = bin(num).replace("0b", "")

#Counter Package
my_list = [1, 3, 4, 1, 2, 1, 1, 3, 4, 3, 5, 1, 2, 5, 3, 4, 5]

counter = Counter(my_list)
top_three_elements = counter.most_common(3)
print(top_three_elements)

# nth largest or smallest number
import heapq
grades = [110, 25, 38, 49, 20, 95, 33, 87, 80, 90]
print(heapq.nlargest(3, grades))
print(heapq.nsmallest(4, grades))

#zip dict
stocks = {'Goog': 520.54,
          'FB': 76.45,
          'YHOO': 39.28,
          'AMZN': 306.21,
          'APPL': 99.76}
zip_1 = zip(stocks.values(), stocks.keys())
print(sorted(zip_1))
zip_2 = zip(stocks.keys(), stocks.values())
print(sorted(zip_2))

#List to Dictionary
user = ["Peter","John","Sam"]
age = [23,19,34]
dictionary = dict(zip(user, age))
print(dictionary)