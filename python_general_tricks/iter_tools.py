from itertools import combinations

num_list = [1,2,3,4,5,6]

for i in num_list:
    for j in num_list:
        if i < j:
            print((i, j))

## Above Logic using Iter tools

combi = combinations(num_list, 2)
for pair in list(combi):
    print(pair)