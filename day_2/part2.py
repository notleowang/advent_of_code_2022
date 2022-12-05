inputFile = open('input', 'r')
lines = inputFile.readlines()

# rock = 1
# paper = 2
# scissors = 3

# rock (X) -> lose
# paper (Y) -> draw
# scissors (Z) -> win

dict = {
    'A': 'ROCK',
    'B': 'PAPER',
    'C': 'SCISSORS'
}

score = 0

for line in lines:
    shapes = line.split(" ")
    shape1 = dict[shapes[0]]
    shape2 = shapes[1].replace("\n", "")

    match shape1:
        case 'ROCK':
            match shape2:
                case 'X':
                    score += 0 + 3 # need to pick scissors
                case 'Y':
                    score += 3 + 1 # need to pick rock
                case 'Z':
                    score += 6 + 2 # need to pick paper
        case 'PAPER':
            match shape2:
                case 'X':
                    score += 0 + 1 # need to pick rock
                case 'Y':
                    score += 3 + 2 # need to pick paper
                case 'Z':
                    score += 6 + 3 # need to pick scissors
        case 'SCISSORS':
            match shape2:
                case 'X':
                    score += 0 + 2 # need to pick paper
                case 'Y':
                    score += 3 + 3 # need to pick scissors
                case 'Z':
                    score += 6 + 1 # need to pick rock

print(score)