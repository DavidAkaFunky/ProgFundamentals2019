def reconhece (idt):
    letra = ("A", "B", "C", "D")
    num = ("1","2","3","4")
    valor_verdade = True
    if idt[0] in letra:
        i = 0
        if idt[len(idt) - 1] not in num:
            valor_verdade = False
        else:
            while i < len(idt) - 2:
                if idt[i] in num and idt [i+1] not in num:
                    valor_verdade = False
                i += 1
    return valor_verdade


str = input ("Insira uma cadeia de caracteres: ")
print (reconhece(str))