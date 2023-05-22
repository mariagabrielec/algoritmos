def totalanimal(cabeca,pes):
    coelhos =((pes - 2*cabeca)/2)
    patos = cabeca - coelhos
    return  patos,coelhos

print(totalanimal(23,70))
