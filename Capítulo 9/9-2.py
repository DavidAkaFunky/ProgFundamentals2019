def cria_rel (h,m,s):
    if not (isinstance(h, int) and h >= 0 and isinstance(m, int) and m >= 0 and isinstance(s, int) and s >= 0):
        return ValueError ("Os valores tem de ser todos inteiros")
    else:
        return [h,m,s]

def horas (relogio):
    return relogio[0]

def minutos (relogio):
    return relogio[1]

def segs (relogio):
    return relogio[2]

def eh_relogio (arg):
    if isinstance(arg,list) and isinstance(horas(arg), int) and horas(arg) >= 0 and isinstance(minutos(arg), int) and minutos(arg) >= 0 and isinstance(segs(arg), int) and segs(arg) >= 0:
        return True
    else:
        return False

def eh_meio_dia (relogio):
    if not eh_relogio(relogio):
        raise ValueError ("")
    elif horas(relogio) == 12 and minutos(relogio) == 0 and segs(relogio) == 0:
        return True
    else:
        return False

def eh_meia_noite (relogio):
    if not eh_relogio(relogio):
        raise ValueError ("")
    elif horas(relogio) == 0 and minutos(relogio) == 0 and segs(relogio) == 0:
        return True
    else:
        return False