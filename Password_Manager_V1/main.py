# Hello, this code is from Dr. Angela Yu's course, which you can find on Udemy: https://www.udemy.com/course/100-days-of-code/
# This is my version of the program.

from tkinter import *
from tkinter import messagebox
import pyperclip
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    entry_password.delete(0,END)
    entry_password.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = entry_website.get()
    email_username = entry_email_username.get()
    password = entry_password.get()

    if website.strip() and email_username.strip() and password.strip():
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered:\nEmail/Username: {email_username}\nPassword: {password}\nIs it ok to save?')
        if is_ok:
            messagebox.showinfo(title=website, message='Saved successfully')
            with open('Password_Manager_V1\data.txt', mode='a') as data:
                data.write(f'{website}, {email_username}, {password}\n')
            entry_website.delete(0, END)
            entry_email_username.delete(0, END)
            entry_password.delete(0, END)
    else:
        messagebox.showwarning(title=website, message='Please fill all the fields.')

# ---------------------------- UI SETUP ------------------------------- #
 
window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)
 
canvas = Canvas(width=200, height=200)
tomato_img = PhotoImage(file=r'Password_Manager_V1\logo.png')
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)
 
label_website=Label(text="Website:")
label_website.grid(column=0, row=1)
 
entry_website = Entry()
entry_website.grid(column=1, row=1, columnspan=2, sticky="EW")
 
label_email_uname = Label(text="Email/Username:")
label_email_uname.grid(column=0, row=2)
 
entry_email_username = Entry()
entry_email_username.grid(column=1, row=2, columnspan=2, sticky="EW")
#entry_email_username.insert(0, 'email@gmail.com')
 
label_password = Label(text="Password:")
label_password.grid(column=0, row=3)
 
entry_password = Entry()
entry_password.grid(column=1, row=3, sticky="EW")
 
generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3, sticky="EW")
 
add_btn = Button(text="Add", width=35, command=save_data)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")

mainloop()