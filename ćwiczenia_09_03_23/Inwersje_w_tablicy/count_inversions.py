
class Solution(object):
    def isIdealPermutation(self, A):
        loc = sum([1 for i in range(len(A)-1) if A[i] > A[i+1]] or [0])
        glo = self.f(A,0,len(A) - 1)
        return loc == glo
    
    # count inversions while merge sorting
    def f(self,nums,i,j):
        if i >= j:
            return 0
        
        med = ( i + j ) >> 1
        count = self.f(nums,i,med) + self.f(nums,med + 1,j)
        
        ii = i
        for k in range(med + 1, j + 1):
            while(ii <= med and nums[ii] < nums[k]):
                ii += 1
            count += (med - ii + 1)
                
        nums[i:j + 1] = sorted(nums[i:j + 1])
        return count