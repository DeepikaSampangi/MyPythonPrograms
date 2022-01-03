import random
from hangman_art import logo, stages
from hangman_word import word_list

chosen_word = random.choice(word_list)

answer = ["_" for _ in range(len(chosen_word))]
print(logo)

lives = 6
print(stages[lives])
print(" ".join(answer))

game_over = False
guessed_list = []

while not game_over:
    guess = input("Enter the letter guessed:").lower()
    if guess in guessed_list:
        print(f"You have already guessed : {guess} ")
    else:
        guessed_list.append(guess)
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                answer[i] = guess
        print(" ".join(answer))
        if "_" not in answer:
            print(f"You won")
            game_over = True
        if guess not in chosen_word:
            lives -= 1
            print(f"{guess} not in the Word, you lose a life")
            if lives == 0:
                game_over = True
                print(f"Game over, Solution is {chosen_word}")
    print(stages[lives])
