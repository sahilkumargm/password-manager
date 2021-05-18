from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
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

    password = "".join(password_list)
    entry_password.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    user_website = entry_website.get()
    user_email = entry_email.get()
    user_password = entry_password.get()

    def clear_entries():
        entry_website.delete(first=0, last=END)  # Clears the website entry
        # entry_email.delete(first=0, last=END)
        entry_password.delete(first=0, last=END)  # Clears the password entry
        entry_website.focus()  # Puts the cursor back to the website entry

    new_data = {
        user_website: {
            "email": user_email,
            "password": user_password
        },
    }

    if len(user_website) == 0 or len(user_password) == 0:
        messagebox.showwarning(title="Empty fields found!", message="Please don't leave any fields empty!")
    else:
        # Read the old data
        try:
            with open("data.json", mode='r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode='w') as data_file:
                json.dump(new_data, data_file, indent=4)
                # clear_entries()
        else:
            # Update the old data with the new data
            data.update(new_data)
            # Write the updated data to the file
            with open("data.json", mode='w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            clear_entries()
        # print(f"{user_website} | {user_password}")


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    to_find = entry_website.get()
    try:
        with open("data.json", mode='r') as user_data:
            data = json.load(user_data)
    except FileNotFoundError:
        messagebox.showinfo(title="None found", message="No data found.")
    else:
        if to_find in data:
            email_found = data[to_find]["email"]
            password_found = data[to_find]["password"]
            messagebox.showinfo(title="Details found", message=f"Email: {email_found}\nPassword: {password_found}")
        else:
            messagebox.showinfo(title="No details found", message="No details for the website found.")


# json.dump() --> write to json file (must be in a dict)
# Optional parameter in json.dump(), "indent", makes the .json file more readable.
# json.load() --> read from json file
# json.update() --> update a json file

# NOTE: USE try, except, else STATEMENTS WHEREVER YOU'RE UNABLE TO USE if-else STATEMENTS. if AND else STATEMENTS
# ARE MEANT TO CATCH THESE KIND OF THINGS MORE OFTEN. EXCEPTIONS ARE EXCEPTIONS, I.E THEY'RE MEANT TO OCCUR SOMETIMES,
# WHEREAS if-else SITUATIONS HAPPEN ALL THE TIME.

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=189)

canvas.create_image(100, 95, image=logo_img)
canvas.grid(column=1, row=0, columnspan=3)

# Labels
label_website = Label(text="Website:")
label_website.grid(row=1, column=0)
label_email = Label(text="Email:")
label_email.grid(row=2, column=0)
label_password = Label(text="Password:")
label_password.grid(row=3, column=0)

# Entries:
entry_website = Entry(width=35)
entry_website.focus()
entry_website.grid(row=1, column=1)
entry_email = Entry(width=35)
entry_email.grid(row=2, column=1)
entry_email.insert(END, "name@email.com")
entry_password = Entry(width=35)
entry_password.grid(row=3, column=1)

# Buttons:
button_search = Button(text="Search", width=15, command=find_password)
button_search.grid(row=1, column=3)
button_generate_password = Button(text="Generate Password", width=15, command=generate_password)
button_generate_password.grid(row=3, column=3, )

button_add = Button(text="Add", width=30, command=save)
button_add.grid(row=5, column=1, padx=3, pady=3)

window.mainloop()
