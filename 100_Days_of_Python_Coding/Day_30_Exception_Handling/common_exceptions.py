# FileNotFound
# with open("a_text.txt") as file:
# file.read()


# KeyError
# a_dict = {"key": "value"}
# value = a_dict["non_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[4]

# TypeError
# text = "abc"
# print(text + 5)

# try:
#     #Something that might caue an exception
#     file = open("a_file.txt")
# except FileNotFoundError:
#     # Do this if there was an exception
#     file = open("a_file.txt", "w")
#     print("There was an error")
# else:
#     # Do this if there were no exceptions
# content = file.read()
# print(content)
# finally:
#     # Do this no matter what happens
# file.close()

# Raising Exceptions

ht = float(input("Heigth: "))
wt = int(input("Weight: "))
if ht > 3:
    raise ValueError("Invalid Heigth Value")
bmi = wt / ht ** 2

print(bmi)
