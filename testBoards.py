import numpy as np

def verticalWin(player):
    testBoard = np.zeros((4, 4))
    col = np.random.randint(0, 4)
    add(testBoard, (0, col), player)
    add(testBoard, (1, col), player)
    add(testBoard, (2, col), player)
    add(testBoard, (3, col), player)
    return testBoard

def horizontalWin(player):
    testBoard = np.zeros((4, 4))
    row = np.random.randint(0, 4)
    add(testBoard, (row, 0), player)
    add(testBoard, (row, 1), player)
    add(testBoard, (row, 2), player)
    add(testBoard, (row, 3), player)
    return testBoard

def diagonalWinOne(player):
    testBoard = np.zeros((4, 4))
    add(testBoard, (0, 0), player)
    add(testBoard, (1, 1), player)
    add(testBoard, (2, 2), player)
    add(testBoard, (3, 3), player)
    return testBoard
    
def diagonalWinTwo(player):
    testBoard = np.zeros((4, 4))
    add(testBoard, (0, 3), player)
    add(testBoard, (1, 2), player)
    add(testBoard, (2, 1), player)
    add(testBoard, (3, 0), player)
    return testBoard
    
def cornerWin(player):
    testBoard = np.zeros((4, 4))
    add(testBoard, (0, 0), player)
    add(testBoard, (0, 3), player)
    add(testBoard, (3, 0), player)
    add(testBoard, (3, 3), player)
    return testBoard

def squareWin(player):
    testBoard = np.zeros((4, 4))
    row = np.random.randint(0, 3)
    col = np.random.randint(0, 3)
    add(testBoard, (row, col), player)
    add(testBoard, (row + 1, col), player)
    add(testBoard, (row, col + 1), player)
    add(testBoard, (row + 1, col + 1), player)
    return testBoard

def filledBoard():
    testBoard = np.array([[1, -1, 1, -1], 
                          [-1, -1, 1, 1], 
                          [1, 1, -1, -1], 
                          [-1, 1, -1, 1]])
    return testBoard
def filledBoardButOne():
    testBoard = np.array([[1, -1, 1, -1], 
                          [-1, 0, 1, 1], 
                          [1, 1, -1, -1], 
                          [-1, 1, -1, 1]])
    return testBoard

def filledBoardButFirst():
    testBoard = np.array([[0, -1, 1, -1], 
                          [-1, -1, 1, 1], 
                          [1, 1, -1, -1], 
                          [-1, 1, -1, 1]])
    return testBoard

def emptyBoard():
    return np.zeros((4,4))

# Mutates given board to add 1 to specified location
# Board is 4x4 np.array
# loc is a tuple
def addX(board, loc):
    add(board, loc, 1)

# Mutates given board to add 1 to specified location
# Board is 4x4 np.array
# loc is a tuple
def addO(board, loc):
    add(board, loc, -1)

# Mutates given board to add val to specified location
# Board is 4x4 np.array
# loc is a tuple
# val is 1 or -1
def add(board, loc, val):
    if board[loc] == 0:
        board[loc] = val
    else:
        raise RuntimeError("Can't place on an occupied location")