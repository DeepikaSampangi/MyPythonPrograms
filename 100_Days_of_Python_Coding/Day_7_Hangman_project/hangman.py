import random

# from hangman_art import logo, stages

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)


answer = ["_" for _ in range(len(chosen_word))]
print(" ".join(answer))

# print(logo)
lives = 5
while lives > 0:
    guess = input("Enter the letter guessed:").lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            answer[i] = guess
        if "_" not in answer:
            print("Game Over")
    lives -= 1
    print(" ".join(answer))

if "_" in answer:
    print("Game over")
