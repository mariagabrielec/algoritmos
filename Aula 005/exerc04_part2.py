x = float(input("Digite o valor do lado X: "))
y = float(input("Digite o valor do lado Y: "))
z = float(input("Digite o valor do lado Z: "))

if x + y > z and x + z > y and y + z > x:
    if x == y == z:
        print("É um triângulo equilátero.")
    elif x == y or x == z or y == z:
        print("É um triângulo isósceles.")
    else:
        print("É um triângulo escaleno.")
else:
    print("Os valores fornecidos não formam um triângulo.")
