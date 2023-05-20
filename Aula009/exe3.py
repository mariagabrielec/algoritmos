lista1=[]
lista2=[]
lista3=[]
for i in range(1,11):
    lista1.append(i)

for i in range(11,21):
    lista2.append(i)

for i in range(0,10):
    if i % 2 == 0:
        lista3.append(lista1[i])
    else:
        lista3.append(lista2[i])

print(lista1)
print(lista2)
print(lista3)