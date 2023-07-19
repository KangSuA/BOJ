import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
word = [input().rstrip() for _ in range(N)]
alph = defaultdict(int)
for w in word:
  lenw = len(w)
  for i in range(lenw):
    alph[w[i]] += 10**(lenw-i-1)
  
alph = sorted(alph.items(), key = lambda x: -x[1])
res = 0
num = 9
for a, n in alph:
  res += n*num
  num -= 1
print(res)