import sys
from collections import deque
input = sys.stdin.readline

N,M,K = map(int,input().split())
fireball = deque()

for _ in range(M):
  temp = list(map(int,input().split()))
  temp[0] -= 1
  temp[1] -= 1
  fireball.append(temp)

dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,1,1,1,0,-1,-1,-1]

board = [[[]for i in range(N)] for j in range(N)]

for i in range(K):
  while fireball:
    f = fireball.popleft()
    r,c,m,s,d = f[0],f[1],f[2],f[3],f[4]
    #이동
    r = (r + dy[d]*s) % N
    c = (c + dx[d]*s) % N
    
    if not board[r][c]:
      board[r][c] = [m,s,d,1]
    else:
      board[r][c][0] += m
      board[r][c][1] += s
      board[r][c][3] += 1
      if board[r][c][2] == -1:
        continue
      elif board[r][c][2]%2 != d%2:
        board[r][c][2] = -1

  for r in range(N):
    for c in range(N):
      if not board[r][c]:
        continue
      if board[r][c][3] == 1:
        m = board[r][c][0]
        s = board[r][c][1]
        d = board[r][c][2]
        fireball.append([r,c,m,s,d])
      if board[r][c][3] >= 2:
        m = board[r][c][0]//5
        if m==0:
          board[r][c] = []
          continue
        s = board[r][c][1]//board[r][c][3]
        if board[r][c][2]==-1:
          for d in range(1,8,2):
            fireball.append([r,c,m,s,d])
        else:
          for d in range(0,7,2):
            fireball.append([r,c,m,s,d])
      board[r][c] = []

res = 0
while fireball:
  f = fireball.popleft()
  res += f[2]
print(res)