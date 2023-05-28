n = int(input())
p=[0]*10001
for i in range(1,n+1):
  p[i]=int(input())

d=[0]*10001
d[1]=p[1]
d[2]=p[1]+p[2]
for i in range(3,n+1):
  d[i]=max(d[i-1], d[i-2]+p[i], d[i-3]+p[i-1]+p[i])
print(d[n])