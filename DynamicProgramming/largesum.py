def maximum_sum_path(arr,r,c):
    dp=[[0 for i in range(c)] for j in range(r)]

    dp[0][0]=arr[0][0]

    for i in range(1,c):
        dp[0][i]=arr[0][i]+dp[0][i-1]

    for j in range(1,r):
        dp[j][0]=arr[j][0]+dp[j-1][0]

    for i in range(1,r):
        for j in range(1,c):
            dp[i][j]=arr[i][j]+max(dp[i-1][j],dp[i][j-1])

    return dp[r-1][c-1]


arr=[
    [3,7,9,2,7],
    [9,8,3,5,5],
    [1,7,9,8,5],
    [3,8,6,4,10],
    [6,3,9,7,8]
]
print(maximum_sum_path(arr,5,5))