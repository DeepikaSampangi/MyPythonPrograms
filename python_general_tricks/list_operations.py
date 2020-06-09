# find frequent value in a list

input_list: list = [1,2,3,4,5,1,3,2,3,4,1,4,5,9,0]

print(max(set(input_list), key=input_list.count))

#Create a soingle string from a list

input_list_str: list = ['Hello', 'to', 'the', 'world']

print(" ".join(input_list_str))

# print a list x no of times
data = [2, 3, 9]
temp = [[x for x in[data]] for x in range(3)]
print (temp)


# List of missing elements in two lists

input_list1: list = ['a','b','c','d']
input_list2: list = ['e','f','a','b']

set1: set = set(input_list1)
set2: set = set(input_list2)

diff_list: list = list( set1.symmetric_difference(set2))

print(f"List of missing elements is {diff_list}")
