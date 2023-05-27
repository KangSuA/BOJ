import sys
read = sys.stdin.readline
n = int(input())
array=[]
cnt=[0]*8001
for i in range(n):
  idata = int(read().rstrip())
  array.append(idata)
  cnt[idata]+=1

print(round(sum(array)/n)) #산술평균
array.sort()
print(array[n//2]) #중앙값
m = max(cnt)
c = 0
j = 0
for i in range(-4000,4001):
  if cnt[i] == m: 
    c+=1
    j=i
  if c==2: break
if c==1 or c==2: print(j) #최빈값
print(array[-1]-array[0]) #범위