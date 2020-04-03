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

print (baralho())