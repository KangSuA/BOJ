import sys
read = sys.stdin.readline
n = int(read().rstrip())
tri = []
for i in range(n):
  tri.append(list(map(int,read().split())))
  
d=[tri[0]]
for i in range(1,n):
  l=[]
  for j in range(len(tri[i])):
    if j==0:
      l.append(d[i-1][j]+tri[i][j])
    elif j==i:
      l.append(d[i-1][j-1]+tri[i][j])
    else:
      l.append(max(d[i-1][j-1],d[i-1][j])+tri[i][j])
  
  d.append(l)
print(max(d[n-1]))