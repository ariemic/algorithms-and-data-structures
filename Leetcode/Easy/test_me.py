def mySqrt(x):
    #return square root of x, round down to integer, using binary search.
    left, right = 0, 46340
    if x == 0: return 0
    while left <= right:
        mid = (right+left)//2
        res = mid*mid
        if x == res: return mid
        elif x < res:
            right = mid - 1
        else: left = mid+1
print(mySqrt(1))