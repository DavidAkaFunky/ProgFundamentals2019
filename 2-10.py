numero = eval(input("Escreva um número inteiro positivo:\n? "))
if numero < 0:
    print ("Esse número não é positivo!")
else:
    num_impar = 0
    n = 0
    while numero != 0:
        digito = numero % 10
        if digito % 2 == 1:
            num_impar = num_impar + digito * (10 ** n)
            n += 1
        numero = numero // 10
    print ("O número composto pelos seus dígitos ímpares é:", num_impar)