import sys
from collections import deque
input = sys.stdin.readline

def rot(arr,dir):
  if dir==1:
    arr.appendleft(arr.pop())
  else:
    arr.append(arr.popleft())

one = deque(map(int,input().rstrip()))
two = deque(map(int,input().rstrip()))
three = deque(map(int,input().rstrip()))
four = deque(map(int,input().rstrip()))
K = int(input())
for _ in range(K):
  no, dir = map(int,input().split())
  diff = [one[2]!=two[6],two[2]!=three[6],three[2]!=four[6]]
  if no==1:
    rot(one,dir)
    if diff[0]:
      rot(two,dir*(-1))
      if diff[1]:
        rot(three,dir)
        if diff[2]:
          rot(four,dir*(-1))
  if no==2:
    rot(two,dir)
    if diff[0]:
      rot(one,dir*(-1))
    if diff[1]:
      rot(three,dir*(-1))
      if diff[2]:
        rot(four,dir)
  if no==3:
    rot(three,dir)
    if diff[1]:
      rot(two,dir*(-1))
      if diff[0]:
        rot(one,dir)
    if diff[2]:
      rot(four,dir*(-1))
  if no==4:
    rot(four,dir)
    if diff[2]:
      rot(three,dir*(-1))
      if diff[1]:
        rot(two,dir)
        if diff[0]:
          rot(one,dir*(-1))
print(one[0]+two[0]*2+three[0]*4+four[0]*8)