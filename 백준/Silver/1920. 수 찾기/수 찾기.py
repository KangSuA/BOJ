import sys
read = sys.stdin.readline

n = int(read().rstrip())
array = list(map(int, read().split()))
m = int(read().rstrip())
s = list(map(int, read().split()))

def binary_search(target):
  start = 0
  end = n-1
  while start<=end:
    mid = (start + end)//2
    if array[mid] == target:
      return 1
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return 0
array.sort()
for i in s:
  print(binary_search(i))