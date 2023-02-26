import sys
read = sys.stdin.readline
s = list(read().rstrip())
res = []
for i in range(len(s)):
  res.append(''.join(s[i:len(s)]))
res.sort()
for i in res: print(i)