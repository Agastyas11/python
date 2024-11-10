import tkinter
from tkinter import *
import pandas
import random

# Data
BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


# Functions
def next_card():
    global current_card
    current_card = random.choice(to_learn)
    language.config(text="French")
    word.config(text=current_card["French"])


def flip_card():
    language.config(text="English")
    word.config(text=current_card["English"])
    canvas.itemconfig(card_background, image=back)

# Window
window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.after(3000, func=flip_card)

# Image path
red_cross = PhotoImage(file="images/wrong.png")
green_tick = PhotoImage(file="images/right.png")
front = PhotoImage(file="images/card_front.png")
back = PhotoImage(file="images/card_back.png")

# Variables
cross = Button(image=red_cross, highlightthickness=0, command=next_card)
tick = Button(image=green_tick, highlightthickness=0, command=next_card)
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR)
card_background = canvas.create_image(415, 265, image=front)
language = tkinter.Label(text="French", font=("Ariel", 40, "italic"), bg="white", fg="black")
word = tkinter.Label(text="trouve", font=("Ariel", 60, "bold"), bg="white", fg="black")

# Grid
canvas.grid(row=1, column=1, columnspan=2)
tick.grid(row=2, column=1)
cross.grid(row=2, column=2)
language.place(x=355, y=150)
word.place(x=326, y=233)

next_card()

window.mainloop()
