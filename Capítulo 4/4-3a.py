def implode (tuplo):
    i = len(tuplo) - 1
    n = 0
    numero = 0
    while i >= 0:
        if not isinstance(tuplo [i], int):
            raise ValueError ("Implode: elemento nao inteiro")
        numero += tuplo[i] * (10 ** n)
        i -= 1
        n += 1
    return numero

tuplo = eval(input("Escreva um tuplo: "))
print (implode (tuplo))