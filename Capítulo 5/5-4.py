def elemento_matriz (matriz, linha, coluna):
    if not isinstance(matriz, list):
        raise ValueError ("Nao introduziu uma matriz")
    else:
        for l in range(len(matriz) - 2):
            if len(matriz[l]) != len(matriz[l+1]):
                raise ValueError("Matriz invalida")
        if coluna > len (matriz[0]) - 1:
            raise ValueError("elemento_matriz: indice invalido, coluna", coluna)
        if linha > len (matriz) - 1:
            raise ValueError("elemento_matriz: indice invalido, linha", linha)
        else:
            return matriz[linha][coluna]

m = eval(input("Insira uma matriz: "))
linha = eval(input("Insira uma linha da matriz: "))
coluna = eval(input("Insira uma coluna da matriz: "))
print (elemento_matriz (m, linha, coluna))