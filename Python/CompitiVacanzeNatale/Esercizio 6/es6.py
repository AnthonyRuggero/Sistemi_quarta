contatore = {"A":0, "T": 0, "C": 0, "G": 0}
f = open("./covid-19_gen1.txt", "r")

righe = f.readlines()

f.close()
for riga in righe:
    for i in range (len(riga)):
        if riga[i] != "\n":
            contatore[riga[i]] += 1

print(contatore)
