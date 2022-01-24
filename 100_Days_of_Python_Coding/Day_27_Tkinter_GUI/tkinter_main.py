from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label

my_label = Label(text="I am Label", font=("Arial", 24, "bold"))

my_label.pack()

# Button
def button_click():
    input_value = input.get()
    my_label.config(text=input_value)


button = Button(text="Submit", command=button_click)
button.pack()

# Entry
input = Entry(width=10)
input.pack()
window.mainloop()
