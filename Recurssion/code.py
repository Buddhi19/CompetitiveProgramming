############################### RECURSION  #####################################

#############################  LINE ############################################

def getmyposition(n):
    if n==1:
        return 1
    return 1+getmyposition(n-1)

############################# REVERSE A STRING ##################################

def reversestring(s):
    if len(s)==1:
        return s[0]
    return reversestring(s[1:])+s[0]

print(reversestring("hello"))

############################ PALINDROME ##########################################

def ispalindrome(s):
    if len(s)==0 or len(s)==1:
        return True
    if s[0]==s[len(s)-1]:
        return ispalindrome(s[1:len(s)-1])
    return False

print(ispalindrome("KAYAK"))
print(ispalindrome("1001001"))
print(ispalindrome("NEWN"))

########################   Palindromic Substrings   ################################

def palindromsubstringcount(arr,i,count):
    if i==len(arr):
        return count
    for j in range(len(arr)):
        if i-j<0 or i+j+1>len(arr):
            break
        if arr[i-j]==arr[i+j]:
            count+=1
        if arr[i-j]!=arr[i+j]:
            break
    for k in range(len(arr)):
        if i-k<0 or i+k+2>len(arr):
            break
        if arr[i-k]==arr[i+k+1]:
            count+=1
        if arr[i-k]!=arr[i+k+1]:
            break
    return palindromsubstringcount(arr,i+1,count)

s="aaab"
arr=list(s)
print(palindromsubstringcount(arr,0,0))
     

######################################### DECIMAL TO BIANRY #######################

def decimaltobinary(n,result):
    result=str(n%2)+str(result)
    if n==0:
        return result
    return decimaltobinary(n//2,result)

print(decimaltobinary(10,""))
print(decimaltobinary(110,""))

###################################### SUM OF NATURAL NUMBERS #######################

def sumnumber(n):
    if n==0:
        return 0
    return n + sumnumber(n-1)

print(sumnumber(10))

#############################################   divide and conquer  ##################################################

##############################################  binary search  #######################################################

def binarysearch_position(arr,k):
    if len(arr)==1:
        if arr[0]>=k:
            return 0
        return 1
    if len(arr)==0:
        return 1
    mid = len(arr)//2 
    if arr[mid]<k:
        return mid + binarysearch_position(arr[mid:],k)
    return binarysearch_position(arr[:mid],k)

print(binarysearch_position([1,2,3],4))
print(binarysearch_position([1,2,6,8,13,43,50],7))

##################################### Fibonacci (RECURSION) ##############################################################

def fibonacci(n):
    if n==1 or n==0:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(7))
print(fibonacci(20))

####################################    Climbing Stairs    ######################################################

def waysclimbingstairs(n):      #with 1 or 2 sized steps
    if n==0:
        return 0
    if n==2:
        return 2
    if n==1:
        return 1
    return waysclimbingstairs(n-1) + waysclimbingstairs(n-2)

print(waysclimbingstairs(5))

###########################   Coin change    #####################################     

def minimumcoins(arr,k,solution,coins):
     n=len(arr)
     if k==0:
          return 0
     list2=[]
     for i in range(n):
          for j in range(len(solution)):
               list2.append(solution[j]+arr[i])
     if k in list2:
          return coins+1
     if min(list2)>k:
          return -1
     solution=list2
     coins+=1
     return minimumcoins(arr,k,solution,coins)

print(minimumcoins([1,2,5],11,[0],0))


############################## Recursive KnapSack ######################################

def knapsack(i,weights,value,CurrentCapacity):
    if i<0 or CurrentCapacity<0:
        return 0
    if weights[i]>CurrentCapacity:
        return knapsack(i-1,weights,value,CurrentCapacity)

    else:
        result1=knapsack(i-1,weights,value,CurrentCapacity)
        result2=value[i]+knapsack(i-1,weights,value,CurrentCapacity-weights[i])
        return max(result1,result2)
    
weights=[1,2,4,2,5]
value=[5,3,5,3,2]
print(knapsack(len(weights)-1,weights,value,10))




    

    

