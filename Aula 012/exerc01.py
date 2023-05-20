def parouimpar(x):
    if x % 2 == 0:
        return True
    else:
        return False
n = int(input("Digite o número: "))
if parouimpar(n):
    print("O número é par")
else:
    print("O número é impar")