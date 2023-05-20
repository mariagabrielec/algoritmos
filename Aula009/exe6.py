from random import randint
count2or12 = 0
soma7 = 0
for i in range(0,30000):
    dado1 = randint(1,7)
    dado2 = randint(1,7)
    somadados = dado1 + dado2
    if somadados == 2 or somadados == 12:
        count2or12 += 1
    if somadados == 7:
        soma7 +=1

porcentagem7 = (soma7/ 30000)*100
if porcentagem7 == (1/6*100):
    print(f'A soma de 2 e 12 aparece {somadados} vezes. A soma de 7 aparece {soma7} vezes, sendo {porcentagem7:.2f} % das jogadas o que representa 1/6 das jogadas.')
else:
    print(f'A soma de 2 e 12 aparece {somadados} vezes. A soma de 7 aparece {soma7} vezes, sendo {porcentagem7:.2f} % das jogadas o que NÃO representa 1/6 das jogadas.')

