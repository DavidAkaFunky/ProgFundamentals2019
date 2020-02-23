#David Emanuel Silva Belchior, LEIC-A, Numero 95550
def eh_labirinto (maze): #Verifica se o labirinto esta bem definido
    if not isinstance(maze,tuple):
        return False
    else:
        def dimensao_labirinto (maze): #Verifica se o labirinto tem o formato correto
            valor_logico = True
            if len(maze) >= 3:
                for i in range(len(maze)-1):
                    if len(maze[i]) != len(maze[i+1]):
                        valor_logico = False
            else:
                valor_logico = False
            return valor_logico
        def paredes_verticais (maze): #Verifica se as paredes verticais estao bem definidas
            valor_logico2 = True
            for el in maze[0] and maze[len(maze)-1]:
                if el != 1:
                    return False
            return valor_logico2
        def paredes_horizontais (maze): #Verifica se as paredes horizontais estao bem definidas
            valor_logico3 = True
            for coluna in maze:
                if coluna[0] != 1 or coluna[len(coluna)-1] != 1:
                    valor_logico3 = False
            return valor_logico3
        return dimensao_labirinto (maze) and paredes_verticais (maze) and paredes_horizontais (maze)

def eh_posicao (unidade):
    valor_logico4 = True
    if len(unidade) != 2:
        valor_logico4 = False
    else:
        for el in unidade:
            if not isinstance(el,int) or el < 0:
                valor_logico4 = False
    return valor_logico4

def eh_conj_posicoes (conjunto):
    valor_logico5 = True
    for el in range(len(conjunto)):
        if not eh_posicao(conjunto[el]):
            valor_logico5 = False
        else:
            for el in range(len(conjunto)-1):
                if conjunto[el] == conjunto[el+1]:
                    valor_logico5 = False
    return valor_logico5

def tamanho_labirinto (maze):
    if not eh_labirinto(maze):
        raise ValueError ("tamanho_labirinto: argumento invalido")
    else:
        return (len(maze), len(maze[0]))

def eh_mapa_valido (maze, conj_posicoes):
    if not (eh_labirinto(maze) and eh_conj_posicoes(conj_posicoes)):
        raise ValueError ("eh_mapa_valido: algum dos argumentos e invalido")
    else:
        valor_logico6 = True
        for posicao in conj_posicoes:
            x = posicao[0]
            y = posicao[1]
            if not (x in range(len(maze)) and y in range(len(maze[0]))) or maze[x][y] == 1:
                valor_logico6 = False
        return valor_logico6

def eh_posicao_livre (maze, conj_posicoes, posicao):
    if not (eh_mapa_valido(maze, conj_posicoes) and eh_posicao (posicao)):
        raise ValueError ("eh_posicao_livre: algum dos argumentos e invalido")
    else:
        valor_logico7 = True
        x = posicao[0]
        y = posicao[1]
        if posicao in conj_posicoes or maze[x][y] == 1:
            valor_logico7 = False
    return valor_logico7

def posicoes_adjacentes (posicao):
    if not eh_posicao(posicao):
        raise ValueError("posicoes_adjacentes: algum dos argumentos e invalido")
    else:
        conj_posicoes_adj = ()
        for y in range(posicao[1]-1, posicao[1]+2):
            if y == posicao[1]:
                for x in (posicao[0]-1, posicao[0]+1):
                    if x >= 0:
                        conj_posicoes_adj += ((x,y),)
            else:
                x = posicao[0]
                if y >= 0:
                    conj_posicoes_adj += ((x,y),)
        return conj_posicoes_adj

def mapa_str (maze, conj_posicoes):
    if not eh_mapa_valido(maze, conj_posicoes):
        raise ValueError ("mapa_str: algum dos argumentos e invalido")
    else:
        mapa = ""
        for linha in range(len(maze[0])):
            for coluna in range (len(maze)):
                if maze[coluna][linha] == 1:
                    mapa += "#"
                else:
                    mapa += "."
                    for posicao in conj_posicoes:
                        x = posicao[0]
                        y = posicao[1]
                        if coluna == x and linha == y:
                            mapa = mapa[0:len(mapa)-1] + "0"
            mapa += "\n"
        return mapa

def obter_objetivos (maze, unidades, posicao):
    if not eh_mapa_valido(maze,unidades) or posicao not in unidades:
        raise ValueError ("obter_objetivos: algum dos argumentos e invalido")
    else:
        objetivo = ()
        for un in unidades:
            if un != posicao:
                for pos_adj in posicoes_adjacentes(un):
                    if pos_adj != posicao and pos_adj not in objetivo and maze[pos_adj[0]][pos_adj[1]] != 1:
                        objetivo += (pos_adj,)
        return objetivo

def obter_caminho (maze, unidades, posicao):
    if not eh_mapa_valido(maze,unidades) or posicao not in unidades:
        raise ValueError ("obter_caminho: algum dos argumentos e invalido")
    else:
        lista_exploracao = (posicao,)
        objetivos = obter_objetivos (maze, unidades, posicao)
        posicoes_visitadas = lista_exploracao
        while lista_exploracao != ():
            posicao_atual = lista_exploracao[0]
            caminho_atual = posicoes_visitadas
            if posicao_atual not in posicoes_visitadas:
                posicoes_visitadas += (posicao_atual,)
                caminho_atual += (posicao_atual,)
                if posicao_atual in objetivos:
                    return caminho_atual
                else:
                    for posicao_adj in posicoes_adjacentes(posicao):
                        if eh_posicao_livre(maze, unidades, posicao_adj):
                            lista_exploracao += (posicao_adj,)
            lista_exploracao = lista_exploracao[1:]
        return caminho_atual


def mover_unidade (maze, conj_posicoes, posicao):
    if not eh_mapa_valido(maze,conj_posicoes) or posicao not in conj_posicoes:
        raise ValueError ("mover_unidade: algum dos argumentos e invalido")
    else:
        for unidade in conj_posicoes:
            if unidade in posicoes_adjacentes(posicao):
                return conj_posicoes
            else:
                pos_nova = obter_caminho(maze, conj_posicoes, posicao)[1]
                for i in range(len(conj_posicoes)):
                    if conj_posicoes[i] == posicao:
                        conj_posicoes = conj_posicoes[:i] + pos_nova + conj_posicoes[i+1:]