

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) #row #col
    return None

def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print(' - '*10)

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print('|', end = "")
            print(f' {board[i][j]} ', end = "")
            if j == len(board[0]) - 1:
                print('')


def valid(board, num, position):
    num = int(num)
    row, col = position

    #Check Row
    for i in range(len(board[row])):
        if board[row][i] == num and col != i:
            return False

    #Check Col
    for i in range(len(board)):
        if board[i][col] == num and row != i:
            return False

    #Check Square
    for i in range(row//3 *3, row//3 *3 +3):
        for j in range(col//3 *3, col//3 *3 +3):
            if board[i][j] == num and (i,j) != position:
                return False

    return True


def solve(board):
    find = findEmpty(board)
    if not find:
        return True

    else:
        row, col = find
        for i in range(1,10):
            if valid(board, i, find):
                board[row][col] = i

                if solve(board):
                    return True
                else:
                    board[row][col] = 0
        return False

