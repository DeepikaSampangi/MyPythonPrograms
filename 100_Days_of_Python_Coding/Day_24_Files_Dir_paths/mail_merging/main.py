PLACEHOLDER = "[name]"

from os.path import dirname, join

current_dir = dirname(__file__)

with open(current_dir + "/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open(current_dir + "/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(
            current_dir + f"/Output/ReadyToSend/letter_for_{stripped_name}.txt",
            mode="w",
        ) as completed_letter:
            completed_letter.write(new_letter)
