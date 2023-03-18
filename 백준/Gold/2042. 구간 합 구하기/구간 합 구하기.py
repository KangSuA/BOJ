import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())

num = [0]*(n+1)
tree = [0]*(n+1)

def update(i,dif):
  while i<=n:
    tree[i] += dif
    i += (i&-i)

def prefix_sum(i): #누적합
  res = 0
  while i>0:
    res += tree[i]
    i -= (i&-i)
  return res

for i in range(1,n+1): #tree update
  x = int(input())
  num[i] = x
  update(i,x)

for _ in range(m+k):
  a,b,c = map(int,input().split())
  if a==1: #b번째수를 c로 바꾼다.
    update(b,c-num[b]) #새로운 값이 아니라 원래 값과 새로운 값의 차이 만큼 update해준다.
    num[b]=c
  if a==2: #b번째 수부터 c번째 수까지의 합을 출력
    print(prefix_sum(c)-prefix_sum(b-1)) # interval_sum 