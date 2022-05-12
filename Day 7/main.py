import hangman_art
import hangman_words
import random
import os

print(hangman_art.logo)

fim_de_jogo = False
vidas = 6
letras_escolhidas = []
palavra_sorteada = random.choice(hangman_words.word_list)
tam_palavra_sorteada = len(palavra_sorteada)

display = []
for n in range(0 , len(palavra_sorteada)):
    display.append("_")
print(f"{' '.join(display)}")

while display.count("_") != 0:
    letra_atual = input("\n*** Escolha uma letra ***: ")
    letra_atual.lower()

    letras_escolhidas.append(letra_atual)

    for posicao in range(tam_palavra_sorteada):
        letra = palavra_sorteada[posicao]

        if letra == letra_atual:
            escolha = True
            display[posicao] = letra_atual 
        else:
            escolha = False
            # vidas -= 1   NÃO FUNCIONOUUUU
    # 2ª alternativa        
    if letra_atual not in palavra_sorteada:
        vidas -= 1   
        print(f"A letra {letra_atual} não está na palavra")
    os.system('clear')

    print(f"Letras já escolhidas: {'-'.join(letras_escolhidas)}")

    print(hangman_art.stages[vidas])

    print(f"{' '.join(display)}")
    if vidas != 0:
        print(f"Você ainda tem {vidas} vidas\n")
    else:
        print("Suas vidas acabaram\n")
    

    if display.count("_") == 0:
        print("VOCÊ GANHOU!!")
    elif vidas == 0:
        print("VOCÊ PERDEU!")
        print(f"A palavra era: {palavra_sorteada}")
    