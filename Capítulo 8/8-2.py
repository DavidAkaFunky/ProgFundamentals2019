def agrupa_por_chave(lista):
    if not isinstance(lista, list):
        raise ValueError ("O argumento tem de ser uma lista")
    else:
        res = {}
        for par in lista:
            if not isinstance(par, tuple):
                raise ValueError("Um dos elementos da lista nao e um tuplo")
            elif par[0] not in res:
                res[par[0]] = [par[1]]
            else:
                res[par[0]] += [par[1]]
        return res

print (agrupa_por_chave([("a", 8), ("b", 9), ("a", 3)]))