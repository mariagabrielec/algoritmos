
matriz = []
for i in range(5):
    linha = []
    for j in range(5):
        elemento = float(input(f"Digite o elemento {i+1},{j+1}: "))
        linha.append(elemento)
    matriz.append(linha)

soma = 0
contagem = 0
for i in range(1, 5, 2):
    for j in range(5):
        soma += matriz[i][j]
        contagem += 1

# Calcula a média
if contagem > 0:
    media = soma / contagem
else:
    media = 0


print("A média dos elementos das linhas pares é:", media)

