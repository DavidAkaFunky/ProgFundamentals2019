#Ciclo for
def soma_fn (n, fn):
    soma = 0
    for i in range (1,n+1):
        soma += fn(i)
    return soma

#Com recursao
def soma_fn2 (n, fn):
    if n == 1:
        return fn (1)
    else:
        return fn (n) + soma_fn2(n-1,fn)