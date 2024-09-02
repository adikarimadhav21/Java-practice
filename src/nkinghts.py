def knight(board, r, c, knights):
    if knights==0:
        display(board)
        print("")
    if r==len(board)-1 and c==len(board): # skip if at last
        return
    if c==len(board):  #new line if all columns for that row completed
        knight(board,r+1,0,knights)
        return

    if isSafe(board,r,c):
        board[r][c]=True
        knight(board,r,c+1,knights-1)
        board[r][c]=False #back tracking
    knight(board,r,c+1,knights) #move ahead without placing


def isSafe(board,r,c):
    if isValid(board,r-2,c-1):
        if board[r-2][c-1]:
            return  False
    if isValid(board,r-1,c-2):
        if board[r-1][c-2]:
            return  False
    if isValid(board,r-2,c+1):
        if board[r-2][c+1]:
            return  False
    if isValid(board,r-1,c+2):
        if board[r-1][c+2]:
            return  False
    return  True

def isValid(board,r,c):
    if r>=0 and r<len(board) and  c>=0 and c<len(board):
        return  True
    return False
def display(board):
    for row in board:
        for element in row:
            if element:
                print("K",end=" ")
            else:
                print("X", end=" ")
        print("")

def main():
    print("*"*20)
    n=4
    board=[[0 for _ in range(n)] for _ in range(n)]
    knight(board, 0, 0, n)

if __name__=="__main__":
    main()