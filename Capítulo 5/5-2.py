def remove_multiplos (lista, num):
    if not (isinstance(lista, list) and isinstance(num, int)):
        raise ValueError ("Nao definido")
    else:
        for i in range (len (lista) - 1, -1, -1):
            if lista[i] % num == 0:
                del lista [i]
        return lista

x = eval(input("Introduza uma lista apenas com inteiros: "))
y = eval(input("Introduza um inteiro: "))
print (remove_multiplos (x, y))