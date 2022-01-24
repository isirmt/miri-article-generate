from pickle import TRUE
from telnetlib import NOP


import os

fArticle = open("./article/20220125.txt")
bArticle = open("./base/base-article.html")
text = fArticle.read()
fArticle.close()

areas = text.splitlines()

first = areas[2]

for i in range(2, len(areas)):
    areas[i] = "<p>"+areas[i]+"</p>"

bText = bArticle.read()
bTextAfter = bText.replace("***TITLE***", areas[0]).replace("***DATE***",
                                               areas[1]).replace("***FIRST***", first)

s = ""
for i in range(2, len(areas)):
    s += areas[i] + "\n"

postText = bTextAfter.replace("***MAIN***", s)

os.makedirs(areas[1], exist_ok=True)

newFilePath = "./"+areas[1]+"/index.html"

with open(newFilePath, "w") as f:
    f.write(postText)

bArticle.close()