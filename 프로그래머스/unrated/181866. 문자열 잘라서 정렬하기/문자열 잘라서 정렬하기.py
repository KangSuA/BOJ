from collections import deque
def solution(myString):
    res = myString.split('x')
    while "" in res:
        res.remove("")
    return sorted(res)