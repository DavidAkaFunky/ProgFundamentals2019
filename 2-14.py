numero = eval(input("Escreva um número inteiro para calcular a soma dos seus dígitos: "))
soma = 0
while numero !=0:
    digito = numero % 10
    soma += digito
    numero = numero // 10
print ("A soma dos seus dígitos é", soma)