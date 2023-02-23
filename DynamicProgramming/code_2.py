#########################  Dynamic Programming 2 ############################

######################### Unique paths ###################################

def numberofpaths(m,n):  #can go right and down only
    if m==1 and n==1:
        return 1
    dp=[[0 for i in range(n)] for j in range(m)]
    dp[0][0]=1
    for i in range(1,n):
        dp[0][i]+=dp[0][i-1]
    for j in range(1,m):
        dp[j][0]+=dp[j-1][0]

    for i in range(1,m):
        for j in range(1,n):
            dp[i][j]+=dp[i-1][j]+dp[i][j-1]
    return dp[m-1][n-1]

print(numberofpaths(3,7))


############################## Longest Common Subsequence ####################

def lenlongestcommonsubsequence(s1,s2):
    dp=[[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]

    for i in range(len(s1)-1,-1,-1):
        for j in range(len(s2)-1,-1,-1):
            if s1[i]==s2[j]:
                dp[i][j]=1+dp[i+1][j+1]

            else:
                dp[i][j]=max(dp[i+1][j],dp[i][j+1])

    return dp[0][0]

print(lenlongestcommonsubsequence("abfde","ace"))


###########################  Best time to Buy and Sell Stock ####################

def maxProfit(arr):
    n=len(arr)
    if n==1:
        return max(0,-1*arr[0])
    
    #state: Buying or Selling
    #if buy-> i+1
    #if sell -> i+2

    dp={} #key=(i,buying) val=max_profit

    def dfs(i,buying):
        if i>=len(arr):
            return 0
        if (i,buying) in dp:
            return dp[(i,buying)]
        
        if buying:
            buy=dfs(i+1, not buying) - arr[i]
            cooldown=dfs(i+1,buying)
            dp[(i,buying)]=max(buy,cooldown)

        else:
            sell=dfs(i+2, not buying) + arr[i]
            cooldown=dfs(i+1,buying)
            dp[(i,buying)]=max(sell,cooldown)
        return dp[(i,buying)]
    return dfs(0,True)
    

print(maxProfit([1,2,4,0,1,2]))


############################  Coin Change 2 ##################################

def coinways(arr,k):
    if k==0:
        return 0
    dp=[0 for i in range(k+1)]
    dp[0]=0

    for coin in arr:
        for i in range(coin,k+1):
            if i-coin>=0:
                dp[i]+=dp[i-coin]
    return dp[k]


######################### Knapsack #######################################

def knapsack(weights,values,k):
    if k==0:
        return 0
    n=len(weights)

    dp=[[0 for i in range(k+1)] for j in range(n+1)]

    for i in range(n+1):
        for j in range(k+1):
            if i==0 and j==0:
                dp[i][j]=0
            elif weights[i-1]<=j:
                dp[i][j]=max(values[i-1]+dp[i-1][j-weights[i-1]],
                dp[i-1][j]
                )
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][k]

values = [60, 100, 120]
weights = [10, 20, 30]
k = 50

print(knapsack(weights,values,k))







    








