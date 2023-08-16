def solution(arr):
    prev = []
    idx = 0
    while True:
        for n in arr:
            if n>=50 and n%2==0:
                prev.append(n//2)
            elif n<50 and n%2:
                prev.append(n*2+1)
            else:
                prev.append(n)
        if prev==arr:
            return idx
        arr = [i for i in prev]
        prev = []
        idx += 1