# new_dict = {new_key:new_value for (key, value) in dict.items() if test}
import random

from black import out

names = ["Damon", "Stefan", "Caroline", "Elena", "Bonnie", "Katherine"]
profile_scores = {name: random.randint(50, 100) for name in names}
print(profile_scores)

outstanding = {name: score for (name, score) in profile_scores.items() if score > 75}
print(outstanding)
