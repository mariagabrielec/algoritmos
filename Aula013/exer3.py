def triangular(n):
    for i in range(1,n-2):
        a = i
        b = i + 1
        c = b + 1
        resultado = a * b * c
        if resultado == n:
            return True
    return False

print(triangular(120))