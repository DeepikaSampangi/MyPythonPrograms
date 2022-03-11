import sys

int_variable: int = 10
str_variable: str = "Hello"
int_list: list = [1, 2, 3, 4]
str_list: list = ["a", "b", "c"]

print(f"Size of int is {sys.getsizeof(int_variable)}")
print(f"Size of str is {sys.getsizeof(str_variable)}")
print(f"Size of int list is {sys.getsizeof(int_list)}")
print(f"Size of str list is {sys.getsizeof(str_list)}")
