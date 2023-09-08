import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def find(x):
  if parent[x]!=x:
    parent[x] = find(parent[x])
  return parent[x]

def union(a,b):
  a = find(a)
  b = find(b)
  if a==b:
    return False
  if a>b:
    parent[b] = a
  else:
    parent[a] = b
  return True

N,M = map(int,input().split())
parent = [i for i in range(N+1)]

hq = []
for _ in range(M):
  a,b,c = map(int,input().split())
  heappush(hq,(c,a,b))
  
res = 0
cnt = 0
if N==2:
  print(0)
  exit(0)
while hq:
  c,a,b = heappop(hq)
  if union(a,b):
    res += c
    cnt += 1
  if cnt==N-2:
    print(res)
    break