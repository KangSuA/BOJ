import sys
input = sys.stdin.readline

def find(node):
  anscestor = []
  while True:
    anscestor.append(node)
    if graph[node]==0:
      break
    else:
      node = graph[node]
  return anscestor
  
T = int(input())
for _ in range(T):
  N = int(input())
  graph = [0]*(N+1)
  
  for i in range(N-1):
    a,b = map(int,input().split())
    graph[b] = a
    
  fn,sn = map(int,input().split())
  first = find(fn)
  second = find(sn)
  
  for i in range(1,min(len(first),len(second))+1):
    if first[-i]!=second[-i]:
      i -= 1
      break
  
  print(first[-i])