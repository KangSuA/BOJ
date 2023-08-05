import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(a,b,c):
  q = deque()
  q.append((a,b))
  visited[a][b] = True
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<N and 0<=ny<N:
        if graph[nx][ny] == c and not visited[nx][ny]:
          q.append((nx,ny))
          visited[nx][ny] = True

resn = 0
for i in range(N):
  for j in range(N):
    if not visited[i][j]:
      bfs(i,j,graph[i][j])
      resn += 1
resc = 0
for i in range(N):
  for j in range(N):
    if graph[i][j]=='G':
      graph[i][j]='R'

visited = [[False]*N for _ in range(N)]
for i in range(N):
  for j in range(N):
    if not visited[i][j]:
      bfs(i,j,graph[i][j])
      resc += 1   
print(resn,resc)