numero = eval(input("Introduza um número: "))
n = 1
while n <= 9:
    produto = numero * 8 + n
    print (numero, "x 8 +", n, "=", produto)
    n += 1
    numero = numero * 10 + n