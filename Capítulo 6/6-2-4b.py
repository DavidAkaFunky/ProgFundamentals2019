def transforma (lst, fn):
    if lst == []:
        return lst
    else:
        return [fn(lst[0])] + transforma (lst[1:], fn)