from collections import deque
N, K, P, X = input().split()

N = int(N)
K = int(K)
P = int(P)
X = deque(map(int,X))
for _ in range(K-len(X)):
  X.appendleft(0)

led = [0b1111110,0b0110000,0b1101101,0b1111001,0b0110011,
       0b1011011,0b1011111,0b1110000,0b1111111,0b1111011]
dif = []
for i in range(10):
  temp = []
  for j in range(10):
    temp.append(bin(led[i]^led[j])[2:].count('1'))
  dif.append(temp)
  
res = 0
for i in range(1,N+1):
  now = deque(map(int,str(i)))
  for _ in range(K-len(now)):
    now.appendleft(0)
    
  change = 0
  for k in range(K):
    change += dif[X[k]][now[k]]
  if change<=P:
    res += 1
print(res-1)