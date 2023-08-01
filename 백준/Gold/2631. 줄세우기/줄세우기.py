import sys
input = sys.stdin.readline

N = int(input())
line = [int(input()) for _ in range(N)]
dp = [0] * N
for i in range(N):
  for j in range(i):
    if line[i] > line[j]:
      dp[i] = max(dp[i],dp[j])
  dp[i] += 1

print(N - max(dp))