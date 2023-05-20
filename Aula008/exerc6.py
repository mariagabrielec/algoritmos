palavra = input("Digite um Palíndromo: ")
novapalavra = palavra[::-1]
if novapalavra != palavra:
    print("Não se trata de um Palíndromo")
else:
    print(f"A palavra {palavra} é a mesma ao contrário.")