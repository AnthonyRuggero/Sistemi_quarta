nomeFile = input("Inserire il nome del file da leggere: ")
file = open(nomeFile, "r")
righe = file.readlines() ##salva in righe non il numero ma il contenuto di ogni riga

nRighe = len(righe) ##in nRighe viene salvato il numero di righe del file

file.close()

nCommenti = 0
nStampe = 0
for riga in righe:
    if "printf" in riga:
        nStampe += 1
    if "//" in riga or "/*" in riga:
        nCommenti += 1

print(f"Il file ha {nRighe} righe")       
print(f"Il file ha {nStampe} 'printf'")
print(f"Il file ha {nCommenti} linee di commento")

