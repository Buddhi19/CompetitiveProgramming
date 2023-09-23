
def longest_subs(arr):
    n=len(arr)
    dp=[1 for i in range(n)]

    for i in range(n):
        for j in range(i):
            if arr[j]<arr[i]:
                dp[i]=max(dp[i],dp[j]+1)

    return max(dp)

arr=[6,2,5,1,7,4,8,3]

print(longest_subs(arr))
