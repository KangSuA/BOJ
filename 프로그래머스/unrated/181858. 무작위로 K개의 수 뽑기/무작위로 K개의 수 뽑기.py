def solution(arr, k):
    res = []
    for a in arr:
        if a not in res:
            res.append(a)
        if len(res)==k:
            return res
    res += [-1]*(k-len(res))
    return res