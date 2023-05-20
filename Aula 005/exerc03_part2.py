precoliquido = float(input("Informe o preço líquido: "))
codigo = int(input("Informe o código de origem:"))
if codigo == 1:
    precofinal = precoliquido * 1.11
    print(f"A origem desse produto é do SUL. O preço final será {precofinal}")
elif codigo == 2:
    precofinal = precoliquido * 1.13
    print(f"A origem desse produto é do Norte. O preço final será {precofinal}")
elif codigo == 3:
    precofinal = precoliquido * 1.09
    print(f"A origem desse produto é do Nordeste. O preço final será {precofinal}")
elif codigo == 4:
    precofinal = precoliquido * 1.12
    print(f"A origem desse produto é do Centro-Oeste. O preço final será {precofinal}")
elif codigo == 5:
    precofinal = precoliquido * 1.18
    print(f"A origem desse produto é do Sudeste. O preço final será {precofinal}")