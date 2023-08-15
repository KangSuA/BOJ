def solution(myString):
    res = myString.split('x')
    return [len(r) for r in res]