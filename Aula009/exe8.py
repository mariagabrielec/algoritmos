lista = []
listaordenada = []
for i in range(0,5):
    adc = int(input("Digite um número inteiro: "))
    lista.append(adc)

maior = 0
index = 0
for n in lista:
    if n > maior:
        listaordenada.insert(index,n)
        maior = n
    index += 1
print(listaordenada)