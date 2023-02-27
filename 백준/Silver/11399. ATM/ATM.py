import sys
n = int(input())
line = list(map(int,(sys.stdin.readline().split(' '))))

line.sort(reverse=True)
res=0
for i in range(n):
  res+= line[i]*(i+1)
print(res)