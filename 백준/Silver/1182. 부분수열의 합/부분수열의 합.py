import sys
input = sys.stdin.readline

N,S = map(int,input().split())
num = list(map(int,input().split()))
num.sort()
res = 0

def sol(n,subl,st):
  global res
  for i in range(st,N):
    subl.append(num[i])
    if sum(subl) == S:
      res += 1
    sol(n+1,subl,i+1)
    subl.pop()
sol(0,[],0)
print(res)