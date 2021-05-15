from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


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

    if len(user_website) == 0 or len(user_password) == 0:
        messagebox.showwarning(title="Empty fields found!", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askyesnocancel(title=user_website,
                                          message=f"Here are the details: \n\nwebsite: {user_website}"
                                                  f" \npassword: {user_password} \n\nProceed to save?")
        if is_ok:
            with open("data.txt", mode='a') as data_writer:
                data_writer.write(
                    f"Website: {user_website} | Username/Email: {user_email} | Password: {user_password}\n")
                entry_website.delete(first=0, last=END)
                # entry_email.delete(first=0, last=END)
                entry_password.delete(first=0, last=END)
                entry_website.focus()
            # print(f"{user_website} | {user_password}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=189)

canvas.create_image(100, 95, image=logo_img)
canvas.grid(column=1, row=0)

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
entry_website.grid(row=1, column=1, columnspan=2)
entry_email = Entry(width=35)
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(END, "name@email.com")
entry_password = Entry(width=35)
entry_password.grid(row=3, column=1, columnspan=2)

# Buttons:
button_generate_password = Button(text="Generate Password", width=40, command=generate_password)
button_generate_password.config(padx=10, pady=10)
button_generate_password.grid(row=4, column=0, columnspan=3, padx=3, pady=3)

button_add = Button(text="Add", width=40, command=save)
button_add.config(padx=10, pady=10)
button_add.grid(row=5, column=0, columnspan=3, padx=3, pady=3)

window.mainloop()
