def readInputData():
    paths = []
    with open('2021/input/Day12.txt') as f:
        for row in f.readlines():
            segment = row.strip().split('-')

            if segment[1] == 'start':
                segment.reverse()

            if 'start' not in segment and 'end' not in segment:
                segment.sort()

            paths.append(segment)

    return paths


def setupPathsMap(segmentsList):
    pathsMap = {}

    # Add segments to map
    for [start, end] in segmentsList:
        if start in pathsMap.keys():
            pathsMap[start].append(end)
        else:
            pathsMap[start] = [end]

    # Add reverse segments to map
    for [start, end] in segmentsList:
        if end in pathsMap.keys() and start not in pathsMap[end]:
            pathsMap[end].append(start)
        elif end not in pathsMap.keys():
            pathsMap[end] = [start]

    return pathsMap
    

def getPaths(pathsMap, current, previousSteps = [], allowOneBack = False):
    initialAllowance = allowOneBack
    previousSteps.append(current)
    paths = []

    for next in pathsMap[current]:
        allowOneBack = allowOneBack and next != 'start'
        canContinue = next.isupper() or next not in previousSteps

        if canContinue or allowOneBack:
            allowOneBack = allowOneBack if canContinue else False

            if next == 'end':
                previousSteps.append(next)
                paths.append([step for step in previousSteps])
                previousSteps.pop()
            elif next in pathsMap.keys():
                paths.extend(getPaths(pathsMap, next, previousSteps, allowOneBack=allowOneBack))
                previousSteps.pop()

        allowOneBack = initialAllowance
    
    return paths


def s1():
    pathSegments = readInputData()
    pathsMap = setupPathsMap(pathSegments)

    # Get all possible paths from start to end
    paths = getPaths(pathsMap, 'start')

    print(f'Solution 1: {len(paths)}')


def s2():
    pathSegments = readInputData()
    pathsMap = setupPathsMap(pathSegments)

    # Get all possible paths from start to end
    paths = getPaths(pathsMap, 'start', allowOneBack=True)

    print(f'Solution 2: {len(paths)}')


if __name__ == '__main__':
    s1()
    s2()
