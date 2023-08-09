from collections import defaultdict
def solution(a, b, c, d):
    dic = defaultdict(int)
    dic[a] += 1
    dic[b] += 1
    dic[c] += 1
    dic[d] += 1
    res = sorted(list(dic.items()), key = (lambda x:(x[1],x[0])),reverse = True)
    if res[0][1] == 4:
        return 1111*res[0][0]
    elif res[0][1] == 3:
        return (10 * res[0][0] + res[1][0])**2
    elif res[0][1] == 2:
        if res[1][1] == 2:
            return (res[0][0] + res[1][0]) * abs(res[0][0] - res[1][0])
        else:
            return res[1][0] * res[2][0]
    else:
        return res[3][0]
            