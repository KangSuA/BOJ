def solution(arr):
    res = []
    for n in arr:
        res += [n for i in range(n)]
    return res