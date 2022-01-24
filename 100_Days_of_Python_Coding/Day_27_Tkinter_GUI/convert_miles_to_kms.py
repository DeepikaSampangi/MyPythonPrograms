from tkinter import *


def convert():
    miles = miles_input.get()
    kms = Label(text=round(int(miles) * 1.609), font=("Arial", 12, "bold"))
    kms.grid(column=1, row=1)


window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

# Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to", font=("Arial", 12, "bold"))
is_equal_label.grid(column=0, row=1)

kms_label = Label(text="km", font=("Arial", 12, "bold"))
kms_label.grid(column=2, row=1)

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

window.mainloop()
