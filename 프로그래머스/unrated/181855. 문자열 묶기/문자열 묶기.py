def solution(strArr):
    cnt = [0]*31
    for s in strArr:
        cnt[len(s)] += 1
    return max(cnt)