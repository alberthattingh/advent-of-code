def readInputData():
    positions = []
    with open('2021/input/Day07.txt') as f:
        positions = list(map(lambda x: int(x), f.readline().strip().split(',')))

    return positions


def s1():
    crabPositions = readInputData()
    fuelPredictions = []

    for goalPosition in crabPositions:
        totalFuel = 0

        for currentPosition in crabPositions:
            fuel = abs(goalPosition - currentPosition)
            totalFuel += fuel

        fuelPredictions.append(totalFuel)

    print(f'Solution 1: {min(fuelPredictions)}')


def s2():
    crabPositions = readInputData()
    fuelPredictions = []

    for goalPosition in crabPositions:
        totalFuel = 0

        for currentPosition in crabPositions:
            fuel = abs(goalPosition - currentPosition)
            totalFuel += sum([n + 1 for n in range(fuel)])

        fuelPredictions.append(totalFuel)

    print(f'Solution 2: {min(fuelPredictions)}')


if __name__ == '__main__':
    s1()
    s2()