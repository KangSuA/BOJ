from heapq import heappush, heappop
import sys
input = sys.stdin.readline
N = int(input())
h = []
for i in range(N):
  x = int(input())
  if x==0:
    if len(h)==0:
      print(0)
    else:
      print(heappop(h))
  else:
    heappush(h,x)