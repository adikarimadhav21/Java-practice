#knapsack
"""
fractional : fractional allow like 0.5
0-1: only full and one time allow
unbounded : multiple times allow for one
"""

# indentify DP: is it recursive (choice ?)? and is it have optimal solution ?

# storage + recursion =DP

"""
problem like we have weight and values ..  7 kg bucket so we need to put item with max profit
"""


#recursive solution
def knapsack(wt,values,cap,n ):
    if n==0 or cap==0:
        return 0
    if wt[n-1]<=cap: # two option we have include or ignore
        return max (values[n-1]+knapsack(wt,values,cap-wt[n-1],n-1),knapsack(wt,values,cap,n-1))
    else:
        return knapsack(wt,values,cap,n-1) # not include bcz size mismatched


 #memoization :
 # create dp matrix for chnages varibale here only cap and n changes for each recursion
def knapsack_dp(wt,values,cap,n ,dp):

    if n==0 or cap==0:
        return 0
    if dp[n][cap]!=-1: # if found  below recursion will not call return from here
        return dp[n][cap]
    if wt[n-1]<=cap: # two option we have include or ignore
        dp[n][cap] =max (values[n-1]+knapsack_dp(wt,values,cap-wt[n-1],n-1,dp),knapsack_dp(wt,values,cap,n-1,dp))
        return dp[n][cap]
    else:
        dp[n][cap] =knapsack_dp(wt,values,cap,n-1,dp) # not include bcz size mismatched
        return dp[n][cap]

"""
Top down approach : stack full hunna hunxa recursion badhi hudha so we need DP top down approach 
No stack overflow
recursive  convert to top down approach  (iterative)
create DP matrix 
initialize (base case) ...then iterative 

"""
def knapsack_dp_top_down(wt,values,cap,n ,dp):


    for i in range(0,n+1):
      for j in range(0,cap+1):
          if i==0 and j==0:
              dp[i][j]=0 #base case so 0 initialize this case
          elif wt[i-1]<=j:
              dp[i][j]=max(values[i-1]+dp[i-1][j-wt[i-1]],dp[i-1][j])
          else:
              dp[i][j]=dp[i-1][j]
    return  dp[n][cap]


def main():
    wt=[1,3,4,5]
    values=[1,5,7,10]
    cap=7
    size=len(wt)
    # create dp matrix for chnages varibale here only cap and n changes for each recursion
    dp=[[-1 for _ in range(cap+1)] for _ in range(size+1)]
    # for i in range(1,size+1):
    #     for j in range(1,cap+1):
    #         if i==0 and j==0:
    #             dp[i][j]=0
    print(knapsack(wt,values,cap,size))
    print(knapsack_dp(wt,values,cap,size,dp))
    print(knapsack_dp_top_down(wt,values,cap,size,dp))

if __name__=="__main__":
    main()