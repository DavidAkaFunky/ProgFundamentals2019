x = eval(input("Escreva um número de segundos\n(Um número negativo para terminar): "))
while x >= 0:
    y = x / (60 * 60 * 24)
    print("O número de dias correspondente é", y)
    x = eval(input("Escreva um número de segundos\n(Um número negativo para terminar): "))
else:
    import sys
    sys.exit(0)