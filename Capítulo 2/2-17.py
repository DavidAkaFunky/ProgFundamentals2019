nota = eval(input("Quais foram as notas dos alunos?\n(Um número negativo para terminar): "))
positiva = 0
total = 0
if nota < 0 or nota > 20:
    print ("Não foram introduzidas notas válidas!")
elif 0 <= nota <= 20:
    total += 1
    if nota >= 9.5:
        positiva += 1
    elif nota > 20:
        print("Não é uma nota válida!")
    nota = eval(input("Quais foram as notas dos alunos?\n(Um número negativo para terminar): "))
    while 0 <= nota <= 20:
        total +=1
        if nota >= 9.5:
            positiva += 1
        nota = eval(input("Quais foram as notas dos alunos?\n(Um número negativo para terminar): "))
    if positiva == 1:
        print("Houve", positiva, "positiva num total de", total, "alunos, o que corresponde a",
              (positiva * 100) / total, "% de alunos com nota positiva.")
    elif positiva != 1:
        print("Houve", positiva, "positivas num total de", total, "alunos, o que corresponde a",
              (positiva * 100) / total, "% de alunos com nota positiva.")