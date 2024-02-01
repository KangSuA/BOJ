import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input())
hq = [] #제일 빨리 끝나는 순
lec = []
for i in range(N):
  s,t = map(int,input().split())
  lec.append((s,t))
lec.sort()
heappush(hq,lec[0][1])
for i in range(1,N):
  s,t = lec[i]
  if hq[0] <= s:
    heappop(hq)
    heappush(hq,t)
  else:
    heappush(hq,t)
print(len(hq))