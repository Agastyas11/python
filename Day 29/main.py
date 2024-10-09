from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def new_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    random_password = "".join(password_list)
    password_box.insert(0, random_password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_details():
    user_website = website_box.get()
    user_email = email_box.get()
    user_password = password_box.get()
    if not user_website or not user_email or not user_password:
        return messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    is_ok = messagebox.askokcancel(title=user_website, message=f"These are the details entered: \nEmail: {user_email} "
                                                               f"\nPassword: {user_password} \nIs it ok to save?")
    if is_ok:
        user_details = open("user_details.txt", "a")
        user_details.write(f"\n {user_website} | {user_email} | {user_password}")
        user_details.close()
        website_box.delete(0, END)
        email_box.delete(0, END)
        password_box.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

# Text
website = Label(text="Website:")
email_slash_username = Label(text="             Email/Username:")
password = Label(text="  Password:")

# Entry Boxes
website_box = Entry(width=38)
website_box.focus()
email_box = Entry(width=38)
password_box = Entry(width=21)

# Buttons
generate_password = Button(text="Generate Password", command=new_password)
add = Button(width=36, text="Add", command=save_details)

# Grid
canvas.grid(row=1, column=2)

# -labels
website.grid(row=2, column=1)
email_slash_username.grid(row=3, column=1)
password.grid(row=4, column=1)

# -entry boxes
website_box.grid(row=2, column=2, columnspan=2)
email_box.grid(row=3, column=2, columnspan=2)
password_box.grid(row=4, column=2)

# -buttons
generate_password.grid(row=4, column=3)
add.grid(row=5, column=2, columnspan=2)

window.mainloop()
