def solution(arr, flag):
    X = []
    for i,f in enumerate(flag):
        if f:
            for _ in range(arr[i]*2):
                X.append(arr[i])
        else:
            for _ in range(arr[i]):
                X.pop()
    return X