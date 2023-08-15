def solution(arr):
    res =  []
    for a in arr:
        if a>=50 and a%2==0:
            res.append(a//2)
        elif a<50 and a%2:
            res.append(a*2)
        else:
            res.append(a)
    return res