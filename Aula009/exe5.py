from random import randint
count1, count2, count3, count4, count5, count6 = 0,0,0,0,0,0
for i in range(0,6000):
    lado = randint(1,7)
    if lado == 1:
        count1+=1
    if lado == 2:
        count2 += 1
    if lado == 3:
        count3 += 1
    if lado == 4:
        count4+= 1
    if lado == 5:
        count5 += 1
    if lado == 6:
        count6 += 1

lista = [count1, count2, count3, count4, count5, count6]
print(f'Os números 1,2,3,4,5,6 repetiram respectivamente {lista}')