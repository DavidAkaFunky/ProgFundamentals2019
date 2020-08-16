def lista_codigos (string):
    if not isinstance(string, str):
        raise ValueError ("Nao foi introduzida uma string")
    else:
        lista = []
        for c in string:
            lista = lista + [ord(c)]
        return lista

x = input("Introduza uma string: ")
print (lista_codigos(x))