def solution(n, lost, reserve):
    res = n-len(lost)
    lost.sort()
    reserve.sort()
    for i in range(1,n+1):
        if i in lost and i in reserve:
            lost.remove(i)
            reserve.remove(i)
            res += 1
    for r in reserve:
        if r-1 in lost:
            lost.remove(r-1)
            res += 1
        elif r+1 in lost:
            lost.remove(r+1)
            res += 1
    return res