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




    

    

