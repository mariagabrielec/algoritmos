lista1 = []
for i in range(3):
    item = int(input("Digite um elemento para a lista1: "))
    lista1.append(item)
lista2 = []
for b in range(3):
    item2 = int(input("Digite um elemento para a lista2: "))
    lista2.append(item2)

conjunto1 = set(lista1)
conjunto2 = set(lista2)
conjunto3 = conjunto1.union(conjunto2)
print(conjunto1)
print(conjunto2)
print(conjunto3)