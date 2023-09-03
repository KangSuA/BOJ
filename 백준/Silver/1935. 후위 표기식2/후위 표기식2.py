import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
exp = deque(list(input().rstrip()))
num = [input().rstrip() for _ in range(N)]
op = "*+-/"

temp = []
while exp:
  comp = exp.popleft()
  if comp in op:
    b = temp.pop()
    a = temp.pop()
    res = eval(a+comp+b)
    temp.append(str(res))
  else:
    temp.append(num[ord(comp)-ord('A')])
res = float(temp[0])
print(f"{res:.2f}")