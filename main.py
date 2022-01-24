f = open("./article/20220125.txt")
text = f.read()
print(text)

areas = text.splitlines()
print(areas)
f.close()

