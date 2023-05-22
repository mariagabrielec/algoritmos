def primo(x):
    count = 0
    if x == 1:
        return True
    else:
        for i in range(1,x+1):
            if x % i == 0:
                count += 1
        if count == 2:
            return True
        else:
            return False

def total_primos(n):
    soma = 0
    total = 0
    atual = 0
    lista1 = []
    while total < n:
        if primo(atual):
            total += 1
            lista1.append(atual)
        atual += 1
    for i in lista1:
        soma += i
    return soma


print(total_primos(23*2+5))