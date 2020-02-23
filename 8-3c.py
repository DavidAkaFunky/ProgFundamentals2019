def baralha(lista):
    if not isinstance(lista, list):
        raise ValueError ("O argumento tem de ser uma lista")
    else:
        from random import random
        a = int(51 * random())
        b = int(51 * random())
        lista[a], lista[b] = lista[b], lista[a]
        return lista

def baralho():
    naipes = ("esp", "cop", "our", "pau")
    valores = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    baralho = []
    for np in naipes:
        for val in valores:
            carta = {}
            carta["np"] = np
            carta["val"] = val
            baralho += [carta]
    return baralho

def distribui(x):
    if len(x) % 4 != 0 or not isinstance(x, list):
        raise ValueError ("Nao definido")
    else:
        return[x[:len(x)//4], x[len(x)//4:2 * len(x)//4], x[2 * len(x)//4:3 * len(x)//4], x[3 * len(x)//4:]]

print(distribui(baralha(baralho())))