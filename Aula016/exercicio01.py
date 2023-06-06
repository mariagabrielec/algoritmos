lista_completa = []
lista_individual = []
def pegar_peso():
    while True:
        try:
            peso = float(input("Digite o seu peso: "))
            return peso
        except:
            print("Digite um peso válido")
        else:
            if peso:
                return peso
            else:
                print("Digite um peso válido")

def pegar_altura():
    while True:
        try:
            altura = int(input("Digite a sua altura: "))
        except:
            print(f"Altura não válida")
        else:
            if altura:
                return altura
            else:
                print("Digite uma altura válida")
def pegar_idade():
    while True:
        try:
            idade = int(input("Digite a sua idade: "))
        except:
            print(f"Idade não válida")
        else:
            if idade:
                return idade
            else:
                print("Digite uma idade válida")

def pegar_sobrenome():
    while True:
        try:
            sobrenome = input("Digite o sobrenome: ")
        except:
            print(f"Sobrenome não válido")
        else:
            if sobrenome:
                if sobrenome.isalpha():
                    return sobrenome
                else:
                    print("Digite um sobrenome válido.")
            else:
                return sobrenome

loop = True
while loop == True:
    sobrenome = pegar_sobrenome()
    if sobrenome == "":
        break
    lista_individual.append(sobrenome)
    lista_individual.append(pegar_idade())
    lista_individual.append(pegar_altura())
    lista_individual.append(pegar_peso())
    lista_completa.append(lista_individual)
    lista_individual = []

print(lista_individual)
print(lista_completa)
