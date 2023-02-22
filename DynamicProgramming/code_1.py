######################## Dynamic Programming-1 ##############################

########################    Climbing Stairs  ##############################

def waysclimbingstairs(n):      #with 1 or 2 sized steps
    dp=[0 for i in range(n+1)]
    dp[0]=0
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]

    return dp[n]

print(waysclimbingstairs(5))

########################    Min Cost Climbing Stairs  ######################

def mincost(arr):   #with 1 or 2 sized steps
    n=len(arr)
    dp=[0 for i in range(n+2)]
    dp[0]=0
    dp[1]=arr[0]
    dp[2]=min(arr[0]+arr[1],arr[1]) 
    for i in range (3,n+1):
        dp[i]=min(dp[i-1],dp[i-2])+arr[i-1]

    return min(dp[n],dp[n-1])

print(mincost([10,15,20]))

########################  House Robber    ################################

def maximumrobb(arr): #cant rob 2 houses in a row
    n=len(arr)
    if n==1:
         return arr[0]
    dp=[0 for i in range(n)]
    dp[0]=arr[0]
    dp[1]=max(arr[0],arr[1])
    for i in range(2,n):
            dp[i]=max(dp[i-2]+arr[i],dp[i-1])

    return dp[n-1]

print(maximumrobb([1,2,3,1]))

########################  Circled House Robber    ################################

def maximumcirclerobb(arr): 
    n=len(arr)
    if n==1:
        return arr[0]
    return max(maximumrobb(arr[1:]),maximumrobb(arr[:-1]))
    
    
print(maximumcirclerobb([2,3,2,6,10]))


###########################   Coin change    #####################################     

def minimumcoins(arr,k):
    dp=[k+1 for i in range(k+1)]
    dp[0]=0 
    for i in range(1,k+1):
         for coin in arr:
              if i-coin>=0:
                   dp[i]=min(dp[i],1+dp[i-coin])
    if dp[k]!=k+1:
         return dp[k]
    else:
         return -1

print(minimumcoins([186,419,83,408],6249))


###########################   Maximum Product Subarray    #############################

def maximumproduct(arr):    #continuous
    n=len(arr)
    if n==1:
         return arr[0]
    dp=[[0,0] for i in range(n)]
    dp[0][0]=arr[0]
    dp[0][1]=arr[0]
    for i in range(1,n):
            if arr[i]==0:
                 dp[i][1]=1
                 dp[i][0]=1
            else:
                dp[i][0]=min(dp[i-1][0]*arr[i],dp[i-1][1]*arr[i],arr[i])
                dp[i][1]=max(dp[i-1][0]*arr[i],dp[i-1][1]*arr[i],arr[i])


    print(dp)
    return max(dp[i][1] for i in range(n))

print(maximumproduct([2,3,-2,4]))



     
     
