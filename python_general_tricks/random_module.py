import random

print("This prints a random float between 0.0 and 1.0", random.random())

print("This prints a random float between a and b", random.uniform(3.5, 10.0))

print(
    "This prints an Integer between 0 to x-1 inclusive", random.randrange(10)
)

print("This prints an Integer between x to y inclusive", random.randint(2, 10))

print(
    "This prints a choice among given input list",
    random.choice(["heads", "tails", "none"]),
)

names: str = "jack jill tom jerry shichan".split()
random.shuffle(names)
print("To shuffle the given input", names)
