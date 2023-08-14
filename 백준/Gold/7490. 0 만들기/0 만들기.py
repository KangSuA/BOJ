T = int(input())
for i in range(T):
  N = int(input())
  seq = [str(n) for n in range(1,N+1)]
  op = [' ']*(N-1)
  dop = [' ','+','-']
  
  def func(n):
    if n==N-1:
      temp = [seq[idx]+op[idx] for idx in range(N-1)]+[seq[N-1]]
      comp = ''.join(temp)
      if eval(comp.replace(' ','')) == 0:
        print(comp)
      return
    for i in range(3):
      op[n] = dop[i]
      func(n+1)
  func(0)
  print()