def numero_digitos (n):
    if not (isinstance(n, int) and n >= 1):
        raise ValueError ("Nao definido")
    elif n // 10 == 0:
        return 1
    else:
        return 1 + numero_digitos (n // 10)

print(numero_digitos(101473722))