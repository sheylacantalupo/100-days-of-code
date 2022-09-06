import tkinter


def button_cliked():
    label_1 = tkinter.Label(text=input.get() + " Miles is equal to", font=("Arial", 16, "bold"))
    label_1.place(x=52, y=78)
    label_2 = tkinter.Label(text=str(miles_to_km()) + " Km", font=("Arial", 16, "bold"))
    label_2.place(x=100, y=120)


def miles_to_km():
    ml = int(input.get())
    km = round(ml/0.62137, 2)
    return km


window = tkinter.Tk()
window.title("Unit Converter")
window.minsize(width=300, height=100)

input = tkinter.Entry(width=15)
input.place(x=50, y=15)

miles = tkinter.Label(text="Miles", font=("Arial", 12))
miles.place(x=110, y=15)

button = tkinter.Button(text="Calculate", command=button_cliked)
button.place(x=170, y=13)

def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())


spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


window.mainloop()

# my_label.pack(side="left")
# my_label.place(x=10, y=0)