import random

lista = []

def main():
    nVolte = int(input("Inserici il numero di elementi da inserire nella lista: "))
    for i in range (nVolte):
          dato = input(f"Inserisci il valore della cella {i}: ")
          lista.append(dato)
    nuova = []
    doppi = []
    while len(nuova) != len(lista):
        indice = random.randint(0,len(lista)-1)
        if indice not in lista:
            nuova.append(lista[indice])
        doppi.append(indice)
    print(nuova)

if __name__ == "__main__":
    main()
