def solution(arr):
    two = 1
    while True:
        if len(arr)<=two:
            break
        two*=2
    arr += [0]*(two-len(arr))
    return arr