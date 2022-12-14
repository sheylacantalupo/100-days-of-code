import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato)

def generate():
    word = input("Enter a word: ").upper()
    try:
        phoneticCodeWords = [nato[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate()
    else:
        print(phoneticCodeWords)


generate()
