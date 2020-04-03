def explode (n):
    if not isinstance(n, int):
        raise ValueError ("Explode: elemento nao inteiro")
    tuplo = ()
    while n > 0:
        digito = n % 10
        tuplo = (digito,) + tuplo
        n = n // 10
    return tuplo


x = eval(input("Indique um numero: "))
print(explode (x))