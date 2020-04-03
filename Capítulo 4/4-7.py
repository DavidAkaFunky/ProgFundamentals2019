def amigas (palavra1, palavra2):
    if len(palavra1) != len(palavra2):
        raise ValueError ("As palavras nao tem o mesmo comprimento!")
    diferenca = 0
    for i in range(len(palavra1) - 1):
        diferenca += abs(ord(palavra1[i]) - ord(palavra2[i]))
    return 
