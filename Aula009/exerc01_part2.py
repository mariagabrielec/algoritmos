matriz = []
for i in range(2):
    linha = []
    for j in range(2):
        elemento = int(input(f"Digite o elemento {i+1},{j+1}: "))
        linha.append(elemento)
    matriz.append(linha)

print(f"1,1 = {matriz[0][0]}")
print(f"1,2 = {matriz[0][1]}")
print(f"2,1 = {matriz[1][0]}")
print(f"2,2 = {matriz[1][1]}")