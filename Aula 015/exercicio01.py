arquivo = open("usuarios.txt", encoding="utf-8")
texto = arquivo.read()
lista = (texto.split("\n"))
dicionario = {}
lista_atualizada = []
totalmb = 0
for valor in lista:
    nome_codigo = valor.split(",")
    vlr_kb_to_mb = int(nome_codigo[1]) / (1024*1024)
    totalmb += vlr_kb_to_mb

for grupo in lista:
    nome_codigo = grupo.split(",")
    vlr_mb = round(int(nome_codigo[1]) / (1024*1024),2)
    vlr_percentual_int = round((vlr_mb / totalmb)*100,2)
    vlr_percentual_str = str(vlr_percentual_int)+"%"
    lista_atualizada.append(nome_codigo[0])
    lista_atualizada.append(str(vlr_mb)+" MB")
    lista_atualizada.append(vlr_percentual_str)



with open("relatorio.txt", "a", encoding="utf-8") as relatorio:
    relatorio.write("ACME Inc.         Uso do espaço em disco pelos usuários")
    relatorio.write("\n")
    relatorio.write("---------------------------------------------------------")
    relatorio.write("\n")
    relatorio.write("Nr.  Usuário      Espaço Utilizado     % do uso")
    relatorio.write("\n")
    soma = 1
    while len(lista_atualizada) > 0:
        itens = lista_atualizada[0:3]
        relatorio.write(str(soma)+"   ")
        for i in itens:
            relatorio.write(str(i)+" ")
        del lista_atualizada[0:3]
        relatorio.write("\n")
        soma += 1



print(lista_atualizada)