quantia = eval(input("Quanto dinheiro possui (em €)? "))
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
moeda2eur = 0
moeda1eur = 0
moeda50 = 0
moeda20 = 0
moeda10 = 0
moeda5 = 0
moeda2 = 0
moeda1 = 0
if quantia < 0:
    print ("Deve introduzir uma quantia positiva!")
else:
    while quantia >= 50:
        nota50 = quantia // 50
        quantia = quantia % 50
    while quantia >= 20:
        nota20 = quantia // 20
        quantia = quantia % 20
    while quantia >= 10:
        nota10 = quantia // 10
        quantia = quantia % 10
    while quantia >= 5:
        nota5 = quantia // 5
        quantia = quantia % 5
    while quantia >= 2:
        moeda2eur = quantia // 2
        quantia = quantia % 2
    while quantia >= 1:
        moeda1eur = quantia // 1
        quantia = quantia % 1
    while quantia >= 0.5:
        moeda50 = quantia // 0.5
        quantia = quantia % 0.5
    while quantia >= 0.2:
        moeda20 = quantia // 0.2
        quantia = quantia % 0.2
    while quantia >= 0.1:
        moeda10 = quantia // 0.1
        quantia = quantia % 0.1
    while quantia >= 0.05:
        moeda5 = quantia // 0.05
        quantia = quantia % 0.05
    while quantia >= 0.02:
        moeda2 = quantia // 0.02
        quantia = quantia % 0.02
    moeda1 = quantia / 0.01
    print ("Essa quantia corresponde a", int(nota50), "notas de 50€,",int(nota20), "notas de 20€,",int(nota10), "notas de 10€,",int(nota5), "notas de 5€,",int(moeda2eur), "moedas de 2€,",int(moeda1eur), "moedas de 1€,",int(moeda50), "moedas de 0,50€,",int(moeda20), "moedas de 0,20€,",int(moeda10), "moedas de 0,10€,",int(moeda5), "moedas de 0,05€,",int(moeda2), "moedas de 0,02€ e", round(moeda1), "moedas de 0,01€.")