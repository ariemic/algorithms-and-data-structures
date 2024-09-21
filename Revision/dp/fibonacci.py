def fibo(n):
  F = [0]*(n+1)
  F[0] = 0
  F[1] = 1
  for i in range(2, n+1):
    F[i] = F[i-1] + F[i - 2]
  return F[n]


print(fibo(5))