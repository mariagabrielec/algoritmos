listaPrimos = []
countdivisores = 0
for i in range(100,200):
    for div in range(1,i+1):
        if i % div == 0:
            countdivisores += 1
        if countdivisores == 2:
            listaPrimos.append(i)
            countdivisores = 0
        else:
            countdivisores = 0
    else:
        break

print(listaPrimos)