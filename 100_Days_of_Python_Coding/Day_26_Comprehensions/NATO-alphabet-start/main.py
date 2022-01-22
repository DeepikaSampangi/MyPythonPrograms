import os

import pandas as pd

curr_dir = os.path.dirname(__file__)

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato_df = pd.read_csv(curr_dir + "/nato_phonetic_alphabet.csv")

nato_dict = {row["letter"]: row["code"] for index, row in nato_df.iterrows()}
print(nato_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter a word: ").upper()
nato_output = [nato_dict[letter] for letter in user_input]
print(nato_output)
