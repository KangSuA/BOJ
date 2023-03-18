H,W,N,M = map(int,input().split())
res1,res2=0,0
res1 += H//(N+1)
if H%(N+1)!=0:
  res1 += 1
res2 += W//(M+1)
if W%(M+1)!=0:
  res2 += 1
print(res1*res2)