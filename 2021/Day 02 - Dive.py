from itertools import accumulate
import operator

def readLines():
    directions = []

    with open('2021/input/Day02.txt') as f:
        for line in f.readlines():
            directions.append(line)

    return directions


def horizontal(directions):
    return list(accumulate(list(map(lambda x: int(x.split(" ")[1]), list(filter(lambda x: 'forward' in x, directions)))), operator.add)).pop()


def down(directions):
    return list(accumulate(list(map(lambda x: int(x.split(" ")[1]), list(filter(lambda x: 'down' in x, directions)))), operator.add)).pop()


def up(directions):
    return list(accumulate(list(map(lambda x: int(x.split(" ")[1]), list(filter(lambda x: 'up' in x, directions)))), operator.add)).pop()


def s1():
    directions = readLines()

    h = horizontal(directions)
    d = down(directions)
    u = up(directions)

    print('Solution 1:', h * (d - u))


def s2():
    directions = readLines()

    horizontalPostion = 0
    depth = 0
    aim = 0

    for d in directions:
        [action, value] = list(map(lambda x: x.strip(), d.split(" ")))
        if action == "forward":
            horizontalPostion += int(value)
            depth += aim * int(value)
        elif action == "down":
            aim += int(value)
        else:
            aim -= int(value)

    print('Solution 2:', horizontalPostion * depth)



if __name__ == "__main__":
    s1()
    s2()