import art
print(art.logo)

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
resp = 's'

def cesar(texto,chave,dir):

    i=1
    resultado = ""
    for letra in texto: 

        if letra not in alfabeto: 
            resultado += letra
        else:
            if dir == 1:
                posição = int(alfabeto.index(letra)) + chave 
            else: 
                posição = int(alfabeto.index(letra)) - chave 
            if posição < 26:
                resultado += alfabeto[posição]
            else:
                resultado += alfabeto[i]
                i +=1
        
    print(f"\nResultado de {''.join(mensagem)}: {resultado}") 

while resp == 's':

    direcao = int(input("Digite 1 para criptografar OU 2 para descriptografar: "))
    mensagem = list(input("Digite sua mensagem: ").lower())
    shift = int(input("chave: "))  
    shift = shift % 26

    cesar(mensagem,shift,direcao)

    resp = input("\nDeseja reiniciar o programa?(S/N)").lower()
    if resp == 'n':
        print("Até a próxima!")
