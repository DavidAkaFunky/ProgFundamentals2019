from math import sqrt
x1 = eval(input("Vou pedir-lhe 5 números e calcularei a média deles e o seu desvio padrão.\nPrimeiro: "))
x2 = eval(input("Segundo: "))
x3 = eval(input("Terceiro: "))
x4 = eval(input("Quarto: "))
x5 = eval(input("Quinto e último: "))
media = (x1 + x2 + x3 + x4 + x5) / 5
desvio = sqrt(((x1 - media)*(x1 - media) + (x2 - media)*(x2 - media) + (x3 - media)*(x3 - media) + (x4 - media)*(x4 - media) + (x5 - media)*(x5 - media)) / 4)
print ("A média é ", media, "e o desvio-padrão é", desvio, ".")