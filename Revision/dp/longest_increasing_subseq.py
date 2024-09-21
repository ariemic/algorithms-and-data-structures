""" 
1. f(k) - dl najdłuższego podciągu kończącego się na A[k]
2. f(k) = max {f(t) + 1 | t < k ^ A[t] < A[k]}
"""
def longest_not_coherent_subseq(A):
  n = len(A)
  F = [1]*n
  Parent = [-1]*n
  for k in range(1, n):
    # nie możemy A[k] porównywać tylko z A[k-1] bo nie wiemy ile wczesniej jest liczba mniejsza od A[k] a nie możemy jej (ich ) ominąć
    # co prawda jeśli dojdzemy do pierwszej mniejszej idąc od tyłu to F[t] juz nie bedzie pozniej wieksze wiec moglibysmy na tym skonczyc
    for t in range(k):
      if A[t] < A[k] and F[t] < F[k] + 1:
        F[k] = F[t] + 1
        Parent[k] = t
    # print_sol(A, Parent, k)
    # print("-----------------------------")
  return F[-1]



#czy ta wersja zawsze zadziała ? Nie mam pewności
def lis(A):
  n = len(A)
  F = [1]*n
  for k in range(n):
    for t in range(k, -1, -1):
      if A[t] < A[k] and F[k] < F[t] + 1:
        F[k] = F[t] + 1
        break
  return F[-1]
    

def print_sol(A, P, k):
  if P[k] != -1:
    print_sol(A, P, P[k])
  print(A[k])


A = [2, 1, 4, 3, 4, 8, 5, 7]
# A2 = [10, 22, 9, 33, 21, 50, 41, 60, 80]

print(longest_not_coherent_subseq(A))
# print(lis(A))