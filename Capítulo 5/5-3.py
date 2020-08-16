def soma_cumultativa (lista):
    if not isinstance(lista, list):
        raise ValueError ("Nao definido")
    else:
        soma = 0
        lista_nova = []
        for i in lista:
            soma += i
            lista_nova = lista_nova + [soma]
        return lista_nova

x = eval(input("Introduza uma lista: "))
print (soma_cumultativa(x))