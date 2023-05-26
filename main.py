from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
timer = None
language = "French"
card = None
window = Tk()
window.title("Flashy")
window.config(height=526, width=800, padx=50, pady=50, bg=BACKGROUND_COLOR)

data = pandas.read_csv("french_words.csv")
to_learn = data.to_dict(orient="records")


def flip():
    global language
    global card
    language = "English"
    card_front.itemconfig(card_title, text="English")
    card_front.itemconfig(image, image=back_logo)
    card_front.itemconfig(card_word, text=card[language])
    card_front.itemconfig(card_title, fill="white")
    card_front.itemconfig(card_word, fill="white")


def is_known():
    global card
    to_learn.remove(card)
    next_card()


def wrong():
    global timer
    global language
    global card
    language = "French"
    card_front.itemconfig(card_title, text="French")
    card_front.itemconfig(card_word, text=card[language])
    card_front.itemconfig(image, image=front_logo)
    card_front.itemconfig(card_word, fill="black")
    card_front.itemconfig(card_title, fill="black")
    timer = window.after(5000, flip)

def next_card():
    global timer
    global language
    global card
    language = "French"
    card = random.choice(to_learn)
    card_front.itemconfig(card_title, text="French")
    card_front.itemconfig(card_word, text=card[language])
    card_front.itemconfig(image, image=front_logo)
    card_front.itemconfig(card_word, fill="black")
    card_front.itemconfig(card_title, fill="black")
    timer = window.after(5000, flip)





front_logo = PhotoImage(file="./images/card_front.png")
back_logo = PhotoImage(file="./images/card_back.png")

card_front = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
image = card_front.create_image(400, 263, image=front_logo)
card_front.grid(column=0, row=0, columnspan=2)


card_title = card_front.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
card_word = card_front.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")

check = PhotoImage(file="./images/right.png")
X = PhotoImage(file="./images/wrong.png")

right = Button(image=check, highlightthickness=0, border=0, command=is_known)
right.grid(column=1, row=1)

wrong = Button(image=X, highlightthickness=0, border=0, command=wrong)
wrong.grid(column=0, row=1)

next_card()


window.mainloop()