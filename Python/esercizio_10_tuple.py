#tuple

tupla = (3, 6, -1, 10) #tupla di 4 elementi
print(tupla)
print(tupla[0])

lista = [3, 3.3, "ciao"] #lista eterogenea, perché composta da tipi diversi
print(lista)
print(lista[-1])
lista[1] = 2.645

numeri_primi = [2, 3, 5, 7, 11, 13]

print(numeri_primi)
numeri_primi.append(17)
print(numeri_primi)

print(f"La lunghezza è: {len(numeri_primi)}")

altri_numeri_primi = [19, 23, 29]

molti_numeri_primi = numeri_primi + altri_numeri_primi  

print(molti_numeri_primi)

for numero_primo in numeri_primi: #stampa solo ciò che è indentato, carattere terminatore
    print(numero_primo) 






