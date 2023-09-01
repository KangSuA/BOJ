import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

if K==1:
  print(N)
  exit(0)

dp = [[0]*(N+1) for _ in range(N+1)]
dp[1][0] = 1
dp[1][1] = 1
for i in range(2,N+1):
  for j in range(1,N+1):
    if j==1:
      dp[i][j] = i
    elif i > j:
      dp[i][j] = dp[i-2][j-1] + dp[i-1][j]
print((dp[N-3][K-1]+dp[N-1][K])%1000000003)