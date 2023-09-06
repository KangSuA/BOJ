import sys
input = sys.stdin.readline
INF = 10e9
V, E = map(int,input().split())
graph = [[INF]*(V+1) for i in range(V+1)]
for i in range(V+1):
  graph[i][i] = 0


for _ in range(E):
  a,b,c = map(int,input().split())
  graph[a][b] = c

for k in range(1,V+1):
  for a in range(1,V+1):
    for b in range(1,V+1):
      graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

res = INF
for a in range(1,V+1):
  for b in range(1,V+1):
    if a==b:
      continue
    res = min(res,graph[a][b]+graph[b][a])

if res==INF:
  print(-1)
else:
  print(res)