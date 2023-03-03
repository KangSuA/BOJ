import sys
read = sys.stdin.readline

n = int(read().rstrip())
a = list(map(int,read().split()))
d=[0 for _ in range(n)]
for i in range(n):
  for j in range(i):
    if a[i]>a[j] and d[i]<d[j]:
      d[i]=d[j]
  d[i]+=1
print(max(d))