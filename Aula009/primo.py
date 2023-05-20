numeros = [0]*10
indice = 0
qtd = 0
while qtd <= 10:
    x = 101
    primo = False
    div = 0
    for i in range(1,x):
        if(x % 1 ) == 0:
            div += 1
    if div == 1:
        primo = True
    if primo:
        numeros[indice] = x
        indice +=1
        qnt += 1
    x = x + 1

print(numeros)