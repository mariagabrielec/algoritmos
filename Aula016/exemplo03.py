def retorna_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return print("Chave não Existe")
    except TypeError:
        return print("Não é um dicionário")

dicio = {"nome":"Maria"}

retorna_valor(dicio,"nome")