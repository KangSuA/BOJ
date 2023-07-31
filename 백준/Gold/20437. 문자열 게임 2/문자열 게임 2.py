import sys
from collections import defaultdict
input = sys.stdin.readline
T = int(input())
for _ in range(T):
  alp = defaultdict(list)
  
  W = list(input().rstrip())
  K = int(input())
  
  for i in range(len(W)):
    alp[W[i]].append(i)
  overk = list(filter(lambda x:(len(x[1])>=K),alp.items()))
  
  if not overk:
    print(-1)
    continue
    
  res = []
  for i in range(len(overk)):
    a, idx = overk[i]
    for j in range(K-1,len(idx)):
      res.append(idx[j]-idx[j-K+1])
  print(min(res)+1,max(res)+1)