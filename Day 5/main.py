#Projeto - Gerador de senhas
import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

numeros_simbolos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Bem-vindo ao Gerador de Senhas!")
n_letras= int(input("Quantas letras você gostaria na sua senha?\n")) 
n_numeros = int(input(f"Quantos números você gostaria?\n")) 
n_simbolos = int(input(f"Quantos símbolos você gostaria?\n"))
print("\n")
senha = []
for l in range(0 , n_letras):                      
 posicao_atual = random.randint(0,51)
 senha.append(letras[posicao_atual])
for n in range(0 , n_numeros):
  posicao_atual = random.randint(0,9)
  senha.append(numeros[posicao_atual])
for n in range(0 , n_simbolos):
  posicao_atual = random.randint(0,8)
  senha.append(simbolos[posicao_atual])

senhaConcatenada = "".join(senha)
#print(senhaConcatenada)

posicoesAleatorias = []
while len(posicoesAleatorias) != len(senha): 
  r = random.randint(0, len(senha)-1)
  if r not in posicoesAleatorias: #add se não existir na lista

    posicoesAleatorias.append(r)
# print(posicoesAleatorias)
senhaFinal = []
for x in range(0 , len(senha)):
  senhaFinal.append(senha[posicoesAleatorias[x]])
senhaFinalConcatenada = "".join(senhaFinal)
print(senhaFinalConcatenada)
