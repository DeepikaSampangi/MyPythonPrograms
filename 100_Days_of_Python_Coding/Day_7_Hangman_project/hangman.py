import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

guess = input("Enter the letter guessed:").lower()

answer = ["_" for _ in range(len(chosen_word))]
print(" ".join(answer))

for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
        answer[i] = guess

print(" ".join(answer))
