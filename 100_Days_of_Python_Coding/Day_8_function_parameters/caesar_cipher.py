from art import logo

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
print(logo)


def caesar(text: str, shift: int, direction: str):
    end_text = ""
    for letter in text:
        position = alphabet.index(letter)
        if direction == "encode":
            position = alphabet.index(letter) + shift
            if position > 25:
                position -= 26
        elif direction == "decode":
            position = alphabet.index(letter) - shift
            if position < 0:
                position += 26
        end_text += alphabet[position]
    print(f"The {direction}d text is {end_text}")


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text=text, shift=shift, direction=direction)
    ans = input("Want to try again (yes/no):")
    if ans == "no":
        break
