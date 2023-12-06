from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    data_cards = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    cards_dict = original_data.to_dict(orient="records")
else:
    cards_dict = data_cards.to_dict(orient="records")


def random_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(cards_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(card_background, image=front_card)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card['English'], fill="black")
    canvas.itemconfig(card_background, image=back_card)


def is_known():
    cards_dict.remove(current_card)
    data = pandas.DataFrame(cards_dict)
    data.to_csv("data/words_to_learn.csv", index=False)

    random_card()


window = Tk()
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
window.title("Flashcards!")

canvas = Canvas(width=800, height=526)
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
sei = PhotoImage(file="images/right.png")
nao_sei = PhotoImage(file="images/wrong.png")

flip_timer = window.after(3000, func=flip_card)

card_background = canvas.create_image(480, 263, image=front_card)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

unknown_button = Button(image=nao_sei, highlightthickness=0, command=random_card)
unknown_button.grid(row=1, column=0)

known_button = Button(image=sei, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

random_card()

window.mainloop()
