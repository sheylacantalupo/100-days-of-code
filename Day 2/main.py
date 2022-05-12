print("Bem-vindo à calculadora de gorjetas!\n")
conta = float(input("Qual foi a conta total?\n"))
porcentagem = int(input("Quanta gorjeta você gostaria de dar? 10, 12 ou 15?\n"))
pessoas = int(input("Quantas pessoas para dividir a conta?\n"))
print(type(conta))
print(type(porcentagem))
print(type(pessoas))


gorjeta = conta * porcentagem / 100

valor_pessoa = (conta + gorjeta)/ pessoas

print(f"Cada pessoa deve pagar R${round(valor_pessoa,2)}")

print(type(valor_pessoa))