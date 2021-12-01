def readLines():
    numbers = []

    with open('2021/input/Day01.txt') as f:
        for line in f.readlines():
            numbers.append(int(line))

    return numbers


def s1():
    report = readLines()
    previous = None
    increases = 0

    for depth in report:
        if previous != None and depth > previous:
            increases += 1
        previous = depth

    print('Solution 1:', increases)


def s2():
    report = readLines()
    previous = None
    increases = 0

    threes = list(zip(report, report[1:], report[2:]))
    for (a, b, c) in threes:
        total = a + b + c
        if previous != None and total > previous:
            increases += 1
        previous = total

    print('Solution 2:', increases)


def main():
    s1()
    s2()


if __name__ == '__main__':
    main()