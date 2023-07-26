import sys
input = sys.stdin.readline

H,W = map(int,input().split())

block = list(map(int,input().split()))
rain = 0
for i in range(1,W-1):
  lmax = max(block[:i])
  rmax = max(block[i+1:])
  mn = min(lmax,rmax)

  if block[i] < mn:
    rain += mn - block[i]
print(rain)