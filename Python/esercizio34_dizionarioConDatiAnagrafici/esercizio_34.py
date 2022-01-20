# chiedi i dati anagrafici e salvali su file

nome = input("Inserisci il tuo nome: ")
cognome = input("Inserisci il tuo cognome: ")
dataDiNascita = input("Inserisci la tua data di nascita: (gg/mm/aaaa) ")

dati = {"nome": nome, "cognome": cognome, "dataDiNascita" : dataDiNascita}

f = open("./dati.txt", "w")

for chiave in dati:
    f.write(dati[chiave] + "\n")

f.close()