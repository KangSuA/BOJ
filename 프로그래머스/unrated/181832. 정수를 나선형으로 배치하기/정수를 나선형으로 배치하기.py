def solution(n):
    res = [[0]*n for _ in range(n)]
    num = 1
    r = 0
    c = 0
    dir = [(0,1),(1,0),(0,-1),(-1,0)]
    cnt = [n-1]
    route = []
    for i in range(n-1,0,-1):
        cnt.append(i)
        cnt.append(i)
    di = 0
    for cc in cnt:
        route += [dir[di%4]]*cc
        di += 1
    
    for dr,dc in route:
        res[r][c] = num
        r += dr
        c += dc
        num += 1
    res[r][c] = num
    return res