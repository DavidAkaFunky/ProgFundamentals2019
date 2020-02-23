num = eval(input("Escreva um inteiro positivo: "))
x = num % 10
if num > 0:
    inv = x
    num = num // 10
    x = num % 10
    while num != 0:
        inv = 10 * inv + x
        num = num // 10
        x = num % 10
    print("O número invertido é:", inv)
else:
    print("O número não é positivo!")