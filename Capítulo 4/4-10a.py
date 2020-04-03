def codifica (str):
    pares = ""
    impares = ""
    str_nova = ""
    for i in range(len(str)):
        if i % 2 == 1:
            pares = pares + str[i]
        else:
            impares = impares + str[i]
        str_nova = impares + pares
    return str_nova

str = str(input("Insira uma cadeia de caracteres: "))
print (codifica(str))