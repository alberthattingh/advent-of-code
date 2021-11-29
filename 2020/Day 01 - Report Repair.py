
def readInputFile(path):
    entries = []

    with open(path, 'r') as f:
        for line in f.readlines():
            entries.append(int(line))

    return entries


def getProductOfPair(expenseReport):
    answer = None
    for number in expenseReport:
        for otherNumber in expenseReport:
            if number + otherNumber == 2020:
                answer = number * otherNumber
                break

        if answer != None:
            break

    return answer


def getProductOfTrio(expenseReport):
    expenseReport = readInputFile('2020/inputs/Day01.txt')
    
    answer = None
    for number in expenseReport:
        for otherNumber in expenseReport:
            for yetAnotherNumber in expenseReport:
                if number + otherNumber + yetAnotherNumber == 2020:
                    answer = number * otherNumber * yetAnotherNumber
                    break

            if answer != None:
                break

        if answer != None:
            break

    return answer


def main():
    expenseReport = readInputFile('2020/inputs/Day01.txt')
    answer1 = getProductOfPair(expenseReport)
    answer2 = getProductOfTrio(expenseReport)
        
    print(f"Problem 1: {answer1}\nProblem 2: {answer2}")


if __name__ == '__main__':
    main()