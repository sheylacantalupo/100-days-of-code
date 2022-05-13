import random
from art import logo

def dica(palpite, resposta, chances):
    if palpite > resposta:
        print("Muito alto")
        return chances -1
    elif palpite < resposta:
        print("Muito baixo")
        return chances-1
    else:
        print(f"Você acertou! A resposta é {resposta}\n\tFim de jogo")
        
def niveis():      
    nivel = {"facil":10 , "dificil":5}       
    dificuldade = str(input("\n Escolha o nível de dificuldade: 'facil' / 'dificil'  "))
    return nivel[dificuldade]
    
def game():
    print(logo)
    print("Bem-vindo ao jogo de adivinhação de números!")
    print("Estou pensando em um número entre 1 e 100.")
    
    resposta = random.randint(1, 100)
    print(f"resposta: {resposta}") 
    chances = niveis()
    
    palpite = 0
    while palpite != resposta:
        print(f"Você tem {chances} para adivinhar o número.")
        palpite = int(input("Palpite: "))
        chances = dica(palpite, resposta, chances)
        if chances == 0:
            print("Você ficou sem palpites, você perdeu")
            return
        elif palpite != resposta:
            print("\n\tAdivinhe novamente")

game()                
        
        
