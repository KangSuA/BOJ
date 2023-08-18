def solution(order):
    res = 0
    for o in order:
        if "americano" in o:
            res += 4500
        elif "cafelatte" in o:
            res += 5000
        else:
            res += 4500
    return res                