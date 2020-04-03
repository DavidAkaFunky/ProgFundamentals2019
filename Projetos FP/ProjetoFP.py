#David Emanuel Silva Belchior, LEIC-A, Numero 95550
def eh_labirinto (maze):
    """Esta funcao indica se o argumento dado eh um labirinto \
nas condicoes descritas no enunciado do projeto"""
    if not isinstance(maze,tuple):
        return False
    else:
        for coluna in range(len(maze)): 
            if maze[coluna] == () or type(maze[coluna]) != tuple: #Verifica se o labirinto eh um tuplo de tuplos
                return False            
            for el in maze[coluna]: #Verifica se cada coluna contem apenas 0 ou 1
                if type(el) != int or not (el == 0 or el == 1):
                    return False        
        def dimensao_labirinto (maze): #Verifica se o labirinto tem o formato correto
            valor_logico = True
            if len(maze) >= 3:
                for i in range(len(maze)-1):
                    if len(maze[i]) < 3 or len(maze[i]) != len(maze[i+1]):
                        valor_logico = False
            else:
                valor_logico = False
            return valor_logico
        def paredes_verticais (maze): #Verifica se as paredes verticais estao bem definidas
            valor_logico2 = True
            for el in maze[0]:
                if el != 1:
                    return False
            for el in maze[len(maze)-1]:
                if el != 1:
                    return False        
            return valor_logico2
        def paredes_horizontais (maze): #Verifica se as paredes horizontais estao bem definidas
            valor_logico3 = True
            for coluna in maze:
                if coluna[0] != 1 or coluna[len(coluna)-1] != 1:
                    valor_logico3 = False
            return valor_logico3
        return dimensao_labirinto (maze) and paredes_verticais (maze) and paredes_horizontais (maze) #Conjuncao logica 

def eh_posicao (unidade):
    """Esta funcao indica se o argumento dado eh uma posicao \
nas condicoes descritas no enunciado do projeto"""    
    valor_logico4 = True
    if type(unidade) != tuple: #Verifica se a unidade e um tuplo
        valor_logico4 = False
    elif len(unidade) != 2: #Verifica se o tuplo contem apenas 2 elementos
        valor_logico4 = False
    else:
        for el in unidade:
            if type(el) != int or el < 0: #Verifica se os elementos sao numeros naturais
                valor_logico4 = False
    return valor_logico4

def eh_conj_posicoes (conjunto):
    """Esta funcao indica se o argumento dado eh um conjunto de posicoes unicas \
nas condicoes descritas no enunciado do projeto"""    
    valor_logico5 = True
    if type(conjunto) != tuple: #Verifica se o conjunto eh um tuplo
        valor_logico5 = False
    else:
        posicoes_distintas = ()
        for posicao in conjunto:
            if not eh_posicao(posicao) or posicao in posicoes_distintas: #Verifica se cada elemento eh uma posicao
                valor_logico5 = False
            else: #Verifica se cada posicao eh unica
                posicoes_distintas += (posicao,)
    return valor_logico5

def tamanho_labirinto (maze):
    """Esta funcao indica as dimensoes de um argumento avaliado positivamente como \
labirinto (numero de colunas, numero de linhas)"""    
    if not eh_labirinto(maze):
        raise ValueError ("tamanho_labirinto: argumento invalido")
    else:
        return (len(maze), len(maze[0]))

def eh_mapa_valido (maze, conj_posicoes):
    """Esta funcao indica se os argumentos dados (um labirinto e um \
conjunto de posicoes unicas) formam um mapa valido \
nas condicoes descritas no enunciado do projeto"""     
    if not (eh_labirinto(maze) and eh_conj_posicoes(conj_posicoes)): #Verifica a validade dos argumentos
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
    """Esta funcao indica se uma posicao (o terceiro argumento dado, validado \
como tal) se encontra livre ao ser indicado um labirinto e um conjunto de \
posicoes (os dois primeiros argumentos, validados como tal)"""
    if not (eh_posicao (posicao) and eh_labirinto(maze) and eh_conj_posicoes(conj_posicoes) and eh_mapa_valido(maze, conj_posicoes)):
        raise ValueError ("eh_posicao_livre: algum dos argumentos e invalido")
    else:
        valor_logico7 = True
        x = posicao[0]
        y = posicao[1]
        if posicao in conj_posicoes or maze[x][y] == 1:
            valor_logico7 = False
    return valor_logico7

def posicoes_adjacentes (posicao):
    """Esta funcao indica as posicoes adjacentes a uma posicao, validada como tal"""    
    if not eh_posicao(posicao):
        raise ValueError("posicoes_adjacentes: argumento invalido")
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
    """Esta funcao permite representar visualmente um labirinto e um conjunto de \
posicoes, validadas como tal. Para isso, deve ser acompanhada da funcao print"""
    if type(conj_posicoes) != tuple or type(maze) != tuple or not eh_mapa_valido(maze, conj_posicoes) or not (eh_labirinto(maze) and eh_conj_posicoes(conj_posicoes)):
        raise ValueError ("mapa_str: algum dos argumentos e invalido")
    else:
        mapa = ""
        for linha in range(len(maze[0])): #O mapa eh criado de linha em linha
            for coluna in range (len(maze)):
                if maze[coluna][linha] == 1:
                    mapa += "#"
                else:
                    mapa += "."
                    for posicao in conj_posicoes:
                        x = posicao[0]
                        y = posicao[1]
                        if coluna == x and linha == y:
                            mapa = mapa[0:len(mapa)-1] + "O"
            mapa += "\n"
        return mapa[:len(mapa)-1] #Permite remover o ultimo "/n" adicionado em excesso
    
def obter_objetivos (maze, unidades, posicao):
    """Esta funcao indica, com base num labirinto, num conjunto de unidades \
que pretendemos alcancar, e numa unidade de partida (validadas como tal), o \
conjunto de posicoes adjacentes as unidades que pretendemos alcancar. \
Serve de base para a funcao obter_caminho"""    
    if not (posicao in unidades and eh_labirinto(maze) and eh_conj_posicoes(unidades)) or not eh_mapa_valido(maze,unidades): #Validacao dos argumentos
        raise ValueError ("obter_objetivos: algum dos argumentos e invalido")
    else:
        objetivo = ()
        for un in unidades:
            if un != posicao:
                for pos_adj in posicoes_adjacentes(un):
                    if pos_adj != posicao and pos_adj not in objetivo and pos_adj not in unidades and maze[pos_adj[0]][pos_adj[1]] != 1:
                        objetivo += (pos_adj,)
        #Sao acrescentadas as posicoes adjacentes das unidades diferentes das posicao, sendo ignoradas posicoes adjacentes repetidas
        return objetivo

def obter_caminho (maze, unidades, posicao):
    """Esta funcao indica, com base num labirinto, num conjunto de unidades \
que pretendemos alcancar, e numa unidade de partida (validadas como tal), o \
caminho mais curto ate uma das posicoes adjacentes as unidades que pretendemos \
alcancar, tendo por base o algoritmo BFS (Breadth-First Search)"""    
    if not (posicao in unidades and eh_labirinto(maze) and eh_conj_posicoes(unidades) and eh_posicao(posicao) and eh_mapa_valido(maze, unidades)):#Validacao dos argumentos
        raise ValueError ("obter_caminho: algum dos argumentos e invalido")
    else: #Inicializacao de estruturas        
        caminho = ()
        if unidades == (posicao,):
            return caminho
        for pos in unidades:
            if posicao in posicoes_adjacentes(pos):
                return caminho
        #Situacoes em que nao e feito qualquer deslocamento
        lista_exploracao = [[posicao, caminho]]
        objetivos = obter_objetivos (maze, unidades, posicao)
        while lista_exploracao != []:
            posicao_atual = lista_exploracao[0][0]
            caminho_atual = lista_exploracao[0][1]
            for pos_adj in posicoes_adjacentes(posicao_atual):
                if pos_adj not in caminho and eh_posicao_livre (maze, unidades, pos_adj):
                    caminho = caminho_atual + (posicao_atual,)
                    lista_exploracao += [[pos_adj, caminho]]
                    if pos_adj in objetivos:
                        return caminho + (pos_adj,)
            del lista_exploracao[0]        
        return caminho

def mover_unidade (maze, conj_posicoes, posicao):
    """Esta funcao permite, com base num labirinto, num conjunto de unidades \
que pretendemos alcancar, e numa unidade de partida (validadas como tal), mover \
essa unidade de partida segundo o caminho mais curto ate uma das posicoes \
adjacentes as unidades que pretendemos obtido na funcao obter_caminho"""
    if not (posicao in conj_posicoes and eh_labirinto(maze) and eh_conj_posicoes(conj_posicoes)):
        raise ValueError ("mover_unidade: algum dos argumentos e invalido")
    else:
        for unidade in conj_posicoes:
            if unidade not in posicoes_adjacentes(posicao) and conj_posicoes != (posicao,):
                caminho = obter_caminho(maze, conj_posicoes, posicao)
                if caminho == ():
                    return conj_posicoes
                pos_nova = caminho[1]
                for i in range(len(conj_posicoes)):
                    if conj_posicoes[i] == posicao and eh_posicao_livre(maze, conj_posicoes, pos_nova):
                        conj_posicoes = conj_posicoes[:i] + (pos_nova,) + conj_posicoes[i+1:]
                        return conj_posicoes
            else:
                return conj_posicoes