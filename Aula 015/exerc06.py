with open("timefutebol.txt","w") as arquivo:
    while True:
        time = input("Digite um texto: ")
        if time == 'sair':
            break
        else:
            arquivo.write(time)
            arquivo.write("\n")