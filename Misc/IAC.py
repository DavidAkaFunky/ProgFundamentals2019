def diferenca (x, y):
    if not y > x:
        raise ValueError ("y tem de ser maior que x")
    else:
        i = x
        res = 0
        while i < y:
            i += 1
            res += 1
        return res

x = eval(input("x = "))
y = eval(input("y = "))
print ("y - x =",diferenca(x,y))