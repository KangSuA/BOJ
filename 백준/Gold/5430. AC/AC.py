import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  op = list(input().rstrip())
  n = int(input())
  arr = (input().replace("[","").replace("]","").replace(","," "))
  arr = deque(arr.split())
  res = ""
  flag = 0
  for o in op:
    if o=="R":
      flag ^= 1
    if o=="D":
      if arr:
        if not flag:
          arr.popleft()
        if flag:
          arr.pop()
      else:
        res = "error"
        break
  if not res:
    if flag:
      arr.reverse()
    res = "["+",".join(arr)+"]"
  print(res)