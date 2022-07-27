import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data)

nato = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()

phoneticCodeWords = [nato[letter] for letter in word]
print(phoneticCodeWords)