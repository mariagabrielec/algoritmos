n = int(input("Digite o número que deseja saber o fatorial: "))
while True:
    if n >= 0:
        break
    n = int(input("Valor inválido. Digite o número que deseja saber o fatorial: "))

x = n - 1
if n == 0:
    print(f'O fatorial é: 1')
else:
    while x >= 1:
        n = n * x
        x = x - 1
    print(f'O fatorial é: {n}')
