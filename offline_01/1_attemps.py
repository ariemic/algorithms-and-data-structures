def is_pali(s):
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True


def ceasar(s): #O(n^3)
    '''
    #1 bruteforce not optimal but works for every test
    zwraca długość najdłużego znalezionego palindromu w zadanym słowie
    '''
    maxi = 0
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            cnt = j-i+1 
            p = s[i:j+1]
            if  cnt > maxi and cnt%2 == 1 and is_pali(p):
                maxi = cnt
    return maxi

print(ceasar('akontnoknonabcddcba'))

            
def ceasar(s):
    maxi = 0
    n = len(s)
    for m in range(n):
        r = 1
        leng = 0
        while m - r >= 0 and m + r < n:
            if s[m-r] != s[m+r]:
                break
            print(s[m-r:m+r+1])
            leng = 2*r + 1
            r += 1 
        maxi = max(maxi, leng)
    return max(maxi, 1)


print(ceasar('akontnoknonabcddcba'))


def ceasar(s):
   pass


def ceasar(s):
    maxi = 0
    n = len(s)
    for m in range(n):
        r = 1
        leng = 0
        while m - r >= 0 and m + r < n:
            if s[m-r] != s[m+r]:
                break
            r += 1 
        leng = 2*(r-1) + 1
        maxi = max(maxi, leng)
    return max(maxi, 1)
