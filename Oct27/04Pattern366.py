i = 1
for x in range(5, 0, -1):
    for y in range(x, 0, -1):
        print(" ", end=" ")
    for z in range(i, 0, -1):
        print(chr(z+64), end=" ")
    i += 2
    print()
