T = 10
for t in range(1,T+1):
    N = int(input())
    building = list(map(int,input().split()))
    res = 0
    for i in range(2,N-2):
        diff = max(building[i-2],building[i-1],building[i+1],building[i+2])
        diff = building[i] - diff
        if diff > 0:
            res += diff
    print(f'#{t} {res}')