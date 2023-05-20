n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
print('''Escolha a operação desejada: 
    1. Média entre os números digitados
    2. Diferença do maior pelo menor
    3. Produto entre os números digitados
    4. Divisão do primeiro pelo segundo''')
escolha = int(input())

if escolha == 1:
    print(f"O resultado da média é: {(n1+n2)/2}")
elif escolha == 2:
    print(f"O resultado da diferença é: {(n1-n2)}")
elif escolha == 3:
    print(f"O resultado da diferença é: {(n1*n2)}")    
else:
    print(f"O resultado da diferença é: {(n1/n2)}")