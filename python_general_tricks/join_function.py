## join is used to join all the separated element to create a single string
## cloud be join by various separators

new_year_date = ['01','01','2020']

print("-".join(new_year_date))

my_name_1 = ['D','E','E','P','I','K','A']
print("".join(my_name_1))

my_name_2 = {1:'D',2:'E',3:'E',4:'P',5:'I',6:'K',7:'A'}
print("".join(my_name_2.values()))
print("".join(str(my_name_2.keys())))

## As a set is an unordered collection of items the iutput is always random
my_name_3 = {'D','E','E','P','I','K','A'}
print("".join(my_name_3))


input_text = 'Separate this'
separator = ';'
print(separator.join(input_text))

##