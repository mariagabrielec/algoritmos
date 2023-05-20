listaPalavras = []
for i in range(1,21):
    palavra = input("Insera uma palavra de no max 10 carac: ")
    while len(palavra) > 10:
        palavra = input("Erro. Insera uma palavra de no max 10 carac: ")
    palavra = palavra[::-1]
    listaPalavras.append(palavra)


print(listaPalavras)