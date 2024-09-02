import math


def sudoku(board):
    n = len(board)
    r = -1
    c = -1
    emptyLeft = True
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                r = i
                c = j
                emptyLeft = False
                break
        if emptyLeft == False:
            break
    if emptyLeft == True:
        return True
    for number in range(1, 9 + 1):
        if safe(board, r, c, number):
            board[r][c] = number
            if sudoku(board):
               # display(board)
                return True
            else:
                board[r][c] = 0
    return False


def display(board):
    for row in board:
        for element in row:
            print(element, end=" ")

        print("")


def safe(board, r, c, num):
    # check row
    for i in range(len(board)):
        if board[r][i] == num:
            return False

    for row in board:
        if row[c] == num:
            return False
    sqr_num = int(math.sqrt(len(board)))
    row_start = r - r % sqr_num
    col_start = c - c % sqr_num
    for i in range(row_start, row_start + sqr_num):
        for j in range(col_start, col_start + sqr_num):
            if board[i][j] == num:
                return False
    return True


def main():
    print("*" * 20)
    input =[[5,1,7,6,0,0,0,3,4], #0
            [2,8,9,0,0,4,0,0,0], #1
            [3,4,6,2,0,5,0,9,0], #2
            [6,0,2,0,0,0,0,1,0], #3
            [0,3,8,0,0,6,0,4,7], #4
            [0,0,0,0,0,0,0,0,0], #5
            [0,9,0,0,0,0,0,7,8], #6
            [7,0,3,4,0,0,5,6,0], #7
            [0,0,0,0,0,0,0,0,0]] #8


    if sudoku(input):
        display(input)
    else:
        print("Not able to solve ")


if __name__ == "__main__":
    main()
