
def partition(A, l, r):
  x = A[r]
  i = l - 1
  for j in range(l, r):
    if A[j] <= x:
      i += 1
      A[i], A[j] = A[j], A[i]
  A[i+1], A[r] = A[r], A[i+1]
  return i + 1

#* it finds k-th smallest element in the array 
#* f.e. I want to fine 2-nd smallest element in this array

def select(A, l, r, k):
  if l == r: return A[l]
  pivot = partition(A, l, r)
  # if pivot is same index and the k-th smallest element we are looking for then return its value
  if pivot == k: return A[pivot] 
  elif k < pivot: return select(A, l, pivot - 1, k)
  else: return select(A, pivot + 1, r, k)




T = [10, 7, 8, 9, 1, 5]
first = select(T, 0, len(T)-1, 0)
second = select(T, 0, len(T)-1, 1)
print(first, second)

