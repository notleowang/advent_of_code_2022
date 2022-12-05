inputFile = open('input', 'r')
rugsacks = inputFile.readlines()

itemsList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
             'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def getPriority(item):
    return itemsList.index(item)

sum = 0

for rugsack in rugsacks:
    rugsack = rugsack[:-1] # gets rid of newline character lol
    numItems = int(len(rugsack) / 2)
    firstCompartment = rugsack[0:numItems]
    secondCompartment = rugsack[numItems:]

    visited = []
    for item1 in firstCompartment:
        for item2 in secondCompartment:
            if item1 not in visited and item1 == item2:
                visited.append(item1)
                sum += getPriority(item1) + 1

print(sum)