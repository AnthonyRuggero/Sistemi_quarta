tavolo = []

def creaTavolo ():
    for i in range (6):
        riga = [] 
        for j in range (7):
            riga.append(" ")
        tavolo.append(riga)

def stampaTavolo ():
    for i in range (6):
        print(tavolo[i])

def inputPlayer (player):
    col = int(input("Inserisci la colonna in cui inserire la pedina: "))
    if col <= 6 and col >= 0 :
        i = 5
        while (i >= 0 and tavolo[i][col] != " "):
            i -= 1
        tavolo[i][col] = player #inserisce la pedina del giocatore

def win (player):
    for riga in tavolo:
        for col in range (4):
            if riga[col] == player and riga[col + 1] == player and riga[col + 2] == player and riga[col + 3] == player:
                return True
    
    for col in range (7):
        for riga in range(3):
            if tavolo[riga][col] == player and tavolo[riga + 1][col] == player and tavolo[riga + 2][col] == player and tavolo[riga + 3][col] == player:
                return True
    for riga in range(3):
        for col in range(4):
            if tavolo[riga][col] == player and tavolo[riga + 1][col + 1] == player and tavolo[riga + 2][col + 2] == player and tavolo[riga + 3][col + 3] == player:
                return True
    for riga in range (3):
        for col in range(3,7):
            if tavolo[riga][col] == player and tavolo[riga + 1][col - 1] == player and tavolo[riga + 2][col - 2] == player and tavolo[riga + 3][col - 3] == player:
                return True

def main ():
    creaTavolo()
    stampaTavolo()
    while True:
        print("E' IL TURNO DEL GIOCATORE 1 ")
        inputPlayer("X")
        stampaTavolo()
        if win("X"):
            print("Il Giocatore 1 ha vinto")
            break
        print("E' IL TURNO DEL GIOCATORE 2 ")
        inputPlayer("O")
        stampaTavolo()
        if win("O"):
            print("Il Giocatore 2 ha vinto")
            break

if __name__ == "__main__": 
    main()

