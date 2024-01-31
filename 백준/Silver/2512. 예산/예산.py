import sys
input = sys.stdin.readline

N = int(input())
budget = list(map(int,input().split()))
M = int(input())

start, end = 0, max(budget)

while start <= end:
  mid = (start+end)//2
  total = 0
  for i in budget:
    if i>=mid: #상한값보다 예산이 더 크면
      total += mid #상한값 까지만
    else:
      total += i
  if total > M:
    end = mid - 1
  else:
    start = mid + 1
print(end)