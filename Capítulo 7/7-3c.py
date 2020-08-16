def numero_digitos (n):
    if not (isinstance(n, int) and n >= 1):
        raise ValueError ("Nao definido")
    else:
        res = 0
        while n != 0:
            res += 1
            n //= 10
        return res

print(numero_digitos(101473722))