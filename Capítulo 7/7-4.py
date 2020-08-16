def eh_capicua (n):
    if not (isinstance(n, int) and n >= 1):
        raise ValueError("Nao definido")
    def numero_digitos(n):
        if n // 10 == 0:
            return 1
        else:
            return 1 + numero_digitos(n // 10)
    dig = numero_digitos(n)
    num = str(n)
    def verifica (num, pos):
        if num == "" or pos == 0:
            return True
        elif num[0] != num[pos-1]:
            return False
        else:
            return verifica(num[1, pos-1])
    return verifica(num, dig)

print(eh_capicua(12321))