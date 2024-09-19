
from math import log10, floor

def leng(num):
    return floor(log10(num)+1)

print(leng(234))


def count_sort(array, p):
    #p - potęga 
    base = 10**p
    new_arr = [[]for _ in range(10)] #create buckets for digits
    for val in array:
        idx = (val // base)%10 #kilka przykładów: val = 1234, dla i=0 -> idx = 4, dla i=1 -> idx = 3
        new_arr[idx].append(val)
    i = 0
    for bucket in new_arr:
        for x in bucket:
            array[i] = x
            i += 1
    
def RaddixSort(array):
    max_val = max(array) #we need to find the biggest value to know the lenght of the biggest number
    max_leng = leng(max_val)
    for i in range(max_leng):
        count_sort(array, i)
        print(array)
    return array

T = [42, 96, 72, 1902, 45, 1, 23, 9032, 123]
print(RaddixSort(T))
