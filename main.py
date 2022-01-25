import os

fileName = 20220125

name = "./article/" + str(fileName) + ".txt"
fArticle = open(name)
bArticle = open("./base/base-article.html")
text = fArticle.read()
fArticle.close()

markdown = {
    "codeBlock": False
}

areas = text.splitlines()

first = areas[2]
date = areas[1][0:4] + "-" + areas[1][4:6] + "-" + areas[1][6:8]

for i in range(2, len(areas)):
    if areas[i] == "```":
        if not markdown["codeBlock"]:
            areas[i] = "<div class=\"markdown\">"
        else:
            areas[i] = "</div>"
        markdown["codeBlock"] = not markdown["codeBlock"]
    else:
        if markdown["codeBlock"]:
            areas[i] = areas[i].replace(" ", "&nbsp;")
        areas[i] = areas[i].replace("<", "&lt;").replace(">", "&gt;")
        areas[i] = "<p>"+areas[i]+"</p>"

bText = bArticle.read()
bTextAfter = bText.replace("***TITLE***", areas[0]).replace(
    "***DATE***", date).replace("***FIRST***", first).replace("***PAGE***", areas[1])

s = ""
for i in range(2, len(areas)):
    s += areas[i] + "\n"

postText = bTextAfter.replace("***MAIN***", s)

os.makedirs(areas[1], exist_ok=True)

newFilePath = "./"+areas[1]+"/index.html"

with open(newFilePath, "w") as f:
    f.write(postText)

bArticle.close()
