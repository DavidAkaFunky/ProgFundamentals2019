digito = eval(input("Escreva um dígito\n(-1 para terminar)\n? "))
if digito != -1:
    n = digito
    digito = eval(input("Escreva um dígito\n(-1 para terminar)\n? "))
    while digito != -1:
        n = n * 10 + digito
        digito = eval(input("Escreva um dígito\n(-1 para terminar)\n? "))
    else:
        print("O número é:", n)
else:
    import sys
    sys.exit(0)