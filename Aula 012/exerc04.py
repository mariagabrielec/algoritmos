def converte(x,y=0,z=0):
    hora_seg = x * 60 * 60
    min_seg = y * 60
    total = hora_seg + min_seg + z
    return total
hora = input("Digite a hora: ").split(":")
print(converte(int(hora[0]),int(hora[1]),int(hora[2])))
