
matriz = []
for i in range(2):
    linha = []
    for j in range(2):
        elemento = int(input(f"Digite o elemento {i+1},{j+1}: "))
        linha.append(elemento)
    matriz.append(linha)


maior_elemento = matriz[0][0]
for linha in matriz:
    for elemento in linha:
        if elemento > maior_elemento:
            maior_elemento = elemento


matriz_resultante = []
for linha in matriz:
    linha_resultante = []
    for elemento in linha:
        elemento_resultante = elemento * maior_elemento
        linha_resultante.append(elemento_resultante)
    matriz_resultante.append(linha_resultante)


for i in range(2):
    for j in range(2):
        print(f"{matriz_resultante[i][j]}", end=" ")
    print()
