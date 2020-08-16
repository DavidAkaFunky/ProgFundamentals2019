def quadrado (n):
    if not (isinstance(n, int) and n >= 1):
        raise ValueError ("Nao definido")
    elif n == 1:
        return 1
    else:
        return n + n - 1 + quadrado (n-1)

print (quadrado(6))