def espelho (n):
    if not (isinstance(n, int) and n >= 1):
        raise ValueError("Nao definido")
    def numero_digitos(n):
        if n // 10 == 0:
            return 1
        else:
            return 1 + numero_digitos(n // 10)
    dig = numero_digitos(n)
    num = str(n)
    for i in range(0, dig):
