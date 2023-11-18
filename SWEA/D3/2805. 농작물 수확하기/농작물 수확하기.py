T = int(input())
for t in range(1,T+1):
    N = int(input())
    farm = []
    for i in range(N):
        farm.append(list(map(int,input())))
    rule = dict(zip(range(N//2,-1,-1),range(1,N+1,2)))
    res = 0
    for i in range(N//2+1):
        k = N//2-i
        val = rule[k]
        res += sum(farm[i][k:k+val])
    for i in range(N//2+1,N):
        k = i-N//2
        val = rule[k]
        res += sum(farm[i][k:k+val])
    print(f'#{t} {res}')