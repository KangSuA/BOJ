import sys
read = sys.stdin.readline

def binary_search(arr,t):
  start = 0
  end = len(arr)-1
  while start <= end:
    mid = (start+end)//2
    if arr[mid]==t:
      return 1
    elif arr[mid] > t:
      end = mid - 1
    else:
      start = mid + 1
  return 0

n = int(read().rstrip())
card = list(map(int,read().split()))
m = int(read().rstrip())
num = list(map(int,read().split()))
card.sort()
for i in num:
  print(binary_search(card,i),end=' ')