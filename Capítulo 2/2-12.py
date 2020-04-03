x = eval(input("Qual o valor de x? "))
n = eval(input("Qual o valor de n? "))
ordem = 1
soma = 1
termo = 1
while ordem <= n:
   soma = soma + termo * (x/ordem)
   termo = termo * (x/ordem)
   ordem = ordem + 1
print ("A soma é", soma)