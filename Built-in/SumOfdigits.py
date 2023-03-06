# Built-in fn of python to calculate sum of digits 


t=int(input())
for i in range(t):
    n=int(input())
    ans=sum(map(int,str(2**n)))
    print(ans)

# 1        testcases
# 1000     2^1000
# 1366     sumOfdigits
