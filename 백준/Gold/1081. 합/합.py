L, U = input().split()
L, U = list(map(int,L)), list(map(int,U))

if len(U) == 1:
  print(U[0]*(U[0]+1)//2 - L[0]*(L[0]-1)//2)
  exit()

L.reverse()
U.reverse()
for _ in range(len(U)-len(L)):
  L.append(0)
cnt = [0]*10

for i in range(len(U)):
  if i==0:
    temp1 = U[i+1:]
    temp1.reverse()
    temp2 = L[i+1:]
    temp2.reverse()
    dif = int(''.join(map(str,temp1))) - int(''.join(map(str,temp2)))
    if U[i] >= L[i]:
      for j in range(10):
        cnt[j] += dif*(10**i)
      for j in range(L[i],U[i]+1):
        cnt[j] += 10**i
    else:
      for j in range(10):
        cnt[j] += dif*(10**i)
      for j in range(U[i]+1,L[i]):
        cnt[j] -= 10**i
    continue
  if i==len(U)-1:
    temp1 = U[:i]
    temp1.reverse()
    temp2 = L[:i]
    temp2.reverse()
    if U[i]==L[i]:
      cnt[U[i]] += int(''.join(map(str,temp1))) - int(''.join(map(str,temp2))) + 1
    else:
      cnt[U[i]] += int(''.join(map(str,temp1))) + 1
      cnt[L[i]] += 10**i - int(''.join(map(str,temp2)))
      for j in range(L[i]+1,U[i]):
        cnt[j] += 10**i
    continue
  #뒷자리
  temp1 = U[:i]
  temp1.reverse()
  cnt[U[i]] += int(''.join(map(str,temp1))) + 1
  temp2 = L[:i]
  temp2.reverse()
  cnt[L[i]] += 10**i - int(''.join(map(str,temp2)))
  #앞자리
  temp1 = U[i+1:]
  temp1.reverse()
  temp2 = L[i+1:]
  temp2.reverse()
  dif = int(''.join(map(str,temp1))) - int(''.join(map(str,temp2)))
  if U[i]-1 >= L[i]+1:
    for j in range(10):
        cnt[j] += dif*(10**i)
    for j in range(L[i]+1,U[i]):
      cnt[j] += 10**i
  else:
    for j in range(10):
        cnt[j] += dif*(10**i)
    for j in range(U[i],L[i]+1):
      cnt[j] -= 10**i
res = 0
for i in range(1,10):
  res += i*cnt[i]
print(res)