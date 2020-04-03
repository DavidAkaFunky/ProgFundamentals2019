def quadrado (n):
    if not (isinstance(n, int) and n >= 1):
        raise ValueError ("Nao definido")
    else:
        res = 0
        for i in range (1, n+1):
            res += i + i - 1
        return res

print (quadrado(6))