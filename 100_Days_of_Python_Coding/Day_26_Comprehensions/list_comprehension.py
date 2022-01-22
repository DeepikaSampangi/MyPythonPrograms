numbers = [1, 2, 3, 4]

new_list = [n + 1 for n in numbers]

print(f"Numbers : {numbers}")
print(f"Numbers New List : {new_list}")

name = "Ananya"
new_name_list = [letter for letter in name]
print(new_name_list)
print(list(name))

doubled_list = [2 * n for n in range(1, 5)]
print(doubled_list)


names = ["Damon", "Stefan", "Caroline", "Elena", "Bonnie", "Katherine"]

short_names = [name for name in names if len(name) < 6]
print(short_names)

long_names = [name.upper() for name in names if len(names) > 5]
print(long_names)
