data = input("Entre com a sua idade: ")
print(data)
datacompleta = data[6:10]+data[3:5]+data[0:2]
print(datacompleta)
data = data.split("/")
for i in range(len(data)-1,-1,-1):
    print(data[i],end="")
