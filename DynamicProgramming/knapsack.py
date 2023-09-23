

def knapsack(arr,sum):
    """
    Finds whether a sum can be made using a subset
    of given array of weights
    """
    if sum<0:
        return False
    if sum==0:
        return True
    
    dp=[[0 for i in range(len(arr))]
                for j in range(sum+1)]

    dp[0][0]=1
    for i in range(1,len(arr)):
        dp[0][i]=1

    for i in range(1,sum+1):
        dp[i][0]=1

    for i in range(1,len(arr)):
        for j in range(1,sum+1):
            if j-arr[i]>=0:
                dp[j][i]=dp[j-arr[i]][i-1]|dp[j][i-1]

    print(dp)
    return max(dp[sum])

arr=[1,3,3,5]
print(knapsack(arr,12))
print(knapsack(arr,10))
print(knapsack(arr,2))

