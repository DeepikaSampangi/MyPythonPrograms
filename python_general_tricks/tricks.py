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
