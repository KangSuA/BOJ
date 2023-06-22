N,M = map(int,input().split())

def rec(m,com):
  if m==M:
    print(com)
    return
  for i in range(int(com[-1]),N+1):
    if m==0:
      rec(m+1,str(i))
    else:
      rec(m+1,com+" "+str(i))
  return

rec(0,"1")