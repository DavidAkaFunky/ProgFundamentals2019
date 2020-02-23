#Realizado por David Belchior e Hugo Ribeiro, LEIC-A, Numeros 95550 e 95590
def movimento (ang, v0, x0, tempo, disc):
    if not ((isinstance(ang, int) or isinstance(ang, float)) and 0 <= ang <= 90 and (isinstance(v0, int) or isinstance(v0, float)) and (isinstance(x0, int) or isinstance(x0, float)) and (isinstance(tempo, int)) and tempo > 0 and (isinstance(disc, int) or isinstance(disc, float)) and disc > 0):
        raise ValueError ("Nao definido")
    def a (ang):
        from math import sin, pi
        return 9.81 * sin ((ang * pi)/180)
    t = 0
    def x (x0, v0, a, t):
        x = (a / 2) * (t ** 2) + v0 * t + x0
        return x
    def v (v0, a, t):
        v = v0 + a * t
        return v
    import time
    a = a (ang)
    while t <= tempo:
        print("A posicao atual e", round(x(x0, v0, a, t), 4), "m.")
        print ("A velocidade atual e", round(v (v0, a, t), 4), "m/s.")
        t += disc
        time.sleep(disc)  # Intervalo de discretizacao
    print ("Terminado!")

ang = eval(input("Insira o angulo do plano inclinado (em graus): "))
v0 = eval(input("Insira a velocidade inicial (em m/s): "))
x0 = eval(input("Insira a posicao inicial (em m): "))
tempo = eval(input("Insira o tempo de observacao do movimento (em s): "))
disc = eval(input("Insira o periodo de atualizacao dos valores da velocidade e da posicao (em s): "))
movimento(ang, v0, x0, tempo, disc)