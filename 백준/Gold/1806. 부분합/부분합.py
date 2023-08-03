import sys
input = sys.stdin.readline

N, S = map(int,input().split())
seq = list(map(int,input().split()))

res = 100002
subsum = 0
s = 0
e = 0
while e!=N:
  subsum += seq[e]
  if subsum >= S:
    while subsum - seq[s] >= S:
      subsum -= seq[s]
      s += 1
    res = min(res, e - s + 1)
  e += 1

print(0 if res==100002 else res)