import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = []
for i in range(N):
  graph.append(list(map(int,input().split())))
plan = list(map(int,input().split()))
visited = [False]*N
def bfs(start):
  q = deque()
  q.append(start)
  while q:
    v = q.popleft()
    visited[v] = True
    for city in [i for i in range(N) if graph[v][i]]:
      if not visited[city]:
        q.append(city)

bfs(plan[0]-1)
res = "YES"
for city in plan:
  if not visited[city-1]:
    res = "NO"
    break
print(res)