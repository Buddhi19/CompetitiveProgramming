
def Z_algo(s,z):
    n = len(s)
    L, R, k = 0,0,0
    for i in range(1,n):
        if i > R:
            L, R = i, i
            while R < n and s[R-L] == s[R]:
                R += 1
            z[i] = R-L
            R -= 1

        else:
            k=i-L
            if z[k] < R-i+1:
                z[i] = z[k]
            
            else:
                L=i
                while R < n and s[R-L] == s[R]:
                    R += 1
                z[i] = R-L
                R -= 1
    return z

def search(S1,S2):
    combined = S2+"|"+S1
    L = len(combined)

    z = [0 for i in range(L)]
    z = Z_algo(combined,z)

    ans=[]
    for i in range(L):
        if z[i] == len(S2):
            ans.append(i-len(S2)-1)

    return ans

