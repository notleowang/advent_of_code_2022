inputFile = open('input', 'r')
lines = inputFile.readlines()

calories = 0

elves = []

for line in lines:
    if (line == "\n"):
        elves.append(calories)
        calories = 0
    else:
        calories += int(line)

elves.sort()
total = 0

for i in range(3):
    total += elves.pop(-1)

print(total)