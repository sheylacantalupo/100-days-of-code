# file not found


# try:
#     file = open('a_file.txt', encoding='UTF-8')
#     a_dicionario = {"a": "value"}
#     print(a_dicionario["a"])
#
# except FileNotFoundError:
#     file = open('a_file.txt', 'w', encoding='UTF-8')
#     file.write("isso aqui é um exemplo...")
#
# except KeyError as error_message:
#     print(f"A chave {error_message} não existe")
#
# else:
#     content = file.read()
#     print(content)
#
# finally:
#     file.close()


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Altura maior de 3 metros.")

imc = weight/(height * height)
print(imc)