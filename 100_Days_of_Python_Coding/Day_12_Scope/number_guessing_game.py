import random

actual = random.choice([i for i in range(1, 101)])


def guess_num(attempts):
    for i in range(attempts):
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess : "))
        if guess > actual:
            print("Too High")
        elif guess < actual:
            print("Too low")
        elif guess == actual:
            print("Congratulations, You win the answer is {guess}!")
            break
        attempts -= 1
        if attempts == 0:
            print("You've run out of guessess, you lose.")
            break
        else:
            print("Guess Again.")


print("Welcome to the NUmber Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ")

if difficulty == "hard":
    guess_num(5)
elif difficulty == "easy":
    guess_num(10)
