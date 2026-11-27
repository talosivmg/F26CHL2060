# bouble sort

listValues = []
listLength = 0
stepCount = 0

with open ("challenge.data", "r") as rawFile:
    for eachLine in rawFile:
        valueClean = eachLine.strip()
        listLength = listLength + 1
        listValues.append(float(valueClean))


while stepCount < listLength:
    listPossition = 0
    while listPossition < listLength - stepCount - 1:
        if listValues[listPossition] > listValues[listPossition + 1]:
            temp = listValues[listPossition]
            listValues[listPossition] = listValues[listPossition + 1]
            listValues[listPossition + 1] = temp
        listPossition = listPossition + 1
    stepCount = stepCount + 1


with open("challenge.out", "w") as outputFile:
    for value in listValues:
        outputFile.write(str(value) + "\n")