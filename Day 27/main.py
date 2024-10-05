from tkinter import *

# Setting Window
window = Tk()
window.minsize(300, 100)
window.title("Mile to Km Converter")


# Calculate
def calculate():
    miles = user_miles.get()
    kilometers = round(int(miles) * 1.60934)
    output = Label(text=str(kilometers))
    output.grid(row=2, column=2)


# Data
user_miles = Entry(width=20)
Miles = Label(text="Miles")
is_equal_to = Label(text="is equal to")
km = Label(text="Km")
Calculate = Button(text="Convert", command=calculate)

# Grid Setup
user_miles.grid(row=1, column=2)
Miles.grid(row=1, column=3)
is_equal_to.grid(row=2, column=1)
km.grid(row=2, column=3)
Calculate.grid(row=3, column=2)

window.mainloop()
