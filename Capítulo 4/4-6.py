def explode (n):
    if not isinstance(n, int):
        raise ValueError ("Explode: elemento nao inteiro")
    tuplo = ()
    while n > 0:
        digito = n % 10
        tuplo = (digito,) + tuplo
        n = n // 10
    return tuplo

def num_para_seq_cod (n):
    if not isinstance(n, int):
        raise ValueError ("Numero nao inteiro")
    num_novo = 0
    i = 0
    while n > 0:
        digito = n % 10
        if digito % 2 == 0:
            if digito == 8:
                digito = 0
            else:
                digito += 2
        else:
            if digito == 1:
                digito = 9
            else:
                digito -= 2
        num_novo += digito * (10 ** i)
        n = n // 10
        i += 1
    return explode (num_novo)

n = eval(input("Insira um numero: "))
print (num_para_seq_cod (n))