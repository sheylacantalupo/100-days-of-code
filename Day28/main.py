from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
# ---------------------------- CONSTANTS ------------------------------- #

rosa = "#e2979c"
vermelho = "#e7305b"
verde = "#9bdeac"
amarelo = "#f7f5dd"
fonte = "Courier"
trabalho = 25
pausa_curta = 5
pausa_longa = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

#
#---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")
window.resizable(False, False)
window.config(padx=100, pady=50, bg=amarelo)

label = Label(text="TIMER", background=amarelo, foreground=verde, font=(fonte, 40))
label.grid(column=1, row=0)
#o bg canvas da mesma cor do window
canvas = Canvas(width=220, height=224, bg=amarelo, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(110, 130, text="00:00", fill="white", font=(fonte, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start")
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset")
reset_button.grid(column=2, row=2)

check = Label(text="✔", background=amarelo, foreground=verde)
check.grid(column=1, row=3)



window.mainloop()