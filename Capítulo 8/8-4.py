def resumo_FP(dicionario):
    if not isinstance(dicionario, dict):
        raise ValueError ("Nao definido")
    else:
        soma_pos_notas = 0
        soma_pos_alunos = 0
        for nota in dicionario:
            if not (isinstance(nota, int) and isinstance(dicionario[nota], list) and 0 <= nota <= 20):
                raise ValueError ("Nao definido")
            elif nota >= 10:
                soma_pos_notas += nota * len(dicionario[nota])
                soma_pos_alunos += len(dicionario[nota])
        return (soma_pos_notas/soma_pos_alunos, soma_pos_alunos)

print(resumo_FP({1 : [46592, 49212, 90300, 59312], 15 : [52592, 59212], 20 : [58323]}))