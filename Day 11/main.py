import random #ok
from replit import clear #ok
from art import logo #ok

def distribuição_cartas(): #ok
    cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    carta = random.choice(cartas)
    return carta
def calculador_pontos(cartas): #ok  
    if sum(cartas) == 21 and len(cartas)==2: # Ás + 10
        return 0 #0 representará um blackjack no nosso jogo
    if 11 in cartas and sum(cartas)>21: #remover o 11 add 1
        cartas.remove(11)
        cartas.append(1)
    return sum(cartas)  
        
def comparar_pontos(pontos_us,pontos_pc):
    if pontos_us == pontos_pc:
        return "Empate."
    if pontos_us > 21 and pontos_pc > 21:
        return "Você perdeu!"
    elif pontos_pc == 0:
        return "Você perdeu! O computador fez Blackjack "
    elif pontos_us == 0:
        return "Você ganhou! Fez Blackjack"
    elif pontos_us>21:
        return "Você perdeu, fez mais de 21 pontos!"
    elif pontos_pc>21:
        return "Você ganhou!"
    else:
        if pontos_us > pontos_pc:
            return "Você ganhou!"
        else:
            return "Você perdeu!"
def rodar_jogo():
    print(logo) 
    cartas_usuario = [] 
    cartas_computador = [] 
    fim_de_jogo = False

    for x in range(2): 
        cartas_usuario.append(distribuição_cartas())
        cartas_computador.append(distribuição_cartas())
    
    while not fim_de_jogo:
        pontos_usuario = calculador_pontos(cartas_usuario)
        pontos_computador = calculador_pontos(cartas_computador)  
        print(f" Suas cartas{cartas_usuario} PONTUAÇÃO ATUAL:{pontos_usuario}")
        print(f" 1º Carta do computador: {cartas_computador[0]}")
        if pontos_usuario == 0 or pontos_computador == 0 or pontos_usuario > 21:
            fim_de_jogo = True
        else:
            adicionar = input("Deseja adicionar mais uma carta? s/n ")
            if adicionar == 's':
                cartas_usuario.append(distribuição_cartas())
            else:
                fim_de_jogo = True
        
    while pontos_computador!=0 and pontos_computador<17:
        cartas_computador.append(distribuição_cartas())
        pontos_computador = calculador_pontos(cartas_computador) 

    print(f" \nSuas cartas finais: {cartas_usuario}, Pontuação final: {pontos_usuario}")
    print(f" Cartas finais computador: {cartas_computador}, Pontuação final: {pontos_computador}")
    print(comparar_pontos(pontos_usuario, pontos_computador))

while input("\nJogar Blackjack? s/n  ") == "s":
    clear()
    rodar_jogo()
