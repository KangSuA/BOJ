import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
board = []
for i in range(N):
  board.append(list(map(int,input().rstrip())))

visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

dx = [0,0,1,-1]
dy = [-1,1,0,0]

def bfs():
  q = deque()
  q.append((0,0,0))
  visited[0][0][0] = 1
  
  while q:
    y, x, z = q.popleft()
    
    if y == N-1 and x == M-1:
      return visited[y][x][z]
      
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if 0<=ny<N and 0<=nx<M:
        if not z and board[ny][nx]:
          q.append((ny,nx,1))
          visited[ny][nx][1] = visited[y][x][0] + 1
        elif not board[ny][nx] and visited[ny][nx][z] == 0:
          q.append((ny,nx,z))
          visited[ny][nx][z] = visited[y][x][z] + 1
  return -1

print(bfs())