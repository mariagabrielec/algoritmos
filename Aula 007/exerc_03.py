pesosoma = 0
alturasoma = 0
lista = []
for x in range(1,21):
     peso = int(input(f'Digite o {x}º peso: '))
     altura = int(input(f'Digite o {x}º peso: '))
     pesosoma += peso
     alturasoma += altura
     imc = peso / (altura*2)
     lista.append(imc)

pesomedio = pesosoma / 20
alturamedia = alturasoma / 20
maximo = max(lista)
minimo = min(lista)
print(f'A média dos pesos é {pesomedio:.2f}')
print(f'A média das alturas é {alturamedia:.2f}')
print(f'O maior IMC é {maximo:.2f}')
print(f'O menor IMC é {minimo:.2f}')

