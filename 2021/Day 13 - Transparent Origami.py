import matplotlib.pyplot as plt

def readCoordinatesAndInstructions():
    coordinates = []
    instructions = []

    with open('2021/input/Day13.txt') as f:
        for row in f.readlines():
            if 'fold along' in row:
                [axis, value] = row.strip().replace('fold along ', '').split('=')
                instructions.append([axis, int(value)])
            
            elif row.strip() == '':
                continue

            else:
                [x, y] = [int(value) for value in row.strip().split(',')]
                coordinates.append({ 'x': x, 'y': y})
            

    return [coordinates, instructions]


def fold(grid, foldIndex, foldAxis):
    otherAxis = 'y' if foldAxis == 'x' else 'x'
    newGrid = {}

    for dot in grid:
        newDot = None
        if dot[foldAxis] < foldIndex:
            newDot = dot
        else:
            newIndex = foldIndex - (dot[foldAxis] - foldIndex)
            newDot = {foldAxis: newIndex, otherAxis: dot[otherAxis]}

        newGrid[f"{newDot['x']}{newDot['y']}"] = newDot

    return list(newGrid.values())


def s1():
    [grid, instructions] = readCoordinatesAndInstructions()
    
    newGrid = fold(grid, instructions[0][1], instructions[0][0])
    print(f'Solution 1: {len(newGrid)}')


def s2():
    [grid, instructions] = readCoordinatesAndInstructions()

    for [axis, index] in instructions:
        grid = fold(grid, index, axis)

    x = [coordinates['x'] for coordinates in grid]
    y = [coordinates['y'] for coordinates in grid]

    print("Solution 2: See graph (widen and flip vertically)")
    plt.scatter(x, y)
    plt.show()


if __name__ == '__main__':
    s1()
    s2()