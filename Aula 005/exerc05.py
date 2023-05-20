anonasc = int(input("Digite o seu ano de nascimento: "))
anoatual = int(input("Digite o ano atual:  "))
idade = anoatual - anonasc
if idade > 15 and idade > 17:
    print("Você já pode votar e tirar carteira de habilitação!")
elif idade > 15:
    print("Você já pode votar!")
else:
    print("Você ainda não pode votar :(")
