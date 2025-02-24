import random

GRID_SIZE = 9
def checkValidNumInRow(board,num,row):
    for i in range(0,GRID_SIZE):
        if board[row][i] == num:
            return True
    return False

def checkValidNumInCol(board,col,num):
    for i in range(0,GRID_SIZE):
        if board[i][col] == num:
            return True
    return False

def checkValidNumInBox(board,num,row,col):
    currentBoxRow = row - row % 3
    currentBoxCol = col - col % 3
    for i in range(currentBoxRow,currentBoxRow + 3):
        for j in range(currentBoxCol,currentBoxCol + 3):
            if board[i][j] == num:
                return True
    return False


def checkValidPlacement(board, num, row, col):
    return not checkValidNumInRow(board, num, row) and not checkValidNumInCol(board, col, num) and not checkValidNumInBox(board, num, row, col)
  

def backtracking(board):
    for row in range(0,GRID_SIZE):
        for col in range(0,GRID_SIZE):
            if board[row][col] == 0:
                for num in range(1,10):
                    if checkValidPlacement(board,num,row,col):
                        board[row][col] = num
                        
                        if backtracking(board):
                            return True
                        else:
                            board[row][col] = 0
                return False
    return True

def printBoard(board):
    for row in range(0, GRID_SIZE):
        if row % 3 == 0 and row != 0:
            print("-----------")
        for col in range(0, GRID_SIZE):
            if col % 3 == 0 and col != 0:
                print("|", end=" ")
            print(board[row][col], end=" ")
        print()


if __name__ == "__main__":
    board = [[7,0,2,0,5,0,6,0,0],
             [0,0,0,0,0,3,0,0,0],
             [1,0,0,0,0,9,5,0,0],
             [8,0,0,0,0,0,0,9,0],
             [0,4,3,0,0,0,7,5,0],
             [0,9,0,0,0,0,0,0,8],
             [0,0,9,7,0,0,0,0,5],
             [0,0,0,2,0,0,0,0,0],
             [0,0,7,0,4,0,2,0,3]]
    print("Game trước khi giải")
    for row in range(0, GRID_SIZE):
        if row % 3 == 0 and row != 0:
            print("-----------")
        for col in range(0, GRID_SIZE):
            if col % 3 == 0 and col != 0:
                print("|", end=" ")
            print(board[row][col], end=" ")
        print()
    if(backtracking(board)):
        print("Giai thanh cong")
    else:
        print("Khong giai duoc")
    printBoard(board)
    