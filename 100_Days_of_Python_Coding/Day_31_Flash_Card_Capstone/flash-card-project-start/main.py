import os
import random
from tkinter import *

import pandas as pd
from PIL import Image, ImageTk

curr_dir = os.path.dirname(__file__)
BACKGROUND_COLOR = "#B1DDC6"

df = pd.read_csv(curr_dir + "/data/french_words.csv")
to_learn = df.to_dict(orient="records")


def is_known():
    pass


def next_card():
    curr_card = random.choice(to_learn)
    lang = "French"
    canvas.itemconfig(card_title, text=lang)
    canvas.itemconfig(card_word, text=curr_card[lang])


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=curr_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = ImageTk.PhotoImage(Image.open(curr_dir + "/images/card_front.png"))
canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(
    400, 150, text="", fill="black", font=("Ariel", 40, "italic")
)
card_word = canvas.create_text(
    400, 263, text="", fill="black", font=("Ariel", 60, "bold")
)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = ImageTk.PhotoImage(Image.open(curr_dir + "/images/wrong.png"))
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_img = ImageTk.PhotoImage(Image.open(curr_dir + "/images/right.png"))
right_button = Button(image=right_img, highlightthickness=0, command=is_known())
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
