import tkinter


def button_cliked():
    label_4.config(text=miles_to_km())


def miles_to_km():
    miles = int(input.get())
    km = round(miles/0.62137, 2)
    return km


window = tkinter.Tk()
window.title("Unit Converter")
window.minsize(width=200, height=200)

label_1 = tkinter.Label(text="Miles", font=("Arial", 16, "bold"))
label_1.grid(column=2, row=0)

label_2 = tkinter.Label(text="Km", font=("Arial", 16, "bold"))
label_2.grid(column=2, row=1)

label_3 = tkinter.Label(text="is equal to", font=("Arial", 16, "bold"))
label_3.grid(column=0, row=1)

label_4 = tkinter.Label(text="", font=("Arial", 12, "bold"))
label_4.grid(column=1, row=1)

button = tkinter.Button(text="Calculate", command=button_cliked)
button.grid(column=1, row=2)

input = tkinter.Entry(width=20)
input.grid(column=1, row=0)

window.mainloop()

# my_label.pack(side="left")
# my_label.place(x=10, y=0)