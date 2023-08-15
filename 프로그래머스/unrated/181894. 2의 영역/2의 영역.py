def solution(arr):
    idx = []
    for i, n in enumerate(arr):
        if n==2:
            idx.append(i)
    if idx:
        return arr[idx[0]:idx[-1]+1]
    else:
        return [-1]