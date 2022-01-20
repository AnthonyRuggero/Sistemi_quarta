f = open("./prova.txt","r")

righe = f.readlines()

print(righe)

f.close()

f = open("./provaScrittura.txt","w")

f.write("Sono ")
f.write("molto ")
f.write("bello ")

f.close()