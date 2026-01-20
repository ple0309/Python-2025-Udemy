from tkinter import *
#Because import * from tkinter not including messagebox
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #List comprehension
    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    password_entry.insert(0,password)

    #Using pyperclip to copy the password into clipboard then ctrl + v to paste.
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    website = website_entry.get()
    email = email_entry.get()
    password= password_entry.get()

    if len(website) == 0 or len(password) == 0:

        messagebox.showinfo(title="Oops", message="Please dont' leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: "
                                                              f"\nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", mode='a') as file:
                file.write(f"{website} | {email} | {password}\n")

                #Clear the input by take from first and last index 0 and END in this scenario.
                website_entry.delete(0,END)
                password_entry.delete(0,END)
                website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady= 50)

canvas = Canvas(width=200,
                height=200)
mypass_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image= mypass_img)
canvas.grid( row=0,column=1)

#Label
website_label = Label(text="Website:")
website_label.grid( row=1,column=0)


email_username = Label(text="Email/Username:")
email_username.grid( row=2,column=0)

password_label = Label(text="Password:")
password_label.grid( row=3,column=0)

#Entry
website_entry = Entry(width=52)
website_entry.grid(row=1, column=1,columnspan=2)
website_entry.focus()

email_entry = Entry(width=52)
email_entry.grid(row=2,column=1,columnspan=2)
#insert END will add the string after the current index.
#insert 0 will add the start of entry.
email_entry.insert(0, "ple030999@gmail.com")

password_entry = Entry(width=33)
password_entry.grid(row=3,column=1)

#Button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid( row=3,column=2)

add_button = Button(text="Add",width=44, command=add_data)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()