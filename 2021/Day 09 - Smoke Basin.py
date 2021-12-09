def readInputData():
    heightMap = []
    with open('2021/input/Day09.txt') as f:
        for row in f.readlines():
            mappedRow = [int(num) for num in row.strip()]
            heightMap.append(mappedRow)

    return heightMap


def getLowPoints(heightMap):
    lowPoints = []

    for rowIndex, row in enumerate(heightMap):
        goal = 4 if rowIndex != 0 and rowIndex != len(heightMap) - 1 else 3

        for numIndex, num in enumerate(row):
            goal = goal - 1 if numIndex == 0 or numIndex == len(row) - 1 else goal
            lowPointCount = 0

            lowPointCount += 1 if numIndex != 0 and row[numIndex-1] > num else 0
            lowPointCount += 1 if numIndex != len(row) - 1 and row[numIndex+1] > num else 0
            lowPointCount += 1 if rowIndex != 0 and heightMap[rowIndex-1][numIndex] > num else 0
            lowPointCount += 1 if rowIndex != len(heightMap) - 1 and heightMap[rowIndex+1][numIndex] > num else 0

            if lowPointCount == goal:
                lowPoints.append([rowIndex, numIndex, num])

            goal = 4 if rowIndex != 0 and rowIndex != len(heightMap) - 1 else 3

    return lowPoints


def getBasinSize(lowPoints, heightMap, size = 1, alreadyChecked = []):
    basin = []

    for [rowIndex, numIndex, num] in lowPoints:
        if rowIndex != 0:
            neighbour = heightMap[rowIndex-1][numIndex]
            if neighbour >= num and neighbour != 9 and [rowIndex-1, numIndex, neighbour] not in alreadyChecked:
                basin.append([rowIndex-1, numIndex, neighbour])

        if numIndex != 0:
            neighbour = heightMap[rowIndex][numIndex-1]
            if neighbour >= num and neighbour != 9 and [rowIndex, numIndex-1, neighbour] not in alreadyChecked:
                basin.append([rowIndex, numIndex-1, neighbour])

        if rowIndex != len(heightMap) - 1:
            neighbour = heightMap[rowIndex+1][numIndex]
            if neighbour >= num and neighbour != 9 and [rowIndex+1, numIndex, neighbour] not in alreadyChecked:
                basin.append([rowIndex+1, numIndex, neighbour])

        if numIndex != len(heightMap[0]) - 1:
            neighbour = heightMap[rowIndex][numIndex+1]
            if neighbour >= num and neighbour != 9 and [rowIndex, numIndex+1, neighbour] not in alreadyChecked:
                basin.append([rowIndex, numIndex+1, neighbour])

        
        alreadyChecked.extend(basin)

    if len(basin) == 0:
        return size + len(basin)
    else:
        return getBasinSize(basin, heightMap, size + len(basin), alreadyChecked)



def s1():
    heightMap = readInputData()
    lowPoints = getLowPoints(heightMap)
    riskLevels = [1 + point[2] for point in lowPoints]    

    print(f'Solution 1: {sum(riskLevels)}')


def s2():
    heightMap = readInputData()
    lowPoints = getLowPoints(heightMap)
    basinSizes = [getBasinSize([point], heightMap) for point in lowPoints]
    basinSizes = sorted(basinSizes, reverse=True)

    print(f'Solution 2: {basinSizes[0] * basinSizes[1] * basinSizes[2]}')


if __name__ == '__main__':
    s1()
    s2()