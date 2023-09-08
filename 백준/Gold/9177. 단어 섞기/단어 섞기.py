import sys
from collections import deque
input = sys.stdin.readline

def bfs():
  visited = [[False]*(len(w2)+1) for _ in range((len(w1))+1)]
  q = deque()
  q.append((0,0,0))
  while q:
    a,b,c = q.popleft()
    if a<len(w1) and w1[a]==w3[c] and not visited[a+1][b]:
      q.append((a+1,b,c+1))
      visited[a+1][b] = True
    if b<len(w2) and w2[b]==w3[c] and not visited[a][b+1]:
      q.append((a,b+1,c+1))
      visited[a][b+1] = True
  if len(w3)==c:
    return "yes"
  else:
    return "no"
n = int(input())
for i in range(n):
  w1, w2, w3 = input().rstrip().split()
  print(f"Data set {i+1}: {bfs()}")