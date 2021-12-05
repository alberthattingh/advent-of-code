def readInputData():
    lineSegments = []
    with open('2021/input/Day05.txt') as f:
        for text in f.readlines():
            [start, end] = text.strip().split(' -> ')
            start = start.strip().split(',')
            end = end.strip().split(',')

            lineSegments.append([list(map(lambda x: int(x), start)), list(map(lambda x: int(x), end))])

    return lineSegments


def plotPoints(lines):
    points = []
    for [start, end] in lines:
        [x1, y1] = start
        [x2, y2] = end

        if x1 == x2:
            step = 1 if y1 <= y2 else -1

            for y in range(y1, y2+step, step):
                filteredPoints = list(filter(lambda p: p['x'] == x1 and p['y'] == y, points))

                if len(filteredPoints) > 0:
                    filteredPoints[0]['count'] += 1
                else:
                    points.append({
                        'x': x1,
                        'y': y,
                        'count': 1
                    })

        elif y1 == y2:
            step = 1 if x1 <= x2 else -1

            for x in range(x1, x2+step, step):
                filteredPoints = list(filter(lambda p: p['x'] == x and p['y'] == y1, points))

                if len(filteredPoints) > 0:
                    filteredPoints[0]['count'] += 1
                else:
                    points.append({
                        'x': x,
                        'y': y1,
                        'count': 1
                    })

    return points


def s1():
    lines = readInputData()
    points = plotPoints(lines)

    overlaps = 0
    for p in points:
        if p['count'] > 1:
            overlaps += 1

    print(f'Solution 1: {overlaps}')


if __name__ == '__main__':
    s1()