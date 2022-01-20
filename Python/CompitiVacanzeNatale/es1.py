"""1. Scrivere un programma che data una lista qualsiasi ne elimini i duplicati."""

lista = []
elimina_doppi = lambda doppi,cella: cella in doppi

def main():
    nVolte = int(input("Inserici il numero di elementi da inserire nella lista: "))
    for i in range (nVolte):
          dato = int(input(f"Inserisci il valore della cella {i}: "))
          lista.append(dato)
    doppi = []
    listaStampa = []
    for elemento in lista:
        if elimina_doppi(doppi,elemento) == False:
            listaStampa.append(elemento)
        doppi.append(elemento)
    print(listaStampa)

if __name__ == "__main__":
    main()
