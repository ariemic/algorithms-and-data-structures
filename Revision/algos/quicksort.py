def quicksort(A, l, r):
  if l < r:
    pivot = partition(A, l, r)
    quicksort(A, l, pivot - 1)
    quicksort(A, pivot+1, r)


def partition(A, l, r):
  x = A[r]
  i = l - 1
  for j in range(l, r):
    if A[j] <= x:
      i += 1
      A[i], A[j] = A[j], A[i]
  A[i+1], A[r] = A[r], A[i+1]
  return i + 1



T = [10, 7, 8, 9, 1, 5]
quicksort(T, 0, len(T) - 1)
print(T)
