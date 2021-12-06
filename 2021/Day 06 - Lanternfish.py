def readInputData():
    fish = []
    with open('2021/input/Day06.txt') as f:
        fish = list(map(lambda x: int(x), f.readline().strip().split(',')))

    return fish


def s1():
    day = 0
    lanternFish = readInputData()

    while day < 80:
        newFish = []
        for index in range(len(lanternFish)):
            if lanternFish[index] == 0:
                newFish.append(8)
                lanternFish[index] = 6

            else:
                lanternFish[index] -= 1
        
        lanternFish.extend(newFish)
        day += 1

    print(f'Solution 1: {len(lanternFish)}')


def s2():
    day = 0
    initialFish = readInputData()
    fishByAge = [0 for n in range(9)]

    for index in range(9):
        fishByAge[index] = len(list(filter(lambda fish: fish == index, initialFish)))

    while day < 256:
        temp = fishByAge.pop(0)
        fishByAge[6] += temp
        fishByAge.insert(8, temp)

        day += 1

    print(f'Solution 2: {sum(fishByAge)}')
        



if __name__ == '__main__':
    s1()
    s2()