import sys
input = sys.stdin.readline

N, K = map(int,input().split())
medal = []
for i in range(N):
  country = list(map(int,input().split()))
  medal.append(country)
medal.sort(key = lambda x:(-x[1],-x[2],-x[3]))

km = []
for i in range(N):
  if medal[i][0]==K:
    km = medal[i][1:4]
    break
    
rank = 0
for i in range(N):
  rank+=1
  if medal[i][1:4]==km:
    break
print(rank)