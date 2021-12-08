def readInputData():
    data = []
    with open('2021/input/Day08.txt') as f:
        for line in f.readlines():
            segmentValues = list(map(lambda x: x.strip().split(' '), line.split('|')))
            data.append(segmentValues)

    return data


def calculate(code, seven, four):
    inSeven = [letter in code for letter in seven]

    if len(code) == 6:
        if all(inSeven):
            inFour = [letter in code for letter in four]
            return 9 if all(inFour) else 0
        return 6

    if all(inSeven):
        return 3
    else:
        matches = len(list(filter(lambda x: x in four, [letter for letter in code])))
        return 5 if matches == 3 else 2


def s1():
    uniqueSegments = [2, 4, 3, 7]
    data = readInputData()

    counter = 0
    for pair in data:
        for outputValue in pair[1]:
            if len(outputValue) in uniqueSegments:
                counter += 1

    print(f'Solution 1: {counter}')


def s2():
    uniqueSegments = ['x', 2, 'x', 'x', 4, 'x', 'x', 3, 7, 'x']
    data = readInputData()

    counter = 0
    for pair in data:
        outputValues = ['x' for n in range(4)]
        for index, outputCode in enumerate(pair[1]):
            if len(outputCode) in uniqueSegments:
                outputValues[index] = uniqueSegments.index(len(outputCode))

        for index, outputCode in enumerate(pair[1]):
            if outputValues[index] == 'x':
                outputValues[index] = calculate(outputCode, list(filter(lambda x: len(x) == 3, pair[0]))[0], list(filter(lambda x: len(x) == 4, pair[0]))[0])

        counter += int(''.join(list(map(lambda x: str(x), outputValues))))

    print(f'Solution 2: {counter}')


if __name__ == '__main__':
    s1()
    s2()