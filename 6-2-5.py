def soma_quadrados_impares (lst):
    def filtra(lst, tst):
        if lst == []:
            return lst
        elif tst(lst[0]):
            return [lst[0]] + filtra(lst[1:], tst)
        else:
            return filtra(lst[1:], tst)
    def transforma(lst, fn):
        if lst == []:
            return lst
        else:
            return [fn(lst[0])] + transforma(lst[1:], fn)
    def acumula(lst, fn):
        if len(lst) == 1:
            return lst[0]
        else:
            return fn(lst[0], acumula(lst[1:], fn))
    return acumula(transforma((filtra(lst, lambda x: x % 2 != 0)), lambda x: x**2), lambda x, y: x + y)

print(soma_quadrados_impares([1, 2, 3, 4, 5, 6]))