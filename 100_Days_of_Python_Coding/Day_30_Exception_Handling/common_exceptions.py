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
# finally:
#     # Do this no matter what happens
