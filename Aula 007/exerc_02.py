##SOMAR PAR

#OPÇÃO1
# somapar = 0
# n = 0
# for i in range(2,200):
#     if n == 50:
#         print(n)
#         break
#     if i % 2 == 0:
#         print(i)
#         n +=1
#         somapar += i
# print(somapar)

#OPÇÃO 2
somapar = 0
par = 2
for i in range(50):
    print(par)
    somapar += par
    par += 2
print(somapar)
