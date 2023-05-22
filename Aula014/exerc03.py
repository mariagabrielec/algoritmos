numero = input("Digite um número: ")
lista = []
soma = 0
multiplicacao = 1
for i in numero:
    num = int(i)
    soma += num
    multiplicacao *= num

print(f"Soma: {soma}")
print(f"Multiplicação: {multiplicacao}")