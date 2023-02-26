import sys
read = sys.stdin.readline

n = int(read())
dot = []
for i in range(n):
  dot.append(list(map(int,read().split())))

dot.sort(key=lambda s:(s[0],s[1]))
for i in dot:
  print(i[0],i[1])