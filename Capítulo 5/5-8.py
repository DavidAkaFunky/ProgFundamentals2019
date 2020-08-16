def seq_ramacan (k):
    if not (isinstance(k, int) and k >= 0):
        raise ValueError ("Nao esta definido")
    else:
        termo = 0
        lista = [0,]
        for n in range (1, k):
            if  lista[n-1] > n and lista[n-1] - n not in lista:
                lista = lista + [lista[n-1] - n]
            else:
                lista = lista + [lista[n-1] + n]
        return lista

k = eval(input("Introduza um numero natural: "))
print (seq_ramacan(k))