import sys
from heapq import heappush
input = sys.stdin.readline

N,C = map(int,input().split())

home = [int(input()) for _ in range(N)]
home.sort()

left = 1
right = home[-1]
res = 0
while left <= right:
  mid = (left + right) // 2
  cur = home[0]
  cnt = 1
  for i in range(1,N):
    if home[i] - cur >= mid:
      cnt += 1
      cur = home[i]
  if cnt >= C:
    res = mid
    left = mid + 1
  else:
    right = mid - 1
print(res)