frase = input("Digite uma frase: ").lower()
countVogais = 0
vogais = ""
for i in frase:
    if i in "aeiouáéíóúãõâêô":
        if i in vogais:
            continue
        else:
            countVogais += 1
            vogais += i
print(countVogais)
