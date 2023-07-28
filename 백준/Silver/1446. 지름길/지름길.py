import sys
input = sys.stdin.readline

N, D = map(int,input().split())

dp = [0]
s,e,d = [],[],[]
for _ in range(N):
  start,end,dist = map(int,input().split())
  s.append(start)
  e.append(end)
  d.append(dist)

for i in range(1,D+1):
  dp.append(dp[i-1]+1)
  while i in e:
    idx = e.index(i)
    if dp[i] > dp[s[idx]] + d[idx]:
      dp[i] = dp[s[idx]]+d[idx]
    s.pop(idx)
    e.pop(idx)
    d.pop(idx)
print(dp[D])   