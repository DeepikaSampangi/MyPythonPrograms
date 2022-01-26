import os
from tkinter import *
from turtle import width

curr_dir = os.path.dirname(__file__)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
pwd_img = PhotoImage(file=curr_dir + "/logo.png")
canvas.create_image(100, 100, image=pwd_img)
canvas.grid(column=1, row=1)

window.mainloop()
