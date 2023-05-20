matriz = []
for i in range(10):
    linha = []
    for j in range(10):
        elemento = int(input(f"Digite o elemento {i+1},{j+1}: "))
        linha.append(elemento)
    matriz.append(linha)


maior_elemento = matriz[0][0]
posicao_maior = (0, 0)
for i in range(10):
    for j in range(10):
        if matriz[i][j] > maior_elemento:
            maior_elemento = matriz[i][j]
            posicao_maior = (i, j)


linha_maior, coluna_maior = posicao_maior
print(f"A posição do maior elemento ({maior_elemento}) é: ({linha_maior+1}, {coluna_maior+1})")


