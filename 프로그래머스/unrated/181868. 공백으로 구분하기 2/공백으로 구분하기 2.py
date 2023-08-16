def solution(my_string):
    my_string = my_string.split(" ")
    res = []
    for s in my_string:
        if s:
            res.append(s)
    return res