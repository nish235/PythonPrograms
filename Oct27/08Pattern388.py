for x in range(1, 5):
    for y in range(4, x, -1):
        print(" ", end=" ")
    for z in range(x - 1, -x, -1):
        print(chr(x - abs(z) + 64), end=" ")
    print()
