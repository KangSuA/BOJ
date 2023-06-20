import sys
input = sys.stdin.readline
N = int(input())

def hanoi(s, e, n):
  if n==1:
    print(s,e)
    return
  hanoi(s,6-s-e,n-1)
  print(s,e)
  hanoi(6-s-e,e,n-1)

print((1<<N)-1)
hanoi(1,3,N)