BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

from tkinter import *
import pandas as pd
import random

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/HP_ Página1.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    # transformar numa lista de dicts
    to_learn = data.to_dict(orient="records")
# print(to_learn[0]["English"])



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card["English"])
    canvas.itemconfig(card_bg, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="Portuguese")
    canvas.itemconfig(card_word, text=current_card["Portuguese"])
    canvas.itemconfig(card_bg, image=card_back)

def is_know():
    # remover a palavra conhecida do baralho
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Anki - Harry Potter")
# pixels de alcochoamento
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# altura e largura compatíveis com a imagens do cartão
canvas = Canvas(width=800, height=526)
# imagens que serão alternadas
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
# colocando a imagem no centro do canvas
card_bg = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 20, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 30, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=is_know)
check_button.grid(row=1, column=1)

next_card()

window.mainloop()