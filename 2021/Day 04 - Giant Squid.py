def readInputData():
    numbers = []
    boards = []
    with open('2021/input/Day04.txt') as f:
        numbers = list(map(lambda x: int(x), f.readline().split(',')))

        board = []
        for line in f.readlines():
            if line == '\n':
                if len(board) > 0:
                    boards.append(board)
                    board = []
                continue
            
            row = list(map(lambda x: int(x), line.strip().split()))
            board.append(row)

    return [numbers, boards]


def updateBoards(boards, number):
    for board in boards:
        for row in board:
            for index, n in enumerate(row):
                if n == number:
                    row[index] = 'x'

    return boards


def checkForWinner(boards):
    for (index, board) in enumerate(boards):
        for row in board:
            if ''.join(list(map(lambda x: str(x), row))) == 'xxxxx':
                return (index, board)

        for i in range(len(board)):
            column = [row[i] for row in board]
            if ''.join(list(map(lambda x: str(x), column))) == 'xxxxx':
                return (index, board)
    
    return None


def removeCompleteBoards(boards):
    winner = checkForWinner(boards)
    while winner != None:
        boards.pop(winner[0])
        winner = checkForWinner(boards)

    return boards
        

def s1():
    [numbers, boards] = readInputData()

    score = None
    for n in numbers:
        boards = updateBoards(boards, n)
        winner = checkForWinner(boards)

        if winner != None:
            boardValues = list(filter(lambda x: str(x) != 'x', [value for row in winner[1] for value in row]))
            score = sum(boardValues) * n
            break

    print(f'Solution 1: {score}')


def s2():
    [numbers, boards] = readInputData()

    score = None
    for n in numbers:
        boards = updateBoards(boards, n)
        winner = checkForWinner(boards)

        if winner != None:
            if len(boards) > 1:
                boards = removeCompleteBoards(boards)
            else:
                boardValues = list(filter(lambda x: str(x) != 'x', [value for row in winner[1] for value in row]))
                score = sum(boardValues) * n
                break

    print(f'Solution 2: {score}')


if __name__ == '__main__':
    s1()
    s2()