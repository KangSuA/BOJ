import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
  K = int(input())
  file = list(map(int,input().split()))
  
  S = [0]*(K+1)
  for i in range(1,K+1):
    S[i] = S[i-1] + file[i-1]
  dp = [[0]*(K+1) for _ in range(K+1)]
  for i in range(2, K+1):
    for j in range(1, K+2-i):
      dp[j][j+i-1] = min(dp[j][j+k] + dp[j+k+1][j+i-1] for k in range(i-1)) + (S[j+i-1]- S[j-1])
  print(dp[1][K])