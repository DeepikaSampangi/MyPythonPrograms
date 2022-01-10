import random
from higher_lower_art import logo, vs
from game_data import data

print(logo)
data_len = len(data)
score = 0
a_dict = data[random.randint(0, data_len)]
a_name = a_dict["name"]
a_description = a_dict["description"]
a_country = a_dict["country"]

b_dict = data[random.randint(0, data_len)]
print(f"Compare A: {a_name}, a {a_description}, from {a_country}.")
# print(vs)
# print(
#     f"Compare B: {data[b_index].name}, a {data[b_index].description}, from {data[b_index].country}."
# )

# user_input = input("Who has more followers? Type 'A' or 'B': ")
# if user_input == "A":
#     if data[a_index].follower_count > data[b_index].follower_count:
#         score += 1
#         print(f"You're right! Current Score: {score}")
#     else:
#         print(f"Sorry, that's wrong. Final Score: {score}")
