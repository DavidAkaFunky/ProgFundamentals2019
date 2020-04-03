def escreve_matriz (matriz):
    if not isinstance(matriz, list):
        raise ValueError ("Nao introduziu uma matriz")
    else:
        for l in range(len(matriz) - 2):
            if len(matriz[l]) != len(matriz[l+1]):
                raise ValueError("Matriz invalida")
        for linha in matriz:
            print (*linha)

m = eval(input("Insira uma matriz: "))
escreve_matriz(m)

escreve_matriz(matriz)