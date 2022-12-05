inputFile = open('input', 'r')
lines = inputFile.readlines()

# rock = 1
# paper = 2
# scissors = 3

# lose = 0
# draw = 3
# win = 6

dict = {
    'A': 'ROCK',
    'B': 'PAPER',
    'C': 'SCISSORS',
    'X': 'ROCK',
    'Y': 'PAPER',
    'Z': 'SCISSORS'
}

score = 0

for line in lines:
    shapes = line.split(" ")
    shape1 = dict[shapes[0]]
    shape2 = dict[shapes[1].replace("\n", "")]

    match shape2:
        case 'ROCK':
            score += 1
            match shape1:
                case 'ROCK':
                    score += 3
                case 'PAPER':
                    score += 0
                case 'SCISSORS':
                    score += 6
        case 'PAPER':
            score += 2
            match shape1:
                case 'ROCK':
                    score += 6
                case 'PAPER':
                    score += 3
                case 'SCISSORS':
                    score += 0
        case 'SCISSORS':
            score += 3
            match shape1:
                case 'ROCK':
                    score += 0
                case 'PAPER':
                    score += 6
                case 'SCISSORS':
                    score += 3

print(score)