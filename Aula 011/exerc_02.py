idade_dic = {}
somaidades = 0
for i in range(10):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    somaidades += idade
    idade_dic[nome] = idade

media = somaidades / len(idade_dic)


for nome, idade2 in idade_dic.items():
    if idade2 > media:
        print(f"A idade do {nome} de {idade2} é maior que a média de {media}")


