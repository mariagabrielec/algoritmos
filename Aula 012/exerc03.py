def num_bissexto(x):
    if x % 4 == 0:
        if x % 100:
            if x % 400:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0
x = int(input("Digite um número: "))

if (x % 4 == 0) or (x % 4 == 0 and x % 100 == 0 and x % 400 == 0):
    print(f"Usando a função: {num_bissexto(x)}")
    print("Entrou porque é Bissexto")
else:
    print("Não é bissexto")