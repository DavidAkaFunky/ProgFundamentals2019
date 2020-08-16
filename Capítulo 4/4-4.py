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

tuplo = eval(input("Escreva um tuplo: "))
print (filtra_pares (tuplo))