frutas = ["Maçã", "Pera", "Laranja"]


def make(index):
    try:
        fruta = frutas[index]
    except IndexError:
        print("Fruit pie")

    else:
        print(fruta + " pie")

make(4)