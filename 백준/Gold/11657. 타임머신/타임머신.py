import sys
input = sys.stdin.readline
INF = int(1e9)

N,M = map(int,input().split())
edges = []
dist = [INF] * (N+1)

for i in range(M):
  a,b,c = map(int,input().split())
  edges.append((a,b,c))

def bf(start):
  dist[start] = 0
  for i in range(N):
    for j in range(M):
      cur = edges[j][0]
      next_node = edges[j][1]
      cost = edges[j][2]
      if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
        dist[next_node] = dist[cur] + cost
        if i == N-1:
          return True
  return False

negative_cycle = bf(1)

if negative_cycle:
  print("-1")
else:
  for i in range(2,N+1):
    if dist[i] == INF:
      print("-1")
    else:
      print(dist[i])