def euromilhoes():
    def bubble_sort (lista):
        i = len (lista)
        while i > 1:
            for k in range(i-1):
                if lista [k] > lista [k + 1]:
                    lista [k], lista [k + 1] = lista [k + 1], lista [k]
            i -= 1
    from random import randrange
    numeros = []
    estrelas = []
    n = 0
    m = 0
    while n < 5:
        numero = randrange(1,51)
        if numero not in numeros:
            numeros = numeros + [numero]
            n += 1
    while m < 2:
        numero = randrange(1,13)
        if numero not in estrelas:
            estrelas = estrelas + [numero]
            m += 1
    bubble_sort(numeros)
    bubble_sort(estrelas)
    print ([numeros, estrelas])

input("Prima ENTER para sortear uma chave do Euromilhoes")
euromilhoes()