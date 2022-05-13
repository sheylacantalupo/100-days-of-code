#CALCULADORA
from art import logo

def soma(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mult(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

operacoes ={
"+": soma,
"-":sub,
"*":mult, 
"/":div
}

def calculadora(): 
    print(logo)
    numero1 = float(input("Qual o primeiro número? "))
    for operacao in operacoes:
        print(operacao)
    r='s'
    while r == 's':
    
        simbolo_da_operaçao = input("Escolha uma das  operações acima: ")
        numero2 = float(input("Qual o próximo número? "))
        #calculo vai receber a função referente a operação escolhida
        calculo = operacoes[simbolo_da_operaçao]
        resp = calculo(numero1,numero2)
        print(f"{numero1} {simbolo_da_operaçao} {numero2}= {resp}")
    
        r = input(f"Digite 's' para calcular com {resp} ou 'n' para um novo cálculo: ")
        if r == 's':
            numero1 = resp
        else: 
            print("\nNovo cálculo")
            calculadora()

calculadora()