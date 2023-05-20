ano = int(input("Digite o seu ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade = ano_atual - ano
meses = idade * 12
dias = idade * 365
semanas = idade * 53
print("Idade: ", idade)
print("Idade em Meses: ", meses)
print("Idade em Dias: ", dias)
print("Idade em Semanas: ", semanas)
