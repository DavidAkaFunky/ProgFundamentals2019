horas = eval(input("Quantas horas trabalhou? "))
if horas < 0:
    print ("Não existem horas negativas!")
else:
    sal_hora = eval(input("Quanto ganha por hora (em €)? "))
    if horas < 0:
        print ("Não pode ganhar quantias negativas por hora!")
    if horas > 40:
        extra = horas - 40
        salario = 40 * sal_hora + 2 * extra * sal_hora
    else:
        salario = horas * sal_hora
    print("Vai receber", salario, "€ esta semana.")