def soma_matrizes (m1, m2):
    if not (isinstance(m1, list) and isinstance(m2, list)):
        raise ValueError("Nao introduziu duas matrizes")
    else:
        def avalia (m):
            for l in range(len(m) - 2):
                if len(m[l]) != len(m[l+1]) :
                    raise ValueError("Matriz invalida")
        def avalia_matrizes (m1, m2):
            if len (m1) != len (m2):
                raise ValueError("As matrizes sao de tipos diferentes")
            else:
                for l in range(len(m1) - 1):
                    if len(m1[l]) != len(m2[l]) :
                        raise ValueError("As matrizes sao de tipos diferentes")
        def escreve_matriz(matriz):
            for linha in matriz:
                print(*linha)
        avalia(m1)
        avalia(m2)
        avalia_matrizes(m1, m2)
        matriz = []
        for l in range(len(m1)):
            linha_nova = []
            for c in range(len(m1[0])):
                linha_nova = linha_nova + [m1[l][c] + m2[l][c]]
            matriz = matriz + [linha_nova]
        return escreve_matriz(matriz)

m1 = eval(input("Insira uma matriz: "))
m2 = eval(input("Insira outra matriz: "))
soma_matrizes (m1, m2)