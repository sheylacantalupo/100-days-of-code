
with open("./Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()  # list of names

with open("./Input/Letters/starting_letter.txt", "r") as letter_file:
    letter = letter_file.read()


for name in names:
    s_name = name.strip()
    new_latter = letter.replace("[name]", s_name)
    arquivo = open(f"./Output/ReadyToSend/letter_for_{s_name}.txt", "a")
    arquivo.write(new_latter)




