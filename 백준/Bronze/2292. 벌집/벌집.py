N = int(input())

lvl = 1
inc = 1
while True:
  if N<=inc:
    break
  inc += 6*lvl
  lvl += 1

print(lvl)