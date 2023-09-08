N = input().rstrip()
digit = [0]*10
lenN = len(N)
for i,n in enumerate(N):
  n = int(n)
  pow10 = 10**(lenN-i-1)
  if i!=0:
    for k in range(10): #앞자리
      digit[k] += int(N[:i])*pow10
  for k in range(n): #자기자리
    digit[k] += pow10
  digit[0] -= pow10
  if i!=lenN-1:
    digit[n] += int(N[i+1:])+1 #뒷자리
  if i==lenN-1:
    digit[n] += 1
print(*digit)