def misterio (x, n):
    def aux (p, res):
        if p == 0:
            return res
        else:
            return aux (p-1, res + x * p)
    return aux (n, 0)

print (misterio(4, 3))