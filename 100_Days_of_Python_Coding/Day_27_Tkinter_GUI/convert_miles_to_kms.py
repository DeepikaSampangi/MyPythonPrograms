from tkinter import *


def convert():
    miles = input.get()
    my_label4 = Label(text=round(int(miles) * 1.6), font=("Arial", 12, "bold"))
    my_label4.grid(column=2, row=3)
    # my_label4.config(padx=50, pady=50)


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=250, height=100)

# Entry
input = Entry(width=10)
input.grid(column=2, row=2)

my_label1 = Label(text="Miles", font=("Arial", 12, "bold"))
my_label1.grid(column=3, row=2)
# my_label1.config(padx=50, pady=50)

my_label2 = Label(text="is equal to", font=("Arial", 12, "bold"))
my_label2.grid(column=1, row=3)
# my_label2.config(padx=50, pady=50)


my_label3 = Label(text="km", font=("Arial", 12, "bold"))
my_label3.grid(column=3, row=3)
# my_label3.config(padx=50, pady=50)


button = Button(text="Calculate", command=convert)
button.grid(column=2, row=4)

window.mainloop()
