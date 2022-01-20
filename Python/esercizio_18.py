#ES. 18

n1 = int (input("Inserisci un numero: "))
n2 = int (input("Inserisci un numero: "))

lista = []

lista.append((n1 ** n1) + (n2 ** n2))
lista.append((n1 + n2) ** (n1 + n2))
lista.append((n1 ** n1) - (n2 ** n2))
lista.append((n1 - n2) ** (n1 - n2))

print(lista)