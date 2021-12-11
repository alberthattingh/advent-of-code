def readInputData():
    octopi = []
    with open('2021/input/Day11.txt') as f:
        for row in f.readlines():
            octopi.append([int(octopus) for octopus in row.strip()])

    return octopi


def getNeighbouringOctopi(rowIndex, octoIndex):
    neighbours = []

    if rowIndex != 0:
        neighbours.append((rowIndex-1, octoIndex)) # Top

        if octoIndex != 0:
            neighbours.append((rowIndex-1, octoIndex-1)) # Top Left

        if octoIndex != 9:
            neighbours.append((rowIndex-1, octoIndex+1)) # Top Right

    if rowIndex != 9:
        neighbours.append((rowIndex+1, octoIndex)) # Bottom

        if octoIndex != 0:
            neighbours.append((rowIndex+1, octoIndex-1)) # Bottom Left

        if octoIndex != 9:
            neighbours.append((rowIndex+1, octoIndex+1)) # Bottom Right

    if octoIndex != 0:
        neighbours.append((rowIndex, octoIndex-1)) # Left

    if octoIndex != 9:
        neighbours.append((rowIndex, octoIndex+1)) # Right

    return neighbours


def flash(allOctopi):
    alreadyFlashed = []
    leftToFlash = list(filter(lambda x: x > 9, [octo for row in allOctopi for octo in row]))

    while len(alreadyFlashed) != len(leftToFlash):
        for rowIndex, row in enumerate(allOctopi):
                for octoIndex, energy in enumerate(row):
                    if energy > 9 and f'{rowIndex}{octoIndex}' not in alreadyFlashed:
                        alreadyFlashed.append(f'{rowIndex}{octoIndex}')
                        neighbours = getNeighbouringOctopi(rowIndex, octoIndex)

                        for (i1, i2) in neighbours:
                            allOctopi[i1][i2] += 1

        leftToFlash = list(filter(lambda x: x > 9, [octo for row in allOctopi for octo in row]))

    for coordinate in alreadyFlashed:
        [i1, i2] = [index for index in coordinate]
        allOctopi[int(i1)][int(i2)] = 0

    return len(alreadyFlashed)


def s1():
    octopi = readInputData()
    steps = 100
    flashes = 0

    for step in range(steps):
        for rowIndex, row in enumerate(octopi):
            for octoIndex, energy in enumerate(row):
                row[octoIndex] += 1

        flashes += flash(octopi)

    print(f'Solution 1: {flashes}')



def s2():
    octopi = readInputData()
    step = 0
    
    while True:
        step += 1
        for rowIndex, row in enumerate(octopi):
            for octoIndex, energy in enumerate(row):
                row[octoIndex] += 1

        flashesThisStep = flash(octopi)
        if flashesThisStep == 100:
            break

    print(f'Solution 2: {step}')


if __name__ == '__main__':
    s1()
    s2()