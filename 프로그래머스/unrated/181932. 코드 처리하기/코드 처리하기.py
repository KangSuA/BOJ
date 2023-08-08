def solution(code):
    ret = ''
    mode = 0
    for idx in range(len(code)):
        if not mode:
            if code[idx]!='1' and not idx%2:
                ret += code[idx]
            elif code[idx]=='1':
                mode = 1
        else:
            if code[idx]!='1' and idx%2:
                ret += code[idx]
            elif code[idx]=='1':
                mode = 0
    if not ret:
        ret = "EMPTY"
    return ret
        