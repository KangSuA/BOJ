import sys
input = sys.stdin.readline

str1 = list(input().rstrip())
str2 = list(input().rstrip())

if len(str1) > len(str2):
  str1, str2 = str2, str1

graph = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]
res = 0

for i,s in enumerate(str1):
  for j,l in enumerate(str2):
    if s==l:
      graph[i+1][j+1] = graph[i][j] + 1
      res = max(res,graph[i+1][j+1])
print(res)