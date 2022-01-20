import sys

mesi = {"Gennaio" : 0, "Febbraio": 0, "Marzo": 0, "Aprile": 0, "Maggio": 0, "Giugno": 0, "Luglio": 0, "Agosto": 0, "Settembre": 0, "Ottobre": 0, "Novembre": 0, "Dicembre":0 }

anni = {"2011": 0, "2012": 0, "2013": 0, "2014": 0, "2015": 0, "2016":0 }

file = open("./prezzi.csv", "r")

prezzo_spesa = []
listaMesi = []
prodotti = []
for i in range (5):
    prodotti.append(int(input(f"Inserire l'indice del {i + 1} prodotto: ")))

righe = file.readlines()

righe.pop(0)

for riga in righe:
    somma = 0
    campi = riga.split(";")
    listaMesi.append(campi[1] + campi[0])
    for prodotto in prodotti:
        somma += float(campi[prodotti[i]])
    prezzo_spesa.append(somma)

print(listaMesi)
print(prezzo_spesa)

prezzoMin = 10000
meseMin = ""
indiceMin = None    
prezzoMax = 0
meseMax= ""
indiceMax = None

for i, prezzo in enumerate(prezzo_spesa):
    if(prezzo < prezzoMin):
        prezzoMin = prezzo
        indiceMin = i

print(f"la spesa ha un prezzo minimo di {listaMesi[indiceMin]} nel mese di " )




for anno in anni.keys():
    if prezzoAnnoMin > anni[anno]:
        prezzoAnnoMin = anni[anno]
        annoMin = anno
    if prezzoAnnoMax < anni[anno]:
        prezzoAnnoMax = anni[anno]
        annoMax = anno

print(f"Il mese {meseMin} è stato il meno caro ({prezzoMin})")
print(f"Il mese {meseMax} è stato il più caro ({prezzoMax})")
print(f"L'anno {annoMin} è stato il meno caro ({prezzoAnnoMin})")
print(f"L'anno {annoMax} è stato il più caro ({prezzoAnnoMax})")
