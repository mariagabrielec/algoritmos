nome = input("Informe seu primeiro nome: ")
sobrenome = input("Informe seu sobrenome: ")
ultimoNome = input("Informe seu último nome: ")
print(f'{nome} {sobrenome} {ultimoNome}')
nomecompleto = " ".join([nome,sobrenome,ultimoNome])
print(nomecompleto)
nomecript = ""
#criptografia
for i in nomecompleto:
    letraatual = ord(i)
    nextletra = chr(letraatual+1)
    nomecript += nextletra
print(nomecript)
