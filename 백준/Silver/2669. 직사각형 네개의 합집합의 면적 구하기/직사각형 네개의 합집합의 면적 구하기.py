import sys
input = sys.stdin.readline

rect = [list(map(int,input().split())) for _ in range(4)]
graph = [[0]*100 for _ in range(100)]

for i in range(4):
  x1, y1, x2, y2 = rect[i]
  for r in range(y1,y2):
    for c in range(x1,x2):
      graph[r][c] = 1

print(sum([sum(graph[r]) for r in range(100)]))