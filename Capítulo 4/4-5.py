def explode (n):
    if not isinstance(n, int):
        raise ValueError ("Explode: elemento nao inteiro")
    tuplo = ()
    while n > 0:
        digito = n % 10
        tuplo = (digito,) + tuplo
        n = n // 10
    return tuplo

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

def filtra_pares (t):
    i = len(t) - 1
    tuplo = ()
    while i >= 0:
        if not isinstance(t[i], int):
            raise ValueError("Implode: elemento nao inteiro")
        if t[i] % 2 == 0:
            tuplo = (t[i],) + tuplo
        i -= 1
    return tuplo

def algarismos_pares (n):
    return (implode(filtra_pares(explode(n))))

numero = eval(input("Escreva um numero: "))
print (algarismos_pares (numero))