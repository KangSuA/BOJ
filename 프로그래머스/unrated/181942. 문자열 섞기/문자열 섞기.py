def solution(str1, str2):
    res = []
    for i in range(len(str1)):
        res.append(str1[i])
        res.append(str2[i])
    answer = ''.join(res)
    return answer