d = 3
for x in range(d, -(d + 1), -1):
    for y in range(abs(x), 0, -1):
        print(" ", end="")
    for z in range(abs(x), 4):
        print(abs(z), end="")
    print()

