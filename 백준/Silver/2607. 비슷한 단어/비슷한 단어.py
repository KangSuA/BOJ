import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
alp = [[0]*26 for _ in range(n)]
for i in range(n):
  word = list(input().rstrip())
  for w in word:
    alp[i][ord(w)-ord('A')] += 1

res = 0
for i in range(1,n):
  cnt = defaultdict(int)
  for j in range(26):
    diff = alp[0][j] - alp[i][j]
    cnt[diff] += 1
  if cnt[0] == 26:
    res += 1
  elif cnt[0] == 25:
    if cnt[1]==1 or cnt[-1]==1:
      res += 1
  elif cnt[0] == 24:
    if cnt[1]==1 and cnt[-1]==1:
      res += 1
print(res)