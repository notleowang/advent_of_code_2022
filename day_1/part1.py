inputFile = open('input.txt', 'r')
lines = inputFile.readlines()

calories = 0

elves = []

for line in lines:
    if (line == "\n"):
        elves.append(calories)
        calories = 0
    else:
        calories += int(line)

print(max(elves))