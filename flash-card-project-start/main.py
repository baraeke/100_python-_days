from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- SAVE PROGRESS ------------------------------- #
def save_progress():
    global french_word
    global data

    data = data[data["French"] != french_word]
    data = data.reset_index(drop=True)
    data.to_csv("data/words_to_learn.csv", index=False)

# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    global french_word
    global ft_img

    canvas.itemconfig(card, image=ft_img)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(words, text=f"{data[data['French'] == french_word]['English'].values[0]}", fill="white")

# ---------------------------- PRESS ✓ BUTTON ------------------------------- #
def check_btn():
    global french_word
    global bg_image
    global flip_timer
    window.after_cancel(flip_timer)

    save_progress()

    if not data.empty:
        french_word = choice(data["French"])
        canvas.itemconfig(card, image=bg_image)
        canvas.itemconfig(title, text="French", fill="black")
        canvas.itemconfig(words, text=f"{french_word}", font=("Arial", 60, "bold"), fill="black")
        flip_timer = window.after(3000, flip_card)
    else:
        canvas.itemconfig(title, text="Congratulations!", fill="black")
        canvas.itemconfig(words, text="You've learned all the words 🎉", font=("Arial", 25, "bold"), fill="black")

# ---------------------------- PRESS X BUTTON ------------------------------- #
def x_btn():
    global french_word
    global bg_image
    global flip_timer
    window.after_cancel(flip_timer)

    if not data.empty:
        french_word = choice(data["French"])
        canvas.itemconfig(card, image=bg_image)
        canvas.itemconfig(title, text="French", fill="black")
        canvas.itemconfig(words, text=f"{french_word}", font=("Arial", 60, "bold"), fill="black")
        flip_timer = window.after(3000, flip_card)
    else:
        canvas.itemconfig(title, text="Congratulations!", fill="black")
        canvas.itemconfig(words, text="You've learned all the words 🎉", font=("Arial", 25, "bold"), fill="black")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

try:
    data = pandas.read_csv("data/words_to_learn.csv")
    french_word = choice(data["French"])
except (FileNotFoundError, IndexError):
    data = pandas.read_csv("data/french_words.csv")
    french_word = choice(data["French"])


canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
bg_image = PhotoImage(file="images/card_front.png")
card = canvas.create_image(400, 263, image=bg_image)
title = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"), fill="black")
words = canvas.create_text(400, 270, text=f"{french_word}", font=("Arial", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

ft_img = PhotoImage(file="images/card_back.png")

flip_timer = window.after(3000, flip_card)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_image, highlightthickness=0, command=x_btn)
wrong_btn.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_btn = Button(image=right_image, highlightthickness=0, command=check_btn)
right_btn.grid(row=1, column=1)

window.mainloop()
