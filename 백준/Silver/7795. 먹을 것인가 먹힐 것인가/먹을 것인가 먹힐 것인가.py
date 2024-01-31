import sys
input = sys.stdin.readline

def bs(B,start,end,target):
  res = -1
  while start <= end:
    mid = (start+end)//2
    if B[mid] < target:
      res = mid
      start = mid + 1
    else:
      end = mid - 1
  return res
for _ in range(int(input())):
  N, M = map(int,input().split())
  A = list(map(int,input().split()))
  B = list(map(int,input().split()))
  B.sort()
  
  res = 0
  for a in A:
    res += bs(B,0,M-1,a) + 1
  print(res)