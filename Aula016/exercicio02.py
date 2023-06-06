n = 1
lista_individual = []
lista_completa = []
gasolina = 5.65
maior_consumo = ""
maximo = 0
carro = ""
while n < 4:
    print(f"Veículo {n}")
    nome = input("Nome: ")
    km = float(input("Km por litro: "))
    if km > maximo:
        maximo = km
        carro = nome
    distancia = 1000 / km
    valor = distancia * gasolina
    lista_individual.append(nome)
    lista_individual.append(km)
    lista_individual.append(distancia)
    lista_individual.append(valor)
    lista_completa.append(lista_individual)
    n += 1
    lista_individual = []

n = 0
largura = 1
print("Relatório Final")
for i in lista_completa:
    print(f"{largura} - {i[n]:<6} - {i[n+1]:12.1f} KM - {i[n+2]:8.2f} Litros - R$ {i[n+3]:8.2f}")
    largura += 1

print(f"O menor consumo é do {carro}")
