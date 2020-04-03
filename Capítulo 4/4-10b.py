def descodifica (str):
    str_nova = ""
    i = 0
    if len(str) % 2 == 0:
        pares = str[len(str) // 2:]
        impares = str[:len(str) // 2]
        while i <= len(impares) // 2:
            str_nova = str_nova + impares[i] + pares[i]
            i += 1
    else:
        pares = str[len(str) // 2 + 1:]
        impares = str[:len(str) // 2 + 1]
        while i <= len(pares) // 2:
            str_nova = str_nova + impares[i] + pares[i]
            i += 1
        str_nova = str_nova + impares[len(impares) - 1]
    return str_nova

str = input("Insira uma cadeia de caracteres: ")
print (descodifica(str))