import itertools
import sys
input = sys.stdin.readline

def binary_search(target,start,end):
  while start <= end:
    mid = (start+end)//2
    if arr[mid] == target:
      return mid
    elif arr[mid] > target:
      end = mid -1
    else:
      start = mid +1
  return 'F'

n = int(input())
arr = list(map(int,input().split()))
arr.sort()
good = 0
nCr = itertools.combinations(arr,2)
for i in nCr:
  a,b = i
  c = a+b
  g = 0
  while True:
    bs = binary_search(c,0,len(arr)-1)
    if bs=='F':
      break
    arr.pop(bs)
    g+=1
  if (a==0 or b==0) and a!=b and g==1:
    arr.append(c)
    arr.sort()
  elif a==b==0 and g==2:
    arr.append(0)
    arr.append(0)
    arr.sort()
  else:
    good+=g
print(good)