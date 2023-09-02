import sys
from heapq import heappop,heappush
input = sys.stdin.readline

def bfs(start):
    visited = [10e9]*(n+1)
    resc, rest = 0, 0
    q = []
    heappush(q,(0,start))
    visited[start] = 0
    while q:
      time, num = heappop(q)
      if visited[num] < time:
        continue
      for nt, nn in graph[num]:
        if visited[nn] > time + nt:
          visited[nn] = time + nt
          heappush(q,(time+nt,nn))
    for v in visited:
      if v != 10e9:
        resc += 1
        if rest < v:
          rest = v
    return [resc,rest]

T = int(input())
for _ in range(T):
  n,d,c = map(int,input().split())
  graph =[[] for _ in range(n+1)]
  for i in range(d):
    a,b,s = map(int,input().split())
    graph[b].append((s,a))
  print(*bfs(c))
