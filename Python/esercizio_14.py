#Es. 14

x1 = float(input("x1: "))
x2 = float(input("x2: "))
y1 = float(input("y1: "))
y2 = float(input("y2: "))

punto1 = (x1, y1)
punto2 = (x2, y2)

diffx = punto2[0] - punto1[0]
diffy = punto2[1] - punto1[1]

distanza = ((diffx**2) + (diffy**2)) ** 0.5

print(distanza)

