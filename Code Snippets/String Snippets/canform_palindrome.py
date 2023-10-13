def canFormPalindrome(s):
    strvector = 0
    for str in s:
        strvector ^= 1 << ord(str)
    return strvector == 0 or strvector & (strvector - 1) == 0