import sys
read = sys.stdin.readline

d=[[0]*15 for _ in range(15)]
d[0]=[i*(i+1)//2 for i in range(15)]

for a in range(1,15):
  for b in range(1,15):
    for c in range(1,b+1):
      d[a][b]+=d[a-1][c]

T=int(read().rstrip())
for i in range(T):
  k=int(read().rstrip()) #층
  n=int(read().rstrip()) #호
  print(d[k-1][n])