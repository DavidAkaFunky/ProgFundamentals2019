digito = eval(input("Escreva um dígito para fazer um número\n(-1 para terminar): "))
if digito < 0:
    print ("O dígito tem de ser positivo!")
elif digito != -1:
    numero = digito
    digito = eval(input("Diga-me um dígito para fazer um número\n(-1 para terminar): "))
    while digito != -1:
        numero = numero * 10 + digito
        digito = eval(input("Diga-me um dígito para fazer um número\n(-1 para terminar): "))
    print ("O número é", numero)
else:
    print ("Não me deu nenhum dígito...")