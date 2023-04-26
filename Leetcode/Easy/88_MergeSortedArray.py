def merge(nums1, nums2, m, n):
    #m - ilosc ele nums1, n - len(nums2); len(nums1) = n+m 
    #uzupełniam tablice nums1 od końca żeby zasepując zera największą z wartości z tablicy nums1 lub nums2
    if m == 0: 
        for i in range(n):
            nums1[i] = nums2[i]
    else:
        i, j = m-1, n-1
        k = m+n-1 #isert array from the end
        while j > -1:
            if nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k], nums1[i] = nums1[i], (-1)*10**9-1
                if i != 0:
                    i -= 1
            k -= 1

nums1 = [0]
m = 0 
nums2 = [1] 
n = 1
num23 = merge(nums1, nums2, m, n)
print(num23)
