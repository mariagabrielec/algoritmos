numero = 1
pares = 0
contador = 0 
while numero != 0:
    numero = int(input("Digite um número para calcular. E 0 para sair."))
    if numero % 2 == 0:
        pares += numero
        contador += 1

media = pares / contador

print(f"A soma dos {contador} numeros pares, resultam em uma média de: {media}")

