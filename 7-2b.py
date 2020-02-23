def quadrado (n):
    if not (isinstance(n, int) and n >= 1):
        raise ValueError ("Nao definido")
    else:
        def aux (n, res):
            if n == 1:
                return res
            else:
                return aux (n-1, res + n + n - 1)
    return aux (n, 1)

print (quadrado(6))