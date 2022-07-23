from replit import clear
import art
resp = 'sim'
lances = {}

def maiorLance(bibliotecaLances):
    maior_atual = 0
    vencedor = ""
    for x in bibliotecaLances:
        lance = bibliotecaLances[x]
        if lance > maior_atual:
            maior_atual = lance
            vencedor = x
    print()        
    print(f"O vencedor é {vencedor} com o lance de  R${maior_atual}")    

print(art.logo)

while resp == 'sim':
    Nome = input("Qual o seu nome? ")
    Lance = int(input("Lance: R$"))
    lances[Nome] = Lance
    resp = input("Mais alguém irá realizar uma oferta? Escreva 'sim' OU 'não' ")
    if resp != 'sim':
        print(art.logo)
        maiorLance(lances)
    else: 
        clear()
