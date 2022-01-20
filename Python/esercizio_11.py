#ES. 11

x = [0, 1, 2, 3, 5, 6, 7, 8]

y = x[ : len(x//2)]
z = x[len(x//2) : ]

y.append(5)

print(x)
print(y)
print(z)