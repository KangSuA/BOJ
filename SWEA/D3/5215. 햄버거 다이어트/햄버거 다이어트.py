T = int(input())
for t in range(1,T+1):
    N, L = map(int,input().split())
    hamburger = [[0]*(L+1) for _ in range(N+1)]
    cal = [0]
    val = [0]
    for i in range(N):
        v, c = map(int,input().split())
        cal.append(c)
        val.append(v)
    for i in range(1,N+1):
        for j in range(1,L+1):
            c = cal[i]
            v = val[i]
            if j < c:
                hamburger[i][j] = hamburger[i-1][j]
            else:
                hamburger[i][j] = max(v + hamburger[i-1][j-c],hamburger[i-1][j])
    print(f'#{t} {hamburger[N][L]}')