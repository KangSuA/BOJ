from itertools import product
def solution(l, r):
    res = []
    num = 5
    mn_len = len(str(l))
    mx_len = len(str(r))
    for i in range(mn_len,mx_len+1):
        temp = list(product('50',repeat=i))
        for t in temp:
            res.append(int(''.join(t)))
    res = set(res)
    res = list(filter(lambda x:l<=x<=r,res))
    return sorted(res) if res else [-1]