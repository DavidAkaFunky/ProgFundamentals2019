def acumula (lst, fn):
    if len(lst) == 1:
        return lst[0]
    else:
        return fn(lst[0], acumula(lst[1:], fn))

print(acumula([1, 2, 3, 4], lambda x, y : x + y))