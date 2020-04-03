def multiplica_matrizes (a, b):
    if not (isinstance(a, list) and isinstance(b, list)):
        raise ValueError("Nao introduziu duas matrizes")
    else:
        def avalia (m):
            for l in range(len(m) - 2):
                if len(m[l]) != len(m[l+1]) :
                    raise ValueError("Matriz invalida")
        def avalia_matrizes (m1, m2):
            if len (m1[0]) != len (m2):
                raise ValueError("O numero de colunas de a nao e igual ao numero de linhas de b, logo o produto nao e efetuavel")
        def escreve_matriz(matriz):
            for linha in matriz:
                print(*linha)
        avalia(a)
        avalia(b)
        avalia_matrizes(a, b)
        matriz = []
        for i in range(len(a)):
            linha_nova = []
            for j in range(len(a)):
                soma = 0
                for k in range(len(a[0])):
                    soma += a[i][k] * b[k][j]
                linha_nova = linha_nova + [soma]
            matriz = matriz + [linha_nova]
        return escreve_matriz(matriz)

m1 = eval(input("Insira uma matriz: "))
m2 = eval(input("Insira outra matriz: "))
multiplica_matrizes (m1, m2)