import numpy as np
import testBoards

def main():
    # Board is represented as a 4x4 np array. 
    # 1 represents 'X' and -1 represents 'O'
    # 0 represents an empty space
    
    board = testBoards.emptyBoard()
    print("Test Board:\n", board)

    isGameOver(board)

# check if there is a winner
# True if there is a winne
# Assumes board doesn't have more than one winning pattern
# Assumes 4x4 np.array board
def checkWinner(board):
    # Verticals
    if checkWinnerHelper(np.sum(board, axis=0)):
        return True

    # Horizontals
    if checkWinnerHelper(np.sum(board, axis=1)):
        return True

    # Diagonals
    if checkWinnerHelper(board.diagonal().sum()):
        return True
    if checkWinnerHelper(np.fliplr(board).diagonal().sum()):
        return True
    
    # Corners
    if checkWinnerHelper(board[::board.shape[0]-1, ::board.shape[1]-1].sum()):
        return True

    # 2x2's
    anchorPoints = board[:-1, :-1]
    iterator = np.nditer(anchorPoints, flags=['multi_index'])
    for x in iterator:
        i, j = iterator.multi_index
        if checkWinnerHelper(board[i:i + 2, j:j + 2].sum()):
            return True
    return False

# Check if a player won in a given set
# Prints which player won
# returns false if neither player has won
def checkWinnerHelper(pattern):
    # X wins
    if np.max(pattern) == 4:
        print("X Wins")
        return True
    # O wins
    if np.min(pattern) == -4:
        print("O Wins")
        return True
    return False

# checks if there are any legal moves left to play
# If there is a move to play, returns False
# If there are no more moves, returns True
def anyMovesLeft(board):
    # takes the sum of the entire board
    # a filled board will have an equal number of 1, and -1
    # so the sum of a filled board will be 0

    # the sum of an empty board will also be 0, so check for that too
    if board[0, 0] == 0:
        return False
    
    return np.sum(board) == 0
    
# returns true if the game is over, false if not
# game is over if a player one or if there are no more moves left
def isGameOver(board):
    if checkWinner(board) or anyMovesLeft(board):
        print("Game Over")
        return True

    print("Continue")
    return False

if __name__ == "__main__":
    main()