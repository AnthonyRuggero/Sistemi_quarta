import turtle

snow = turtle.Turtle()

window = turtle.Screen()

f = open("./istruzioni.txt", "r")

righe = f.readlines()

for riga in righe:
    ls = riga.split(":")
    comando = ls[0]                #prendo il primo elemento della lista ovvero il comando
    valore = int(ls[1][:-1])       #prendo il secondo elemento della lista, senza l'ultimo carattere (senza \n)
    if(comando == "forward"):
        snow.forward(valore)
    elif(comando == "backward"):
        snow.backward(valore)
    elif(comando == "right"):
        snow.right(valore)
    elif(comando == "left"):
        snow.left(valore)

f.close()

window.exitonclick()