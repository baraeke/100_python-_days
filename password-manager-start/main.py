from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

password = ""

# ---------------------------- SEARCH MECHANISM ------------------------------- #
def search():
    search_website = website_input.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            website_details = data[search_website]
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found")
    except (KeyError, json.decoder.JSONDecodeError):
        messagebox.showerror(title="Invalid Entry", message="You have entered an in valid website\nPlease try again!")
    else:
        messagebox.showinfo(title=search_website, message=f"Email: {website_details['email']}\nPassword: {website_details['password']}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    global password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))] + [choice(symbols) for _ in range(randint(2, 4))] + [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)

    password_input.insert(0, f"{password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    global password
    website = website_input.get()
    email_username = email_username_input.get()
    pwd = password_input.get()
    new_data = {
        website: {
            "email": email_username,
            "password": pwd,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
        return

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            data.update(new_data)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        with open("data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)
    else:
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

    messagebox.showinfo(title=website, message="Saved successfully...")
    website_input.delete(0, END)
    password_input.delete(0, END)
    website_input.focus()
    email_username_input.delete(0, END)
    email_username_input.insert(END, "ifiemi2love@gmail.com")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50, bg="pink")

canvas = Canvas(width=200, height=200, bg="pink", highlightthickness= 0)
bg_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image = bg_img)
canvas.grid(row=0, column=1)

website_l = Label(text="Website: ", bg="pink")
website_l.grid(row=1, column=0)
website_input = Entry(width=19)
website_input.focus()
website_input.grid(row=1, column=1)

search_btn = Button(text="Search", width=13, bg="white", command=search)
search_btn.grid(row=1, column=2)

email_username_l = Label(text="Email/Username: ", bg="pink")
email_username_l.grid(row=2, column=0)
email_username_input = Entry(width=35)
email_username_input.insert(END, "ifiemi2love@gmail.com")
email_username_input.grid(row=2, column=1, columnspan=2)

password_l = Label(text="Password: ", bg="pink")
password_l.grid(row=3, column=0)
password_input = Entry(width=19)
password_input.grid(row=3, column=1)

generate_pwd = Button(text="Generate Password", width=13, bg="white", command=generate_password)
generate_pwd.grid(row=3, column=2)

add_btn = Button(text="Add", width=33, bg="white", command=add)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()