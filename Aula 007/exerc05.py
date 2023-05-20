
minutos = 10
segundos = 0


while minutos >= 0:
    print(f"{minutos:02}:{segundos:02}") 


    if segundos > 0:
        segundos -= 1
    else:
        minutos -= 1
        segundos = 59


print("Contagem regressiva concluída!")


