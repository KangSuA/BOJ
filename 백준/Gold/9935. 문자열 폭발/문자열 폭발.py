import sys
input = sys.stdin.readline

org = list(input().rstrip())
bomb = list(input().rstrip())
stck = []
idx = 0
lenb = len(bomb)
for w in org:
  stck.append(w)
  if len(stck)>=lenb:
    if stck[-lenb:] == bomb:
      for i in range(lenb):
        stck.pop()
if stck:
  print(''.join(stck))
else:
  print("FRULA")