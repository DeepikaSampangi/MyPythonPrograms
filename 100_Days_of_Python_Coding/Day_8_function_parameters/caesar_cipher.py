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

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().


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


# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(text=text, shift=shift, direction=direction)
