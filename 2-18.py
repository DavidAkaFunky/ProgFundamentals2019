numero = eval(input("Escreva um número inteiro: "))
seguido = 0
digito = 0
while numero > 0:
    digito = numero % 10
    if digito == 0:
        numero = numero // 10
        digito = numero % 10
        while digito == 0:
            seguido += 1
            digito = numero % 10
            numero = numero // 10
    numero = numero // 10
print ("O número tem", seguido, "zeros seguidos.")