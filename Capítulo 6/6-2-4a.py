def filtra(lst,tst):
    if lst == []:
        return lst
    elif tst(lst[0]):
        return [lst[0]] + filtra(lst[1:], tst)
    else:
        return filtra(lst[1:], tst)

print(filtra([1, 2, 3, 4, 5], lambda x: x % 2 == 0))