numero_orig = eval(input("Escreva um número:\n-> "))
numero = numero_orig
if numero > 0:
    digito = numero % 10
    numero = numero // 10
    inv = digito
    while numero != 0:
        digito = numero % 10
        inv = inv * 10 + digito
        numero = numero // 10
        numero_orig = numero_orig * 10
    numero_orig += inv
print ("A respetiva capicua é",numero_orig)