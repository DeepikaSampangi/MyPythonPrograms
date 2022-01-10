import random
from higher_lower_art import logo, vs
from game_data import data

print(logo)
data_len = len(data)
score = 0
a_dict = data[random.randint(0, data_len)]

while True:
    print("----------------------------------------")
    b_dict = data[random.randint(0, data_len)]
    print("Compare A: {name}, a {description}, from {country}.".format(**a_dict))
    print(vs)
    print("Compare B: {name}, a {description}, from {country}.".format(**b_dict))

    user_input = input("Who has more followers? Type 'A' or 'B': ")
    if user_input == "A":
        if a_dict["follower_count"] > b_dict["follower_count"]:
            score += 1
            print(f"You're right! Current Score: {score}")
        else:
            print(f"Sorry, that's wrong. Final Score: {score}")
            break
    elif user_input == "B":
        if b_dict["follower_count"] > a_dict["follower_count"]:
            score += 1
            print(f"You're right! Current Score: {score}")
            a_dict = b_dict
        else:
            print(f"Sorry, that's wrong. Final Score: {score}")
            break
    else:
        break
    print("----------------------------------------")
