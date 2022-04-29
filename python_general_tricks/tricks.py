# Reverse List
input_list = ["e","c","n","a","d"]
input_list.reverse()
print(input_list)

#Generator Function
print(sum(i for i in range(10)))

#Using zip function
year = (1996, 2004, 2010, 2022)
month = ("sept", "march", "dec", "jan")
day = (26, 10, 25, 1)
print(list(zip(year, month, day)))


# Transpose of Matrix
input_matrix = [[10,21],[3,20],[16,28]]
print(list(zip(*input_matrix)))

#Print n times
input_str = "Hello"
print(input_str*4)

#Factors of a number

num = 32
for i in range(1, num+1):
    if num%i == 0:
        print(i)