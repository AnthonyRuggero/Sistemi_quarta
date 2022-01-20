
scelta = int(input("Che operazione vuoi fare: (0 somma, 1 sottrazione, 2 moltiplicazione, 3 divisione)"))
n1 = int(input("Inserisci un numero: "))
n2 = int(input("Inserisci un numero: "))

if(scelta == 0):
    somma = n1 + n2
    print(f"somma: {somma}")
elif(scelta == 1):
    differenza = n1 - n2
    print(f"differenza: {differenza}")
elif(scelta == 2):
    prodotto = n1 * n2
    print(f"prodotto: {prodotto}")
elif(scelta == 3):
    quoziente = n1 / n2
    print(f"quoziente: {quoziente}")
else:
    print("Inserisci un altro numero")