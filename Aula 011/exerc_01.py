tuplageral = ()
for i in range(10):
    x = int(input("Informe um elemento: "))
    tuplageral = tuplageral + tuple([x])

print(tuplageral[::-1])
