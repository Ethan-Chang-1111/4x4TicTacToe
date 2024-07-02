
import numpy as np

def main():
    # Board is represented as a 4x4 np array. 
    # 1 represents 'X' and -1 represents 'O'
    # 0 represents an empty space
    testBoard = np.zeros((4,4))

# Mutates given board to add 1 to specified location
# Board is 4x4 np array
# loc is a tuple
def addX(board, loc):
    add(board, loc, 1)

# Mutates given board to add 1 to specified location
# Board is 4x4 np array
# loc is a tuple
def addO(board, loc):
    add(board, loc, -1)

# Mutates given board to add val to specified location
# Board is 4x4 np array
# loc is a tuple
# val is 1 or -1
def add(board, loc, val):
    if board[loc] == 0:
        board[loc] = val
    else:
        raise ValueError("Can't place on an occupied location")

# check if there is a winner
# True if there is a winner
# Needs to return who the winner is
def checkWinner(board):
    # Verticals
    vert = np.sum(board, axis=0)
    print(vert)

    # Horizontals

    # Diagonals

    # Corners

    # 2x2's

    return

# checks if there are any legal moves left to play
# returns True if there are no more moves to play
def anyMovesLeft(board):
    # takes the sum of the entire board
    # a filled board will have an equal number of 1, and -1
    # so the sum of a filled board will be 0

    # the sum of an empty board will also be 0, so check for that too
    if board[0,0] == 0:
        return False

    return np.sum(board) == 0
    

# returns true if the game is over, false if not
# game is over if a player one or if there are no more moves left
def isGameOver(board):
    return checkWinner(board) or anyMovesLeft(board)

if __name__ == "__main__":
    main()