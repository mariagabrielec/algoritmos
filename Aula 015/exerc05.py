#ITERANDO EM UM ARQUIVO
arquivo = open("frutas.txt", encoding="utf-8")
texto = arquivo.read()
lista = texto.split("\n")
arquivo = open("frutas.txt","a",encoding="utf-8")
while True:
    fruta = input("dDigite uma fruta: ")
    if fruta == "":
        break
    elif fruta in lista:
        print("Fruta repetida!!")
    else:
        arquivo.write(f"{fruta}\n")

arquivo.close()
