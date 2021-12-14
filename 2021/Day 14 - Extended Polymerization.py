from more_itertools import pairwise

def readInputData():
    rules = {}
    template = None
    with open('2021/input/Day14.txt') as f:
        template = f.readline().strip()

        for row in f.readlines():
            if row.strip() == '':
                continue

            [pair, result] = row.strip().split(' -> ')
            rules[pair] = result

    return [template, rules]


def s1():
    [template, rules] = readInputData()

    for _ in range(10):
        resultingTemplate = ''
        for index, pair in enumerate(pairwise(template)):
            pairString = ''.join(pair)
            if index == 0:
                resultingTemplate += pair[0]

            resultingTemplate += rules[pairString]
            resultingTemplate += pair[1]

        template = resultingTemplate

    mostCommon = 0
    leastCommon = None
    for letter in rules.values():
        count = template.count(letter)
        mostCommon = max(mostCommon, count)
        leastCommon = count if leastCommon == None else min(leastCommon, count)

    print(f'Solution 1: {mostCommon - leastCommon}')


def s2():
    [template, rules] = readInputData()

    letterCount = {}
    for letter in template:
        if letter in letterCount.keys():
            letterCount[letter] += 1
        else:
            letterCount[letter] = 1

    templateMap = {}
    for pair in pairwise(template):
        pairString = ''.join(pair)
        if pairString in templateMap.keys():
            templateMap[pairString] += 1
        else:
            templateMap[pairString] = 1

    for _ in range(40):
        newTemplateMap = {}

        for pair in templateMap.keys():
            count = templateMap[pair]
            [a, b] = [letter for letter in pair]
            c = rules[pair]
            
            letterCount[c] = letterCount[c] + count if c in letterCount.keys() else count

            newTemplateMap[f'{a}{c}'] = newTemplateMap[f'{a}{c}'] + count if f'{a}{c}' in newTemplateMap.keys() else count
            newTemplateMap[f'{c}{b}'] = newTemplateMap[f'{c}{b}'] + count if f'{c}{b}' in newTemplateMap.keys() else count

        templateMap = newTemplateMap

    print(f'Solution 2: {max(letterCount.values()) - min(letterCount.values())}')


if __name__ == '__main__':
    s1()
    s2()