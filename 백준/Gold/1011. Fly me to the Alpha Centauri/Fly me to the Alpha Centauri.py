import sys
from math import sqrt
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  x, y = map(int,input().split())
  dist = y-x
  n = int(sqrt(dist - 1))
  
  if n**2 < dist <= n**2 + n:
    print(2*n)
  else:
    print(2*n+1)