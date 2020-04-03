from math import sin, pi
for ang in range (91):
    seno = "seno_" + str(ang)
    y = round(256 * (sin ((ang * pi)/180)))
    if ang < 10:
        print (seno, "         WORD   ", y)
    else:
        print (seno, "        WORD   ", y)