import sys
read = sys.stdin.readline

n=int(read().rstrip())
arr=list(map(int,read().split()))

d=[arr[0]]
for i in range(1,n):
  d.append(max(d[i-1]+arr[i],arr[i]))
print(max(d))