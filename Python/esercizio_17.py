liste = ["Ciao", "Casa", "Lavagna", "Contemporaneamente"]

lungMax = ""
for lista in liste:
    if(len(lista) > len(lungMax)):
        lungMax = lista

print(f"La parola più lunga è: {lungMax}")