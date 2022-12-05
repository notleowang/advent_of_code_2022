inputFile = open('input', 'r')
rugsacks = inputFile.readlines()

itemsList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
             'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def getPriority(item):
    return itemsList.index(item)

sum = 0

counter = 0
rugsackGroup = []
for rugsack in rugsacks:
    rugsack = rugsack[:-1] # gets rid of newline character lol
    counter += 1
    rugsackGroup.append(rugsack)

    visited = []
    if counter % 3 == 0:
        for item1 in rugsackGroup[0]:
            if (item1 in (item2 for sublist in rugsackGroup[1] for item2 in sublist) and 
                item1 in (item3 for sublist in rugsackGroup[2] for item3 in sublist) and
                item1 not in visited):
                visited.append(item1)
                sum += getPriority(item1) + 1

        rugsackGroup = []

print(sum)