def feb(n):
    if n<=2:
        return 1
    return feb(n-1)+feb(n-2)
    
## space O(n) to store call stack 
# time will be O(2^n) .. expensive  
# ## see tree of function call there are duplicate or overllaping computation

#memoization : cache ..time O(n) and space O(n)

def feb(n,memo):
    if n<=2:
        return 1
    if n in memo:
        return memo[n]
    memo[n]=feb(n-1,memo)+feb(n-2,memo)  
    return memo[n]

print(feb(50,{}))
# 2d grid ..begin top left corner ..goal to travel bottom right corner 
# only move down or right .. how many ways can travel
"""
if (1,1) grid so you are already there so 1 answer 
if (0,1) then 0 : invalid 
if (1,0) then 0 ....
now recursive 
if we have gridTraveler(3,3) lets move down
now gridTraveler(2,3) lets move right
gridTraveler (2,2) then down
gridTraveler(1,2) then right
gridTravler(1,1) destination 
m, n are size of grid m*n
"""
#O(2^n+m) time .. O(n+m) space

def gridTraveler(m,n):
    if m==1 and n==1 :
        return 1
    if m==0 or n==0:
        return 0
    #down reduce row that is m  and right reduce n 
    return gridTraveler(m-1,n)+gridTraveler(m,n-1)
    
#memoization
#(1,2) should be same (2,1)
# O(m*n)
def gridTraveler(m,n,memo):
    key= tuple([m,n])
    if key in memo:
        return memo[key]
    if m==1 and n==1 :
        return 1
    if m==0 or n==0:
        return 0
    #down reduce row that is m  and right reduce n 
    memo[key]= gridTraveler(m-1,n,memo)+gridTraveler(m,n-1,memo)
    return memo[key]

print(gridTraveler(4,4,{}))
      
# return boolen if target  will  sum of elements 
# O(n^m) n=len(numbers),m=target O(m)>>space
def canSum(targetSum,numbers):
    if targetSum==0:
        return True
    if targetSum<0:
        return False
    for n in numbers:
        diff=targetSum-n
        result=canSum(diff,numbers)
        if result:
            return True
    return False
# O(n*m)
def canSum(targetSum,numbers,memo):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum==0:
        return True
    if targetSum<0:
        return False
    for n in numbers:
        diff=targetSum-n
        result=canSum(diff,numbers,memo)
        if result:
            memo[targetSum]=True
            return True
    memo[targetSum]=False    
    return False

#print(canSum(7,[2,4,3,7]))    
#print(canSum(7,[2,4,4,8]))    
# return one possibile combination else null
# recurisve tree ... when target zero then [] then append other node
def howSum(targetSum,numbers):
    if targetSum==0:
        return []
    if targetSum<0:
        return None
    for n in numbers:
        diff=targetSum-n
        result=howSum(diff,numbers)
        if result!=None:
            return result+ [n]
    return None   

def howSum(targetSum,numbers,memo):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum==0:
        return []
    if targetSum<0:
        return None
    for n in numbers:
        diff=targetSum-n
        result=howSum(diff,numbers,memo)
        
        if result!=None:
            new_a=result+ [n]
            memo[diff]=new_a
            return new_a
    memo[targetSum]=None    
    return None   

print(howSum(7,[2,4,3,7],{}))


#Tabulation
def gridTraveler(m,n):
    dp=[[ 0  for _ in range(n+1)] for _ in range(m+1)]
    dp[1][1]=1
    for i in range(m+1):
        for j in range(n+1):
            if i+1<=m:
                dp[i+1][j]+=dp[i][j]
            if j+1<=n:
                dp[i][j+1]+=dp[i][j]
    return dp[m][n]                


print(gridTraveler(4,4))
