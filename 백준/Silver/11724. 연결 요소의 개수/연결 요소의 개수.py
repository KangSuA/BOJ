import sys
from collections import deque
#inpt = sys.stdin.readline().rstrip()

MAX = 1000
n,m = map(int, (sys.stdin.readline().rstrip()).split())
graph = [[0] for _ in range(n+1)]
for i in range(m):
  a,b = map(int,(sys.stdin.readline().rstrip()).split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(s):
  q = deque()
  q.append(s)
  visited[s]=1
  while q:
    v = q.popleft()
    for i in graph[v]:
      if visited[i]==0:
        q.append(i)
        visited[i] = 1

visited = [0]*(n+1)
res = 0
for i in range(1,n+1):
  if visited[i]==0:
    bfs(i)
    #print(i)
    res+=1
print(res)