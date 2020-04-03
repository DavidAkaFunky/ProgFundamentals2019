def metabolismo (dic):
    res = {}
    for nome in dic:
        s = dic[nome][0]
        p = dic[nome][1]
        h = dic[nome][2]
        i = dic[nome][3]
        if s == "M":
            res[nome] = 66 + 6.3 * p + 12.9 * h + 6.8 * i
        elif s == "F":
            res[nome] = 655 + 4.3 * p + 4.7 * h + 4.7 * i
    return res

print(metabolismo({"Maria" : ("F", 34, 1.65, 64), "Pedro": ("M", 34, 1.65, 64),"Ana": ("F", 54, 1.65, 120), "Hugo": ("M", 12, 1.82, 75)}))