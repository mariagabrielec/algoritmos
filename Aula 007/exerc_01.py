import math
n = int(input("Entre o valor inteiro positivo: "))
e = 0
for i in range(1,n+1):
    e += math.pow(2,i)
print(f'O valor de E é = {e:.2f}')