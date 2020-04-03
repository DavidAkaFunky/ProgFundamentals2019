# David Emanuel Silva Belchior - LEIC-A - Numero 95550

####### TAD posicao #######

#Construtores
#Posicao: (Coordenada x, coordenada y)

def cria_posicao (x,y):
    """Esta funcao cria uma posicao com as condicoes descritas no enunciado do projeto"""
    if not (type(x) == int and x >= 0 and type(y) == int and y >= 0):
        raise ValueError ("cria_posicao: argumentos invalidos")
    else:
        return (x,y)

def cria_copia_posicao (pos):
    """Esta funcao cria uma copia da posicao dada como argumento"""
    return pos.copy()

#Seletores

def obter_pos_x (pos):
    """Esta funcao devolve a posicao em x da posicao dada como argumento"""
    return pos[0]

def obter_pos_y (pos):
    """Esta funcao devolve a posicao em y da posicao dada como argumento"""
    return pos[1]

#Reconhecedor

def eh_posicao (arg):
    """Esta funcao indica se o argumento da mesma eh uma posicao"""
    return type(arg) == tuple and type(obter_pos_x(arg)) == int and obter_pos_x(arg) > 0 and type(obter_pos_y (arg)) == int and obter_pos_y (arg) > 0

#Teste

def posicoes_iguais (p1,p2):
    """Esta funcao indica se duas posicoes sao iguais"""
    return eh_posicao(p1) and eh_posicao(p2) and p1 == p2

#Transformador

def posicao_para_str (p):
    """Esta funcao devolve uma string correspondente 'a posicao dada como argumento"""
    return str(p)

#Funcoes de alto nivel

def obter_posicoes_adjacentes (pos):
    """Esta funcao indica as posicoes adjacentes 'a posicao dada como argumento"""
    pos_x = obter_pos_x (pos)
    pos_y = obter_pos_y (pos)
    conj_posicoes_adj = ()
    for y in range(pos_y-1, pos_y+2):
        if y == pos_y:
            for x in (pos_x-1, pos_x+1):
                if x >= 0:
                    conj_posicoes_adj += ((x,y),)
        else:
            x = pos_x
            if y >= 0:
                conj_posicoes_adj += ((x,y),)
    return conj_posicoes_adj

####### TAD unidade #######

#Construtores
#Unidade: [Posicao, Vida, Forca de ataque, Exercito]
def cria_unidade (p, v, f, s):
    """Esta funcao cria uma unidade com as condicoes descritas no enunciado do projeto"""    
    if not (eh_posicao(p) and type(v) == int and v > 0 and type(f) == int and f > 0 and type(s) == str and s != ""):
        raise ValueError ("cria_unidade: argumentos invalidos")
    else:
        return [p, v, f, s]

def cria_copia_unidade (unidade):
    """Esta funcao cria uma copia da unidade dada como argumento"""    
    return unidade.copy()

#Seletores

def obter_posicao (unidade):
    """Esta funcao devolve a posicao da unidade dada como argumento"""    
    return unidade[0]

def obter_vida (unidade):
    """Esta funcao devolve a vida da unidade dada como argumento"""        
    return unidade[1]

def obter_forca (unidade):
    """Esta funcao devolve a forca de ataque da unidade dada como argumento"""        
    return unidade[2]

def obter_exercito (unidade):
    """Esta funcao devolve o nome do exercito da unidade dada como argumento"""           
    return unidade[3]

#Modificadores

def muda_posicao (un, pos):
    """Esta funcao altera destrutivamente a posicao da unidade dada como argumento para o argumento pos"""
    un[0] = pos
    return un

def remove_vida (un, vida):
    """Esta funcao altera destrutivamente a vida da unidade dada como argumento, subtraindo-lhe o valor do argumento vida"""
    un[1] -= vida
    return un


#Reconhecedor

def eh_unidade(arg):
    """Esta funcao indica se o argumento da mesma eh uma unidade"""    
    return type(arg) == list and eh_posicao(obter_posicao (arg)) and type(obter_vida (arg)) == int and obter_vida (arg) > 0 and type(obter_forca (arg)) == int and obter_forca (arg) > 0 and type(obter_exercito (arg)) == str and obter_exercito (arg) != ""

#Teste

def unidades_iguais (u1, u2):
    """Esta funcao indica se as duas unidades passadas como argumentos sao iguais"""    
    return eh_unidade(u1) and eh_unidade(u2) and u1 == u2

#Transformadores

def unidade_para_char (un):
    """Esta funcao devolve o primeiro caracter do exercito da unidade em letra maiuscula"""
    return (obter_exercito (un)[0]).upper()

def unidade_para_str (un):
    """Esta funcao devolve uma string que representa externamente a unidade, segundo a estrutura descrita no enunciado do projeto"""
    return str(unidade_para_char (un)) + str ([obter_vida (un), obter_forca (un)]) + "@" + str(obter_posicao(un))

#Funcoes de alto nivel

def unidade_ataca (u1, u2):
    """Esta funcao permite efetuar um ataque do primeiro argumento (u1) sobre o segundo (u2), retirando 'a vida de u2 o valor da forca de ataque de u1 e devolvendo um valor logico que indica se u2 morreu, ou seja, se a sua vida passou a ser menor ou igual que 0 depois do ataque"""
    remove_vida(u2, obter_forca(u1))
    return obter_vida(u2) <= 0

def ordenar_unidades (lista_un):
    """Esta funcao permite ordenar as unidades de uma lista segundo a sua posicao, de acordo com a ordem de leitura convencionada para os mapas"""
    def pos_x (un):
        return obter_pos_x(obter_posicao(un))    
    def pos_y (un):
        return obter_pos_y(obter_posicao(un))
    return sorted(sorted(lista_un, key = pos_x), key = pos_y)

####### TAD mapa #######

#Construtor
#Mapa: {"dim": Dimensao do mapa (x,y), "prd": Locais das paredes, "ex1": Unidades do exercito 1, "ex2": Unidades do exercito 2}
def cria_mapa (d, w, e1, e2):
    """Esta funcao cria um mapa com as condicoes descritas no enunciado do projeto"""
    if not(type(d) == tuple and len(d) == 2 and type(w) == tuple and type(e1) == tuple and len(e1) >= 1 and type(e2) == tuple and len(e2) >= 1):
        raise ValueError ("cria_mapa: argumentos invalidos")
    else:
        for pos in w:
            for e1_un in e1:
                for e2_un in e2:
                    if not (eh_posicao(pos) and eh_unidade(e1_un) and eh_unidade(e2_un)):
                        raise ValueError ("cria_mapa: argumentos invalidos")
        return {"dim": d, "prd": w, "ex1": e1, "ex2": e2}

def cria_copia_mapa (m):
    """Esta funcao cria uma copia do mapa dado como argumento"""
    ex1 = ()
    ex2 = ()
    for un in m["ex1"]:
        ex1 += (cria_copia_unidade(un),)
    for un in m["ex2"]:
        ex2 += (cria_copia_unidade(un),)
    m1 = {"dim": m["dim"], "prd": m["prd"], "ex1": ex1, "ex2": ex2}
    return m1

#Seletores

def obter_tamanho (m):
    """Esta funcao devolve o tamanho, em x e em y, do mapa dado como argumento"""
    return (m["dim"][0], m["dim"][1])

def obter_nome_exercitos (m):
    """Esta funcao devolve o nome de cada exercito do mapa dado como argumento"""    
    return (obter_exercito(m["ex1"][0]), obter_exercito(m["ex2"][0]))

def obter_unidades_exercito (m,e):
    """Esta funcao devolve, de forma ordenada, as unidades do exercito do mapa dado como argumento"""        
    if e in ("ex1", "ex2"):
        return ordenar_unidades(m[e])
    else:
        for chave in ("ex1","ex2"):
            if e == obter_exercito(m[chave][0]):
                return ordenar_unidades(m[chave])

def obter_todas_unidades (m):
    """Esta funcao devolve, de forma ordenada, todas as unidades do mapa dado como argumento""" 
    return ordenar_unidades(obter_unidades_exercito(m,"ex1") + obter_unidades_exercito(m,"ex2"))

def obter_unidade (m,p):
    """Esta funcao devolve, se existir, a unidade que se encontra na posicao p do mapa m"""
    for unidade in obter_todas_unidades(m):
        if obter_posicao(unidade) == p:
            return unidade

#Modificadores

def eliminar_unidade (m, u):
    """Esta funcao permite eliminar, se existir, a unidade u do mapa m"""
    for chave in m:
        for un in range(len(m[chave])-1):
            if u == m[chave][un]:
                if un == len(m[chave])-1:
                    m[chave] = m[chave][:un]
                else:
                    m[chave] = m[chave][:un] + m[chave][un+1:]
    return m

def mover_unidade (m, u, n):
    """Esta funcao permite mover, se existir, a unidade u do mapa m para a posicao n"""
    for chave in m:
        for un in range(len(m[chave])):
            if u == m[chave][un]:
                m[chave][un][0] = n
    return m

#Reconhecedores
def eh_posicao_unidade (m, p):
    """Esta funcao indica se a posicao p do mapa p se encontra ocupada por uma unidade"""        
    return p in (m["ex1"], m["ex2"])

def eh_posicao_corredor (m, p):
    """Esta funcao indica se a posicao p do mapa p nao se encontra ocupada, ou seja, se se trata de um corredor"""
    return p not in m["prd"] and obter_pos_x(p) not in (0, obter_tamanho(m)[0]) and obter_pos_y(p) not in (0, obter_tamanho(m)[1])

def eh_posicao_parede (m, p):
    """Esta funcao indica se a posicao p do mapa p se encontra ocupada por uma parede"""
    return not eh_posicao_corredor(m, p)

#Teste

def mapas_iguais (m1,m2):
    """Esta funcao indica se os mapas m1 e m2 sao iguais"""    
    return obter_tamanho(m1) == obter_tamanho(m2) and m1["prd"] == m2["prd"] and obter_todas_unidades (m1) == obter_todas_unidades(m2)

#Transformador

def mapa_para_str (m):
    """Esta funcao permite representar visualmente um labirinto e um conjunto de \
posicoes, validadas como tal. Para isso, deve ser acompanhada da funcao print"""
    mapa = ""
    pos_ex1 = []
    pos_ex2 = []
    nome_ex1 = unidade_para_char(m["ex1"][0])
    nome_ex2 = unidade_para_char(m["ex2"][0])
    for unidade in obter_unidades_exercito(m, "ex1"):
        pos_ex1 += [obter_posicao(unidade)]
    for unidade in obter_unidades_exercito(m, "ex2"):
        pos_ex2 += [obter_posicao(unidade)]    
    for linha in range(obter_pos_y(obter_tamanho(m))): #O mapa eh criado de linha em linha
        for coluna in range (obter_pos_x(obter_tamanho(m))):
            pos = (coluna, linha)
            if linha == 0 or linha == obter_pos_y(obter_tamanho(m))-1 or coluna == 0 or coluna == obter_pos_x(obter_tamanho(m))-1 or pos in m["prd"]:
                mapa += "#"
            elif pos in pos_ex1:
                mapa += nome_ex1
            elif pos in pos_ex2:
                mapa += nome_ex2           
            else:
                mapa += "."
        mapa += "\n"
    return mapa[:len(mapa)-1] #Permite remover o ultimo "/n" adicionado em excesso

#Funcoes de alto nivel

def obter_inimigos_adjacentes (m, u):
    """Esta funcao indica que unidades nas posicoes adjacentes 'a da posicao de u sao do exercito inimigo"""    
    pos_u = obter_posicao(u)
    res = []
    for chave in ("ex1","ex2"):
        for i in range(len(m[chave])):
            inim_possivel = m[chave][i]
            if obter_posicao(inim_possivel) in obter_posicoes_adjacentes (pos_u) and obter_exercito (inim_possivel) != obter_exercito (u):
                res += [inim_possivel]
    return res

def obter_movimento(mapa, unit):
    '''
    A funcao obter_movimento devolve a posicao seguinte da unidade argumento
    de acordo com as regras de movimento das unidades no labirinto.

    obter_movimento: mapa x unidade -> posicao
    '''

    ######################
    # Funcoes auxiliares #
    ######################
    def pos_to_tuple(pos):
        return obter_pos_x(pos), obter_pos_y(pos)

    def tuple_to_pos(tup):
        return cria_posicao(tup[0], tup[1])

    def tira_repetidos(tup_posicoes):
        conj_tuplos = set(tuple(map(pos_to_tuple, tup_posicoes)))
        return tuple(map(tuple_to_pos, conj_tuplos))

    def obter_objetivos(source):
        enemy_side = tuple(filter(lambda u: u != obter_exercito(source), obter_nome_exercitos(mapa)))[0]
        target_units = obter_unidades_exercito(mapa, enemy_side)
        tup_com_repetidos = \
            tuple(adj
                  for other_unit in target_units
                  for adj in obter_posicoes_adjacentes(obter_posicao(other_unit))
                  if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj))
        return tira_repetidos(tup_com_repetidos)

    def backtrack(target):
        result = ()
        while target is not None:
            result = (target,) + result
            target, _ = visited[target]
        return result

    ####################
    # Funcao principal #
    ####################
    # Nao mexer se ja esta' adjacente a inimigo
    if obter_inimigos_adjacentes(mapa, unit):
        return obter_posicao(unit)

    visited = {}
    # posicao a explorar, posicao anterior e distancia
    to_explore = [(pos_to_tuple(obter_posicao(unit)), None, 0)]
    # registro do numero de passos minimo ate primeira posicao objetivo
    min_dist = None
    # estrutura que guarda todas as posicoes objetivo a igual minima distancia
    min_dist_targets = []

    targets = tuple(pos_to_tuple(obj) for obj in obter_objetivos(unit))

    while to_explore:  # enquanto nao esteja vazio
        pos, previous, dist = to_explore.pop(0)

        if pos not in visited:  # posicao foi ja explorada?
            visited[pos] = (previous, dist)  # registro no conjunto de exploracao
            if pos in targets:  # se a posicao atual eh uma dos objetivos
                # se eh primeiro objetivo  ou se esta a  distancia minima
                if min_dist is None or dist == min_dist:
                    # acrescentor 'a lista de posicoes minimas
                    min_dist = dist
                    min_dist_targets.append(pos)
            else:  # nao 'e objetivo, acrescento adjacentes
                for adj in obter_posicoes_adjacentes(tuple_to_pos(pos)):
                    if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj):
                        to_explore.append((pos_to_tuple(adj), pos, dist + 1))

        # Parar se estou a visitar posicoes mais distantes que o minimo,
        # ou se ja encontrei todos os objetivos
        if (min_dist is not None and dist > min_dist) or len(min_dist_targets) == len(targets):
            break

    # se encontrei pelo menos uma posicao objetivo,
    # escolhe a de ordem de leitura menor e devolve o primeiro movimento
    if len(min_dist_targets) > 0:
        # primeiro dos objetivos em ordem de leitura
        tar = sorted(min_dist_targets, key=lambda x: (x[1], x[0]))[0]
        path = backtrack(tar)
        return tuple_to_pos(path[1])

    # Caso nenhuma posicao seja alcancavel
    return obter_posicao(unit)

####### Funcoes adicionais #######

def calcula_pontos (mapa, ex):
    """Esta funcao devolve a soma dos pontos de vida de cada unidade do exercito ex do mapa dado como argumento, acompanhados do nome do respetivo exercito"""
    total = 0
    for unidade in obter_unidades_exercito(mapa, ex):
        total += obter_vida(unidade)
    if total < 0:
        total = 0
    return total

def simula_turno (m):
    """Esta funcao permite simular um turno de uma batalha. Para cada unidade, eh realizado um movimento. Se existir uma ou mais unidades inimigas nas posicoes adjacentes da unidade, a primeira detetada, segundo a ordem de leitura, eh atacada. Se esse ataque provocar a morte da unidade, ela eh removida do mapa"""
    m1 = cria_copia_mapa(m)
    for unidade in obter_todas_unidades(m1):
        mover_unidade(m1, unidade, obter_movimento(m,unidade))
        for poss_inim in obter_inimigos_adjacentes(m1, unidade):
            if obter_posicao(poss_inim) in obter_posicoes_adjacentes(obter_posicao(unidade)):
                if unidade_ataca(unidade, poss_inim):
                    eliminar_unidade(m1,poss_inim)
                break
    return m1

def simula_batalha (config, bool):
    """Esta funcao recebe, como argumentos, o ficheiro de configuracao que contem os elementos necessarios para a realizacao da batalha, segundo a ordem indicada no enunciado do projeto, e um valor logico. Se esse valor logico for True, o mapa inicial e todos os turnos da batalha sao apresentados no ecran. Caso contrario, apenas o mapa inicial e o final sao apresentados. Em ambos os casos, o mapa apresentado eh acompanhado dos pontos de cada exercito, tal como obtido pela funcao calcula_pontos.
    
    Na batalha, sao efetuados turnos ate que um dos exercitos morra (sendo apresentado o nome do exercito vencedor), ambos os exercitos morram (resultando num empate), ou nenhum dos exercitos possa ser atacado, devido ao isolamento dado pelas paredes (resultando, igualmente, num empate)."""
    with open(config) as f:
        args = f.readlines()
    dim = eval(args[0])
    ex1_nome = eval(args[1])[0]
    ex1_vida = eval(args[1])[1]
    ex1_forca = eval(args[1])[2]
    ex2_nome = eval(args[2])[0]
    ex2_vida = eval(args[2])[1]
    ex2_forca = eval(args[2])[2]
    paredes = eval(args[3])
    ex1_un = eval(args[4])
    ex2_un = eval(args[5])
    ex1 = ()
    ex2 = ()
    for pos in ex1_un:
        ex1 += (cria_unidade(pos, ex1_vida, ex1_forca, ex1_nome),)
    for pos in ex2_un:
        ex2 += (cria_unidade(pos, ex2_vida, ex2_forca, ex2_nome),)
    mapa = cria_mapa(dim, paredes, ex1, ex2)
    def turno (mapa, ex1_nome, ex2_nome):
        print(mapa_para_str(mapa))
        print("[", str(ex1_nome) + ":"+str(calcula_pontos(mapa,ex1_nome)), str(ex2_nome) + ":"+str(calcula_pontos(mapa,ex2_nome)), "]")
    turno (mapa,ex1_nome,ex2_nome)
    mapa_ant = cria_copia_mapa(mapa)
    while calcula_pontos(mapa,ex1_nome) > 0 and calcula_pontos(mapa,ex2_nome) > 0 and not mapas_iguais(mapa_ant, simula_turno(mapa)):
        if bool:
            turno(mapa, ex1_nome, ex2_nome)
        mapa_ant = cria_copia_mapa(mapa)
    if calcula_pontos(mapa,ex1_nome) <= 0 and calcula_pontos(mapa,ex2_nome) > 0:
        print(ex2_nome)
    elif calcula_pontos(mapa,ex1_nome) > 0 and calcula_pontos(mapa,ex2_nome) <= 0:
        print(ex1_nome)
    elif calcula_pontos(mapa,ex1_nome) == 0 and calcula_pontos(mapa,ex2_nome) == 0:
        print ("EMPATE")
    else:
        turno(mapa, ex1_nome, ex2_nome)
        print ("EMPATE")    