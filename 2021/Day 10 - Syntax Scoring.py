def readInputData():
    chunks = []
    with open('2021/input/Day10.txt') as f:
        for row in f.readlines():
            chunks.append(row.strip())

    return chunks


def getValidLines(chunks):
    pointsMap = {')': 3, ']': 57, '}': 1197, '>': 25137}
    openingChars = ['(', '[', '{', '<']
    closingChars = [')', ']', '}', '>']

    syntaxErrorScore = 0
    validLines = []

    for line in chunks:
        expectedClosingChars = []
        valid = True

        for char in line:
            if char in openingChars:
                index = openingChars.index(char)
                expectedClosingChars.insert(0, closingChars[index])
            else:
                if len(expectedClosingChars) == 0 or char != expectedClosingChars[0]:
                    syntaxErrorScore += pointsMap[char]
                    valid = False
                    break
                else:
                    expectedClosingChars.pop(0)

        if valid:
            validLines.append([line, expectedClosingChars])

    return [syntaxErrorScore, validLines]


def s1():
    chunks = readInputData()
    [syntaxErrorScore, validLines] = getValidLines(chunks)

    print(f'Solution 1: {syntaxErrorScore}')


def s2():
    pointsMap = {')': 1, ']': 2, '}': 3, '>': 4}

    chunks = readInputData()
    [syntaxErrorScore, validLines] = getValidLines(chunks)

    completionScores = []
    for [validLine, expected] in validLines:
        score = 0
        for char in expected:
            score *= 5
            score += pointsMap[char]

        completionScores.append(score)

    completionScores = sorted(completionScores)

    print(f'Solution 2: {completionScores[int(len(completionScores) / 2)]}')


if __name__ == '__main__':
    s1()
    s2()