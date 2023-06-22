N,M = map(int,input().split())

visited = [False for _ in range(N+1)]
def rec(m,com):
  if m==M:
    print(com)
    return
  for i in range(int(com[-1]),N+1):
    if not visited[i]:
      visited[i] = True
      if m==0:
        rec(m+1,str(i))
      else:
        rec(m+1,com+" "+str(i))
      visited[i] = False
  return

rec(0,"1")