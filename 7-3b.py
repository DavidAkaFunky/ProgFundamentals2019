def numero_digitos (n):
    if not (isinstance(n, int) and n >= 1):
        raise ValueError ("Nao definido")
    else:
        def aux (p, res):
            if p // 10 == 0:
                return res
            else:
                return aux(p // 10, res + 1)
        return aux (n, 1)

print(numero_digitos(101473722))