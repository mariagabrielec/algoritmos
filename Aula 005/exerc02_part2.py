idade = int(input("Digite a idade: "))
if idade > 4 and idade < 8:
    print(f"Categoria Infantil")
elif idade > 7 and idade < 11:
    print(f"Categoria Juvenil")
elif idade > 10 and idade < 16:
    print(f"Categoria Adolescente")
elif idade > 15 and idade < 31:
    print(f"Categoria Adulto")
else:
    print("Categoria Sênior")