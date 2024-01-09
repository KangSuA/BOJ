import sys
from collections import deque
input = sys.stdin.readline

def bfs(q):
  cnt = 0
  while q:
    z,x,y,cnt = q.popleft()
    for dz,dx,dy in dxyz:
      nz = z + dz
      nx = x + dx
      ny = y + dy
      if 0<=nz<H and 0<=nx<N and 0<=ny<M and graph[nz][nx][ny]==0:
        graph[nz][nx][ny] = 1
        q.append((nz,nx,ny,cnt+1))
  return cnt

M, N, H = map(int,input().split())
graph = [[[0]*M for _ in range(N)]for _ in range(H)]
for i in range(H):
  for j in range(N):
    graph[i][j] = list(map(int,input().split()))
    
dxyz = [(0,-1,0),(0,1,0),(0,0,-1),(0,0,1),(1,0,0),(-1,0,0)] #앞뒤왼오상하
res = 0

q = deque()
for i in range(H):
  for j in range(N):
    for k in range(M):
      if graph[i][j][k]==1:
        q.append((i,j,k,0))
res = bfs(q)
for i in range(H):
  for j in range(N):
    for k in range(M):
      if graph[i][j][k]==0:
        print(-1)
        exit(0)
print(res)