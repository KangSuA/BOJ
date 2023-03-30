import sys
input = sys.stdin.readline
n,m = map(int,input().split())
word = {}
for i in range(n):
  w = input().rstrip()
  if len(w)<m:
    continue
  if w not in word:
    word[w] = 1
  else:
    word[w] += 1
res = dict(sorted(sorted(sorted(word.items()), key=lambda x:len(x[0]),reverse=True), key=lambda x:x[1],reverse=True)).keys()
for i in res:
  print(i)
