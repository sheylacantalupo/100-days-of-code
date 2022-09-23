import math
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
reps = 0
Work_min = 25
Short_break_min = 5
Long_break_min = 20
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="TIMER")
    check.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = Work_min * 60
    short_break_sec = Short_break_min * 60
    long_break_sec = Long_break_min * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="BREAK", foreground=vermelho)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="BREAK", foreground=rosa)
    else:
        count_down(work_sec)
        label.config(text="WORK", foreground=verde)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    min = math.floor(count/60)
    sec = count % 60
    if sec <10:
        sec = f"0{sec}"

    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
            check.config(text=mark)


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
timer_text = canvas.create_text(110, 130, text="00:00", fill="white", font=(fonte, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check = Label(background=amarelo, foreground=verde)
check.grid(column=1, row=3)


text="✔",
window.mainloop()