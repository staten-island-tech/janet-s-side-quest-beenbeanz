#F TO C
list = ["Label", 32, 50, 77, 104]
newList = []
actualList = []

for i in list[1:]:
    newList.append(i)

temperaturesInF = map(lambda x: (x - 32) * (5/9), newList)
for i in temperaturesInF:
    actualList.append(i)
print((actualList))

