import sys
input = sys.stdin.readline
n,m = map(int,input().split())
str = []
lvl = []
for i in range(n):
  a,b = input().split()
  if len(lvl)!=0 and lvl[-1]==b: #같으면 처음 값만 저장.
    continue
  str.append(a)
  lvl.append(int(b))

def binary_search(target):
  start=0
  end=len(lvl)-1
  while start <= end:
    mid = (start+end)//2
    if target > lvl[mid]:
      start = mid + 1
    else:
      end = mid - 1
  print(str[end+1])

for i in range(m):
  target = int(input())
  binary_search(target)