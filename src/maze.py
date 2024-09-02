
def maze(row,column):
    if row==1 or column==1: ## if reach at end of column there will be only downward option and if row end ..forward only to destination

        return 1
    left=maze(row-1,column)
    right=maze(row,column-1)
    return left+right

def maze_path(ans,row,column):
    result=[]
    if row==1 and column==1:
        result.append(ans)
        return result
    collect=[]
    if row>1:
        collect.extend(maze_path(ans+'D',row-1,column))
    if column>1:
        collect.extend(maze_path(ans+'R',row,column-1))
    return collect
def maze_path_diagonal(ans,row,column):
    result=[]
    if row==1 and column==1:
        result.append(ans)
        return result
    #collect=[]
    if row>1 and column>1:
        result.extend(maze_path_diagonal(ans+'D',row-1,column-1))
    if row>1:
        result.extend(maze_path_diagonal(ans+'V',row-1,column))
    if column>1:
        result.extend(maze_path_diagonal(ans+'H',row,column-1))
    return result
def maze_path_obstacle(ans, maze, row,column):
    result=[]
    if len(maze)-1==row and column==len(maze[0])-1:
        result.append(ans)
        return result
    if maze[row][column]==False: #if obstacle so stop recursive for that point
        return ""
    # if row<len(maze) and column<len(maze[0]):
    #     result.extend(maze_path_obstacle(ans+'D',maze,row-1,column-1))
    if row<len(maze)-1:
        result.extend(maze_path_obstacle(ans+'V',maze,row+1,column))
    if column<len(maze[0])-1:
        result.extend(maze_path_obstacle(ans+'H',maze,row,column+1))
    return  result

"""
lets up have to move left right up and down ..
if we go left right , up and down .. it will be infinite recursion 
so we need to mark the visited node but this also create the problem means.. visited node may be 2-3 option so
we need to use back tracking 
lets marked visited and then we goes make on same recursion return .. un marked that previous node so
we can think what will be the next option path from there
"""
def backtracking(ans,maze,row,col):
    if row==len(maze)-1 and len(maze[0])-1==col:
        print(ans)
        return
    if maze[row][col]==False: ##  obstacle  so exit from that point
        return
    maze[row][col]=False # marked as visited for that recursion call so considering this path in my path
    if row<len(maze)-1:
        backtracking(ans+'D',maze,row+1,col)
    if col<len(maze[0])-1:
        backtracking(ans+'R',maze,row,col+1)
    if row>0:
        backtracking(ans+'U',maze,row-1,col)
    if col>0:
        backtracking(ans+'L',maze,row,col-1)
    maze[row][col]=True # backtracking  functiion will be over then before exit function  unmarked that point



def backtracking_path(ans,maze,row,col,path,step):
    if row==len(maze)-1 and len(maze[0])-1==col:
        path[row][col]=step
        for p in path:
            print(p)
        print(ans)
        print()
        return
    if maze[row][col]==False: ##  obstacle  so exit from that point
        return
    maze[row][col]=False # marked as visited for that recursion call so considering this path in my path
    path[row][col]=step
    if row<len(maze)-1:
        backtracking_path(ans+'D',maze,row+1,col,path,step+1)
    if col<len(maze[0])-1:
        backtracking_path(ans+'R',maze,row,col+1,path,step+1)
    if row>0:
        backtracking_path(ans+'U',maze,row-1,col,path,step+1)
    if col>0:
        backtracking_path(ans+'L',maze,row,col-1,path,step+1)
    maze[row][col]=True # backtracking  functiion will be over then before exit function  unmarked that point
    path[row][col]=0
def main():
     print(maze(3,3))
     print(maze_path("",3,3))
     print(maze_path_diagonal("",3,3))
     maze1=[[True,True,True],[True,True,True],[True,True,True]]
     print(maze_path_obstacle("",maze1,0,0))
     print("*"*20)
     backtracking("",maze1,0,0)
     print("*"*20)
     path=[[0 for _ in range(len(maze1[0]))] for _ in range(len(maze1))]
     print(path)
     backtracking_path("",maze1,0,0,path,1)

if __name__=="__main__":
    main()