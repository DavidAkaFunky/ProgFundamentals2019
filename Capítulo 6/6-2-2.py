def piatorio (l_inf, l_sup, op, prox):
    produto = 1
    while l_inf <= l_sup:
        produto *= op(l_inf)
        l_inf = prox(l_inf)
    return produto

#Para invocar a funcao fatorial (do numero n) com a funcao piatorio:
n = eval(input("Introduza um numero para calcular o seu fatorial: "))
print(piatorio(1, n, lambda x: x, lambda x: x+1))