def solution(n):
    res = [[0]*n for i in range(n)]
    for i in range(n):
        res[i][i] = 1
    return res