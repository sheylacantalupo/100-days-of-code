import game_data
import random
import art
import os
#função para sortear Instagram, retorna o dicionário - dict
def insta():
    tamanho = len(game_data.data)
    #começa pela posição 1 para garantir que a conta do instagram não seja sorteada
    numero = random.randint(0 , tamanho-1)
    return game_data.data[numero]
    
#função para comparar o número de seguidores de 2 instagrans,
    #retorna a resposta correta da rodada - str
def maior(instaA , instaB ): 
    if instaA > instaB:
        return 'A' 
    else:
        return 'B'
        
#função para substituir o insta A - dict
def substituir_A(instaA , instaB ):
    if instaA['follower_count'] > instaB['follower_count']:
        return instaA 
    else:
        return instaB
        
#função para comparar a resposta do computador com a do usuário
#retorna a pontuação do usuráio caso tenha acertado - int
def resposta(resp , respUser, score):
    if resp == respUser:
        score = score+1
        print(f"Correto! Sua pontuação atual: {score}")
        return score
    else:
        score = 0
        print(f"Resposta errada!")
        return score

def imprimir_dados(insta):
    print(f"{insta['name']},{insta['description']}, {insta['country']}.")
    
def jogo():
    novoJogo = 's'
    while novoJogo == 's':
        print(art.logo)
        pont = 0
        fim = False
        A = insta()
        B = insta()  
        while fim != True:
            print("Comparar A: ")
            imprimir_dados(A)
            print(art.vs)
            print("Com B: ")
            imprimir_dados(B)
            resp = maior(A['follower_count'] ,B['follower_count'] )
            respUser = input("\n\tQuem tem mais seguidores? Digite 'A'/'B' ")
            respUser = respUser.upper()
            os.system('clear')
            pont = resposta(resp,respUser,pont)
            A = substituir_A(A,B)
            B = insta()
            if pont == 0:
                fim = True
                novoJogo = input("Deseja jogar novamente? Digite s/n ")
                os.system('clear')
            else:
                fim = False
                
jogo()