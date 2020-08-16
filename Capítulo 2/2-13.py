numero = eval(input("Escreva um número para efetuar a sua tabuada da multiplicação: "))
fator = 1
while fator <= 10:
    produto = numero * fator
    print (numero, "x", fator, "=", produto)
    fator += 1