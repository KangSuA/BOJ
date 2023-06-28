import sys
input = sys.stdin.readline

L, C = map(int,input().split())
ch = list(input().split())
ch.sort()

def sol(n,password,st):
  if n==L:
    check = [i for i in password if i in 'aeiou']
    if 1<=len(check)<=L-2:
      print(''.join(password))
    return
  for i in range(st,C):
    sol(n+1,password+ch[i],i+1)
  return

sol(0,'',0)