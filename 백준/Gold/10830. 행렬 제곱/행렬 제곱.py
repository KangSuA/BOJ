import sys
input = sys.stdin.readline

def mul(a, b, N):
  newA = [[0]*N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      for k in range(N):
        newA[i][j] += a[i][k]*b[k][j]
      newA[i][j] %= 1000
  return newA

def power(a, n, N):
  if n == 1:
    return a
    
  x = power(a, n//2, N)
  xx = mul(x,x,N)
  if n % 2 == 0:
    return xx
  else:
    return mul(xx,a,N)

N, B = map(int,input().split())

A = [list(map(int,input().split())) for _ in range(N)]

res = power(A,B,N)
for i in range(N):
  for j in range(N):
    print(res[i][j]%1000,end=" ")
  print()