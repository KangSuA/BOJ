n = int(input())
dp=[0]*1000001
idx = [0]*1000001
dp[1]=0

for i in range(2,n+1):
  dp[i] = dp[i-1]+1
  idx[i] = i-1
  if(i%3==0):
    if(dp[i]>dp[i//3]+1):
      dp[i] = dp[i//3]+1
      idx[i] = i//3
  if(i%2==0):
    if(dp[i]>dp[i//2]+1):
      dp[i] = dp[i//2]+1
      idx[i] = i//2

print(dp[n])
print(n,end=" ")
while n!=1:
  print(idx[n],end=" ")
  n = idx[n]