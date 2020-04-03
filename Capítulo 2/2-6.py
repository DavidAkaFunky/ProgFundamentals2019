print("Vou pedir-lhe 3 números e dir-lhe-ei o maior deles.")
x1 = eval(input("O primeiro: "))
x2 = eval(input("O segundo: "))
x3 = eval(input("O terceiro e último: "))
if x1 < x2 and x2 <= x3:
    numero = x3
elif x1 < x2 and x2 > x3:
    numero = x2
elif x1 >= x2 and x1 > x3:
    numero = x1
else:
    numero = x3
print ("O maior dos 3 números é o", numero)