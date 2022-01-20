lista = []

def main():
    nVolte = int(input("Inserici il numero di elementi da inserire nella lista: "))
    for i in range (nVolte):
          dato = input(f"Inserisci il valore della cella {i}: ")
          lista.append(dato)
    dizionario = {}
    chiave = 0
    for elemento in lista:
        dizionario[chiave] = elemento
        chiave+=1
    print(dizionario)
if __name__ == "__main__":
    main()
      
