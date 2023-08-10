def solution(intStrs, k, s, l):
    res = []
    for i in intStrs:
        num = int(i[s:s+l])
        if num > k:
            res.append(num)
    return res