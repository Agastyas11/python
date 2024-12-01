from tkinter import *
import requests


def category_chooser():
    category_window = Tk()
    category_window.title("Choose Your Category")
    category_window.geometry("600x400")

    # Dropdown menu options

    options = {
        "General Knowledge": 9,
        "Entertainment: Books": 10,
        "Entertainment: Film": 11,
        "Entertainment: Music": 12,
        "Entertainment: Musical Theaters": 13,
        "Entertainment: Television": 14,
        "Entertainment: Video Games": 15,
        "Entertainment: Board Games": 16,
        "Science & Nature": 17,
        "Science: Computers": 18,
        "Science: Mathematics": 19,
        "Mythology": 20,
        "Sports": 21,
        "Geography": 22,
        "History": 23,
        "Politics": 24,
        "Art": 25,
        "Celebrities": 26,
        "Animals": 27,
        "Vehicles": 28,
        "Entertainment: Comics": 29,
        "Science: Gadgets": 30,
        "Entertainment: Japanese Anime & Manga": 31,
        "Entertainment: Cartoon & Animations": 32,
    }

    # datatype of menu text
    clicked = StringVar()

    # initial menu text
    clicked.set("General Knowledge")

    # Get keys
    def getlist(dicts):
        lists = []
        for key in dicts.keys():
            lists.append(key)
        return lists

    # Create Dropdown menu
    drop = OptionMenu(category_window, clicked, *getlist(options))
    drop.pack()

    # Create Quiz
    def button_pressed():
        category_chosen = clicked.get()
        category_number = options.get(category_chosen)
        parameters.update({"category": category_number})
        category_window.destroy()

    enter_button = Button(text="Submit", command=button_pressed)
    enter_button.pack()

    category_window.mainloop()


parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 9,

}

category_chooser()

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
