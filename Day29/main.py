import math
import tkinter
from tkinter import *
from tkinter.ttk import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Gerenciador de Senhas")
window.config(padx=30, pady=30)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

botao_gerador = Button(text="Gerar Senha")
botao_gerador.grid(column=2, row=3)
botao_salvar = Button(text="Salvar", width=36)
botao_salvar.grid(column=1, row=4)

website_label = tkinter.Label(text="Website:", font=("Arial", 12, "bold"))
website_label.grid(column=0, row=1)
email_label = tkinter.Label(text="Email/username", font=("Arial", 12, "bold"))
email_label.grid(column=0, row=2)
senha_label = tkinter.Label(text="Senha:", font=("Arial", 12, "bold"))
senha_label.grid(column=0, row=3)

input1 = Entry(width=35)
input1.grid(column=1, row=1)
input2 = Entry(width=35)
input2.grid(column=1, row=2)
input3 = Entry(width=21)
input3.grid(column=1, row=3)





window.mainloop()
