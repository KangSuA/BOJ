def solution(rank, attendance):
    res = [(r,i) for i,r in enumerate(rank) if attendance[i]]
    res.sort()
    return 10000*res[0][1] + 100*res[1][1] + res[2][1]