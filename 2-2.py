x = eval(input("Que distância percorreu (em km)? "))
if x < 0 :
    print ("Não existem distâncias negativas!")
else:
    y = eval(input("Quanto tempo demorou (em minutos)? "))
    if x >= 0 and y > 0:
        z = (60 * x) / y
        w = x / 1000 * 60 * y
        print("A sua velocidade foi de", z, "km/h ou", w, "m/s.")
    elif y < 0:
        print("Não existem tempos negativos!")
    else:
        print("Não se pode dividir por zero!")