import turtle

snow = turtle.Turtle()

window = turtle.Screen()

f = open("./istruzioni.txt", "w")

window.bgcolor("blue")
snow.color("white")

for _ in range(10):
    snow.down
    snow.forward(100)    #Ramo lungo
    f.write("forward:" + "100" + "\n")
    snow.left(10)
    f.write("left:" + "10" + "\n")
    snow.forward(40)    #Ramo corto
    f.write("forward:" + "40" + "\n")
    snow.up
    snow.backward(40)   #torna indietro
    f.write("backward:" + "40" + "\n")

    snow.right(20)      #Ramo corto
    f.write("right:" + "20" + "\n")
    snow.down
    snow.forward(40)
    f.write("forward:" + "40" + "\n")
    snow.up
    snow.backward(40)
    f.write("backward:" + "40" + "\n")

    snow.right(20)      #Ramo corto
    f.write("right:" + "20" + "\n")
    snow.down
    snow.forward(40)
    f.write("forward:" + "40" + "\n")
    snow.up
    snow.backward(40)
    f.write("backward:" + "40" + "\n")

    snow.left(10)
    f.write("left: " + "10" + "\n")
    snow.backward(100)
    f.write("backward:" + "100" + "\n")
    snow.right(20)
    f.write("right:" + "20" + "\n")

print(snow)

f.close
window.exitonclick()