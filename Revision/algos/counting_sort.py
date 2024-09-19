def counting_sort(A, k):
  n = len(A)
  B = [None]*n
  C = [0]*k
  for x in A: C[x] += 1
  