f = open("abc.txt", "r")
l1 = f.readlines()
last = l1[-6:]
print(last)
f.close()
