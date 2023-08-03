import sys
from heapq import heappush, heappop
input = sys.stdin.readline

INF = int(1e9)
N, M, X = map(int,input().split())

graph = [[] for i in range(N+1)]
time = [[INF]*(N+1) for _ in range(N+1)]

for i in range(M):
  s, e, t = map(int,input().split())
  graph[s].append((e,t))
  
def dijkstra(s):
  q = []
  heappush(q,(0,s))
  time[s][s] = 0
  while q:
    dist, now = heappop(q)
    if time[s][now] < dist:
      if s!=X and now==X:
        return
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < time[s][i[0]]:
        time[s][i[0]] = cost
        heappush(q,(cost,i[0]))
for i in range(1,N+1):
  dijkstra(i)
res = [0]*(N+1)
for i in range(1, N+1):
  res[i] = time[X][i] + time[i][X]
print(max(res))