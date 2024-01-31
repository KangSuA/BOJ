import sys
from collections import defaultdict
input = sys.stdin.readline

for _ in range(int(input())):
  N = int(input())
  note1 = list(map(int,input().split()))
  M = int(input())
  note2 = list(map(int,input().split()))
  
  dic = defaultdict(list)
  
  for n in note1:
    dic[n] = 1
  
  for m in note2:
    if dic[m]:
      print(1)
    else:
      print(0)