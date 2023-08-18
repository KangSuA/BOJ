def solution(picture, k):
    res = []
    for p in picture:
        temp = []
        for pic in p:
            temp += [pic]*k
        res+=[''.join(temp)]*k
    return res