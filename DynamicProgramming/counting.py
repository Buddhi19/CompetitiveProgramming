
def counting_ways(arr,sum):
    n=len(arr)
    if sum==0:
        return 0
    dp=[0 for i in range(sum+1)]
    dp[0]=1
    for i in range(1,sum+1):
        for j in range(n):
            if i-arr[j]>=0:
                dp[i]+=dp[i-arr[j]]
    print(dp)
    return dp[sum]


arr=[1,3,4]
print(counting_ways(arr,5))