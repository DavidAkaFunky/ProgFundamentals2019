#E necessario corrigir
def conta_palavras (cc):
    conj_palavras = []
    palavra = ""
    res = {}
    for char in cc:
        if char == " ":
            conj_palavras += [palavra]
            palavra = ""
        else:
            palavra += cc
    for palavra in conj_palavras:
        if palavra not in res:
            res[palavra] = 1
        else:
            res[palavra] += 1
    return res

cc = "a aranha arranha a ra a ra arranha a aranha nem a aranha arranha a ra nem a ra arranha a aranha"
print(conta_palavras(cc))