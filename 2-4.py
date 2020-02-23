x = (eval(input("Escreva um número de segundos: ")))
if x >= 0:
    dias = x // 86400
    x = x % 86400
    horas = x // 3600
    x = x % 3600
    minutos = x // 60
    x = x % 60
    print ("Esse número de segundos equivale a", dias, "dias,", horas, "horas,", minutos, "minutos e", x, "segundos.")
else:
    print ("Não existem segundos negativos!")