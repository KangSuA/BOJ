def solution(arr, queries):
    res = []
    for s,e,k in queries:
        filt = list(filter(lambda x:x>k,arr[s:e+1]))
        res.append(min(filt) if filt else -1)
    return res