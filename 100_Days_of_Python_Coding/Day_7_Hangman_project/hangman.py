import random

# from hangman_art import logo, stages
stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)


answer = ["_" for _ in range(len(chosen_word))]
print(" ".join(answer))

lives = 6
print(stages[lives])

game_over = False

while not game_over:
    guess = input("Enter the letter guessed:").lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            answer[i] = guess

    if "_" not in answer:
        print(f"You won")
        game_over = True
    if guess not in chosen_word:
        lives -= 1
    if lives == 0:
        game_over = True
    print(stages[lives])
    print(" ".join(answer))


if "_" in answer:
    print(f"Game over, Solution is {chosen_word}")
