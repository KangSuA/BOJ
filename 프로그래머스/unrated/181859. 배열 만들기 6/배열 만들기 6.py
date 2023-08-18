def solution(arr):
    stk = []
    for a in arr:
        if not stk:
            stk.append(a)
        else:
            if stk[-1]==a:
                stk.pop()
            else:
                stk.append(a)
    if stk:
        return stk
    else:
        return [-1]
    