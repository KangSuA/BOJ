def solution(a, b, c):
    res = [(a**i+b**i+c**i) for i in range(1,4)]
    if a==b==c:
        return res[0]*res[1]*res[2]
    elif a==b or b==c or c==a:
        return res[0]*res[1]
    else:
        return res[0]