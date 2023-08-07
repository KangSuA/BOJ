def solution(n):
    res = 0
    if n%2!=0:
        res = sum([i for i in range(1,n+1,2)])
    else:
        res = sum([i**2 for i in range(0,n+1,2)])
    return res