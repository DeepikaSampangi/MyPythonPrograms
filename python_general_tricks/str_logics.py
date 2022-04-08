# Logic to remove ith Char in a string

input_str = "amazing"
print(f"Old String {input_str}")
new_str = input_str.replace("a", "")
print(f"New String {new_str}")

# removing all occurances
input_str = "amazing"
print(f"Old String {input_str}")
new_str = input_str.replace("a", "", 2)
print(f"New String {new_str}")