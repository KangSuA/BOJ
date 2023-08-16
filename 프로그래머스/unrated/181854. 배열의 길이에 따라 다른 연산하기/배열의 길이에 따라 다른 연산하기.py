def solution(arr, n):
    s = 1
    if len(arr)%2:
        s=0   
    for i in range(s,len(arr),2):
        arr[i] += n
    return arr            