import random

f = open("./lanci.txt", "w")

alice = [random.randint(1,6) for n in range(10)]
bob = [random.randint(1,6) for n in range(10)]

f.write("A  B\n")

for n in range(10):
    f.write(f"{alice[n]}, {bob[n]}\n")

f.close()