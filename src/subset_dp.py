"""
subset sum problem:
knapsack : ignore or taken

"""
def subset_sum(arr,sum,n,dp):
    #i  mean arr size
    #j means sum
    for i in range(n+1):
        for j in range(sum+1):
            # if i==0 and j==0:
            #     dp[i][j]=True # initialize
            if arr[i-1]<=j:
              dp[i][j]= dp[i-1][j-arr[i-1]] or dp[i-1][j]  # initialize
            else:
                dp[i][j]=   dp[i-1][j]
    return dp[n][sum] #answer will be last corner


"""
equal sum partition problem:
divide array and each subset should have same sum
return True if valid else false 
"""
def subset_partition_sum(arr,n):
    total_sum=sum(arr)
    sum_half=total_sum//2
    dp=[[False for _ in range(sum_half+1)] for _ in range(n+1)]
    # initialize: Base case of recursive
    for i in range(n+1):
        for j in range(sum_half+1):
            if i==0:
                dp[i][j]=False
            if j==0:
                dp[i][j]=True
    if total_sum %2 !=0:
        return  False
    else:
        return  subset_sum(arr,sum_half,n,dp)


def subsets_count(arr,sum,n,dp):

    for i in range(1,n+1):
        for j in range(sum+1):
            if arr[i-1]<=j:
                dp[i][j]=dp[i-1][j-arr[i-1]] + dp[i-1][j] # plus + instead of or
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][sum]



def main():
    arr=[2,3,5,6,8,10]
    sum=10
    n=len(arr)
    dp=[[False for _ in range(sum+1)] for _ in range(n+1)]
    # initialize: Base case of recursive
    for i in range(n+1):
        for j in range(sum+1):
            if i==0:
                dp[i][j]=False # if we have size zero of array but we have some sum that means False not valid
            if j==0:
                dp[i][j]=True #if you have size of array but sum is 0 so at that time empty subset so True
    print(subset_sum(arr,sum,n,dp))
    print(subset_partition_sum(arr,n))


    dp_1=[[0 for _ in range(sum+1)] for _ in range(n+1)]
    # initialize: Base case of recursive
    for i in range(n+1):
        for j in range(sum+1):
            if i==0:
                dp_1[i][j]=0 # if we have size zero of array but we have some sum that means 0 not valid
            if j==0:
                dp_1[i][j]=1 #if you have size of array but sum is 0 so at that time empty subset so 1
    print(subsets_count(arr,sum,n,dp_1))
if __name__=="__main__":
    main()