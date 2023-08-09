def solution(arr, queries):
    for s,e,k in queries:
        res = list(filter(lambda x: x%k==0, range(s,e+1)))
        for r in res:
            arr[r] += 1
    return arr