import sys
from collections import deque

T = int(input())
for _ in range(T):
  line = list(map(int,input().split()))+[0]
  step = 0

  for i in range(2,21):
    for j in range(1,i):
      if line[i]<line[j]:
        step += i-j
        line = line[:j] + [line[i]] + line[j:i] + line[i+1:]
        break
  print(line[0],step)