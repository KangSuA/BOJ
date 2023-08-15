import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = []
tree = [[deque() for _ in range(N)] for i in range(N)]
soil = [[5]*N for i in range(N)]
res = M
for i in range(N):
  A.append(list(map(int,input().split())))

for i in range(M):
  x,y,z = map(int,input().split())
  tree[x-1][y-1].append(z)
  
def year():
  global res
  temp = []
  for r in range(N):
    for c in range(N):
      #spring
      if tree[r][c]:
        trees = len(tree[r][c])
        for t in range(len(tree[r][c])):
          if soil[r][c] - tree[r][c][t] >= 0:
            soil[r][c] -= tree[r][c][t]
            tree[r][c][t] += 1
            if tree[r][c][t]%5==0:
              temp.append([r,c])
          else:
            #summer
            res -= trees-t
            for i in range(trees-t):
              soil[r][c] += tree[r][c].pop()//2
            break
  #fall
  dr = [-1,-1,-1,0,0,1,1,1]
  dc = [-1,0,1,-1,1,-1,0,1]
  while temp:
    r,c = temp.pop()
    for i in range(8):
      nr = r + dr[i]
      nc = c + dc[i]
      if 0<=nr<N and 0<=nc<N:
        tree[nr][nc].appendleft(1)
        res += 1
  for r in range(N):
    for c in range(N):
      #winter
      soil[r][c] += A[r][c]
for _ in range(K):
  year()
  
print(res)