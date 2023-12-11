import sys
from itertools import combinations
input = sys.stdin.readline

N,M = map(int,input().split())
home = []
store = []
res = 10e9
for i in range(N):
  oneline = list(map(int,input().split()))
  for j in range(N):
    if oneline[j]==1:
      home.append((i,j))
    elif oneline[j] == 2:
      store.append((i,j))

for s in combinations(store,M):
  temp = 0
  for h in home:
    chicken_len = 10e9
    for i in range(M):
      chicken_len = min(chicken_len,abs(h[0]-s[i][0])+abs(h[1]-s[i][1]))
    temp += chicken_len
  res = min(res,temp)
print(res)