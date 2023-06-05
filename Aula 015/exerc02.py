#SUBSTITUIR INFORMAÇÃO DE UM ARQUIVO JÁ EXISTENTE OU NÃO
texto = input("Digite o texto: ")
arquivo = open("texto.txt","w",encoding="utf-8")
arquivo.write(texto)
print("gravando")
arquivo.close()