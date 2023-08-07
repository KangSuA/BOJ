N = int(input())
cur = list(map(int,input()))
target = list(map(int,input()))

def click(cur,target):
  copy = cur[:]
  press = 0
  for i in range(1,N):
    if copy[i-1] == target[i-1]:
      continue
    press += 1
    for j in range(i-1, i+2):
      if j<N:
        copy[j] = 1 - copy[j]
  if copy == target:
    return press
  else:
    return 1e9

f_nc = click(cur,target)
cur[0] = 1 - cur[0]
cur[1] = 1 - cur[1]
f_c = click(cur,target) + 1
res = min(f_nc,f_c)
print(-1 if res == 1e9 else res)