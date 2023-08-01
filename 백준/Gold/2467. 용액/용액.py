import sys
input = sys.stdin.readline

N = int(input())
liquid = list(map(int,input().split()))
liquid.sort()

lp = 0
rp = N-1
mn, mnl, mnr = 2000000001, 0, 0
while lp < rp:
  val = liquid[lp]+liquid[rp]
  if abs(val) < mn:
    mn = abs(val)
    mnl = lp
    mnr = rp
  if val < 0:
    lp += 1
  elif val > 0:
    rp -= 1
  else:
    break

print(liquid[mnl], liquid[mnr])